from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random
from sqlalchemy import func
import sys
import traceback

print("Starting application...")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exam.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

print("Initializing database...")
try:
    db = SQLAlchemy(app)
    print("Database initialized successfully")
except Exception as e:
    print(f"Error initializing database: {e}")
    traceback.print_exc()
    sys.exit(1)

print("Defining models...")
# 题目模型
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50), nullable=False)  # 学科
    question_type = db.Column(db.String(50), nullable=False)  # 题型
    content = db.Column(db.Text, nullable=False)  # 题目内容
    options = db.Column(db.Text)  # 选项（JSON格式）
    answer = db.Column(db.String(500), nullable=False)  # 答案
    explanation = db.Column(db.Text)  # 解析
    difficulty = db.Column(db.Integer)  # 难度等级（1-5）
    category = db.Column(db.String(50))  # 题目分类/考点

# 用户答题记录模型
class UserAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    user_answer = db.Column(db.String(500))
    is_correct = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    time_spent = db.Column(db.Integer)  # 答题用时（秒）
    attempt_count = db.Column(db.Integer, default=1)  # 尝试次数
    confidence_level = db.Column(db.Integer)  # 用户对答案的自信度（1-5）
    
    # 关联到题目
    question = db.relationship('Question', backref='user_answers')

print("Models defined successfully")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/questions', methods=['GET'])
def get_questions():
    subject = request.args.get('subject', 'all')
    question_type = request.args.get('type', 'all')
    difficulty = request.args.get('difficulty', 'all')
    is_exam = request.args.get('is_exam', 'false')
    
    query = Question.query
    
    if subject != 'all':
        query = query.filter_by(subject=subject)
    if question_type != 'all':
        query = query.filter_by(question_type=question_type)
    if difficulty != 'all':
        query = query.filter_by(difficulty=int(difficulty))
    
    questions = query.all()
    
    if is_exam == 'true':
        # 随机抽取100道题目组成试卷
        if len(questions) > 100:
            questions = random.sample(questions, 100)
        # 按学科和难度排序
        questions.sort(key=lambda x: (x.subject, x.difficulty))
    
    return jsonify([{
        'id': q.id,
        'subject': q.subject,
        'question_type': q.question_type,
        'content': q.content,
        'options': q.options,
        'difficulty': q.difficulty,
        'answer': q.answer
    } for q in questions])

@app.route('/api/submit_answer', methods=['POST'])
def submit_answer():
    data = request.json
    user_answer = UserAnswer(
        user_id=data['user_id'],
        question_id=data['question_id'],
        user_answer=data['answer'],
        is_correct=data['is_correct'],
        time_spent=data.get('time_spent', 0),
        confidence_level=data.get('confidence_level', 3)
    )
    db.session.add(user_answer)
    db.session.commit()
    return jsonify({'status': 'success'})

@app.route('/api/question/<int:question_id>', methods=['GET'])
def get_question(question_id):
    question = Question.query.get_or_404(question_id)
    return jsonify({
        'id': question.id,
        'subject': question.subject,
        'question_type': question.question_type,
        'content': question.content,
        'options': question.options,
        'answer': question.answer,
        'explanation': question.explanation,
        'difficulty': question.difficulty,
        'category': question.category
    })

@app.route('/api/personalized_questions')
def get_personalized_questions():
    try:
        print("Starting get_personalized_questions function")
        user_id = request.args.get('user_id', type=int)
        count = request.args.get('count', 10, type=int)
        subject = request.args.get('subject', 'all')
        
        print(f"Parameters received - user_id: {user_id}, count: {count}, subject: {subject}")
        
        if not user_id:
            print("Error: Missing user_id parameter")
            return jsonify({'error': 'Missing user_id parameter'}), 400
            
        # 获取用户的所有答题记录
        user_answers = UserAnswer.query.filter_by(user_id=user_id).all()
        print(f"Found {len(user_answers)} user answers")
        
        if not user_answers:
            print("No user answers found, returning random questions")
            questions = Question.query.order_by(func.random()).limit(count).all()
            print(f"Selected {len(questions)} random questions")
            return jsonify([{
                'id': q.id,
                'content': q.content,
                'options': q.options,
                'answer': q.answer,
                'explanation': q.explanation,
                'subject': q.subject,
                'question_type': q.question_type,
                'difficulty': q.difficulty
            } for q in questions])
            
        # 分析用户的错误模式
        error_patterns = {}
        for answer in user_answers:
            if not answer.is_correct:
                question = Question.query.get(answer.question_id)
                if question:
                    key = (question.subject, question.question_type)
                    if key not in error_patterns:
                        error_patterns[key] = 0
                    error_patterns[key] += 1
        
        print(f"Error patterns found: {error_patterns}")
                    
        # 根据错误模式获取题目
        questions = []
        for (subject_key, question_type), error_count in sorted(error_patterns.items(), key=lambda x: x[1], reverse=True):
            print(f"Processing subject: {subject_key}, type: {question_type}, error count: {error_count}")
            # 如果指定了学科，只获取该学科的题目
            if subject != 'all' and subject_key != subject:
                print(f"Skipping {subject_key} as it doesn't match requested subject {subject}")
                continue
                
            # 获取该类型的最新题目
            type_questions = Question.query.filter_by(
                subject=subject_key,
                question_type=question_type
            ).order_by(func.random()).limit(error_count).all()
            
            print(f"Found {len(type_questions)} questions for {subject_key} - {question_type}")
            questions.extend(type_questions)
            
        # 如果题目数量不足，补充随机题目
        if len(questions) < count:
            remaining = count - len(questions)
            print(f"Need {remaining} more questions to reach requested count")
            # 如果指定了学科，只获取该学科的随机题目
            if subject != 'all':
                random_questions = Question.query.filter_by(subject=subject).order_by(func.random()).limit(remaining).all()
            else:
                random_questions = Question.query.order_by(func.random()).limit(remaining).all()
            print(f"Added {len(random_questions)} random questions")
            questions.extend(random_questions)
            
        # 确保返回指定数量的题目
        questions = questions[:count]
        print(f"Final question count: {len(questions)}")
        
        return jsonify([{
            'id': q.id,
            'content': q.content,
            'options': q.options,
            'answer': q.answer,
            'explanation': q.explanation,
            'subject': q.subject,
            'question_type': q.question_type,
            'difficulty': q.difficulty
        } for q in questions])
        
    except Exception as e:
        print(f"Error in get_personalized_questions: {str(e)}")
        print(f"Error type: {type(e)}")
        import traceback
        print(f"Traceback: {traceback.format_exc()}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Creating database tables...")
    try:
        with app.app_context():
            db.create_all()
            print("Database tables created successfully")
            
            # 检查是否有题目数据
            question_count = Question.query.count()
            print(f"Current question count in database: {question_count}")
            
    except Exception as e:
        print(f"Error creating database tables: {e}")
        traceback.print_exc()
        sys.exit(1)
    
    print("Starting Flask development server...")
    app.run(host='localhost', port=8080, debug=True) 
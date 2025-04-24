from app import app, db, Question
import json

def generate_math_questions():
    questions = []
    
    # 数与代数（40题）
    for i in range(1, 21):
        # 基础运算题
        questions.append({
            'subject': 'math',
            'question_type': 'calculation',
            'content': f'计算：{i*2} × {i+3} + {i*3} = ?',
            'options': None,
            'answer': str(i*2 * (i+3) + i*3),
            'explanation': f'{i*2} × {i+3} = {i*2*(i+3)}, 再加{i*3}得{i*2*(i+3)+i*3}',
            'difficulty': min(1 + i//5, 5),
            'category': '基础运算'
        })
        # 方程题
        questions.append({
            'subject': 'math',
            'question_type': 'calculation',
            'content': f'解方程：{i}x + {i+5} = {i*10}',
            'options': None,
            'answer': str((i*10 - (i+5))/i),
            'explanation': f'{i}x + {i+5} = {i*10}\n{i}x = {i*10-i-5}\nx = {(i*10-i-5)/i}',
            'difficulty': min(2 + i//5, 5),
            'category': '方程解法'
        })

    # 几何题（30题）
    for i in range(1, 16):
        # 面积计算
        questions.append({
            'subject': 'math',
            'question_type': 'calculation',
            'content': f'一个长方形的长是{i+5}厘米，宽是{i+2}厘米，求面积。',
            'options': None,
            'answer': str((i+5)*(i+2)),
            'explanation': f'长方形面积 = 长 × 宽 = {i+5} × {i+2} = {(i+5)*(i+2)}平方厘米',
            'difficulty': min(1 + i//4, 5),
            'category': '几何计算'
        })
        # 周长计算
        questions.append({
            'subject': 'math',
            'question_type': 'calculation',
            'content': f'一个正方形的边长是{i+3}厘米，求周长。',
            'options': None,
            'answer': str((i+3)*4),
            'explanation': f'正方形周长 = 边长 × 4 = {i+3} × 4 = {(i+3)*4}厘米',
            'difficulty': min(1 + i//4, 5),
            'category': '几何计算'
        })

    # 应用题（30题）
    for i in range(1, 16):
        # 行程问题
        questions.append({
            'subject': 'math',
            'question_type': 'calculation',
            'content': f'小明步行速度是每小时{i+3}千米，骑自行车速度是步行速度的3倍。如果他从家到学校骑车需要{i}小时，那么步行需要多少小时？',
            'options': None,
            'answer': str(i*3),
            'explanation': f'骑车速度是步行速度的3倍，所以步行时间是骑车时间的3倍\n步行时间 = {i} × 3 = {i*3}小时',
            'difficulty': min(2 + i//4, 5),
            'category': '行程问题'
        })
        # 比例问题
        questions.append({
            'subject': 'math',
            'question_type': 'calculation',
            'content': f'一箱苹果共有{i*10}个，已经卖出{i*6}个，卖出的比例是多少？',
            'options': None,
            'answer': f'{i*6}/{i*10}',
            'explanation': f'卖出比例 = 卖出数量/总数量 = {i*6}/{i*10}',
            'difficulty': min(2 + i//4, 5),
            'category': '比例问题'
        })

    return questions

def generate_chinese_questions():
    questions = []
    
    # 成语题（25题）
    idioms = [
        ('守株待兔', '望梅止渴', '画蛇添足', '掩耳盗铃'),
        ('一举两得', '一石二鸟', '两全其美', '双喜临门'),
        ('入木三分', '锲而不舍', '持之以恒', '坚持不懈'),
        ('四面楚歌', '众叛亲离', '孤立无援', '孤军奋战'),
        ('五光十色', '绚丽多彩', '色彩斑斓', '五彩缤纷'),
        ('六神无主', '手足无措', '惊慌失措', '不知所措'),
        ('七上八下', '忐忑不安', '心神不定', '坐立不安'),
        ('八面玲珑', '圆滑世故', '处世圆通', '左右逢源'),
        ('九牛一毛', '微不足道', '沧海一粟', '杯水车薪'),
        ('十全十美', '完美无缺', '尽善尽美', '无懈可击'),
        ('胸有成竹', '运筹帷幄', '谋定后动', '成竹在胸'),
        ('一丝不苟', '精益求精', '严谨认真', '一丝不差'),
        ('画龙点睛', '点石成金', '妙笔生花', '锦上添花'),
        ('欣欣向荣', '蒸蒸日上', '蓬勃发展', '日新月异'),
        ('风起云涌', '波澜壮阔', '气势磅礴', '排山倒海'),
        ('披荆斩棘', '闯关夺隘', '勇往直前', '所向披靡'),
        ('集思广益', '博采众长', '取长补短', '兼收并蓄'),
        ('举一反三', '触类旁通', '闻一知十', '融会贯通'),
        ('循序渐进', '按部就班', '稳扎稳打', '步步为营'),
        ('精益求精', '精雕细琢', '追求完美', '精益求精'),
        ('学海无涯', '学无止境', '活到老学到老', '终身学习'),
        ('温故知新', '学而不厌', '温故而知新', '学而时习之'),
        ('勤能补拙', '笨鸟先飞', '勤学苦练', '勤学好问'),
        ('专心致志', '全神贯注', '聚精会神', '心无旁骛'),
        ('持之以恒', '坚持不懈', '锲而不舍', '百折不挠')
    ]
    
    for i, idiom_group in enumerate(idioms):
        questions.append({
            'subject': 'chinese',
            'question_type': 'choice',
            'content': f'下列成语中，与"{idiom_group[0]}"意思最接近的是：',
            'options': json.dumps([f'{chr(65+j)}. {idiom}' for j, idiom in enumerate(idiom_group[1:])]),
            'answer': 'A',
            'explanation': f'"{idiom_group[0]}"和"{idiom_group[1]}"意思相近。',
            'difficulty': min(1 + i//5, 5),
            'category': '成语辨析'
        })

    # 阅读理解（25题）
    passages = [
        {
            'text': '春天来了，小草偷偷地从土里钻出来，嫩嫩的，绿绿的。园子里的花朵们也你争我抢地开放了：桃花、杏花、梨花，争奇斗艳，白的像雪，粉的像霞，红的像火。',
            'questions': [
                ('这段话运用了什么修辞手法？', ['拟人、比喻', '夸张、排比', '对偶、明喻', '拟人、排比'], 'A', '文中"偷偷地钻出来"是拟人，"白的像雪，粉的像霞，红的像火"是比喻'),
                ('这段话主要描写了什么季节？', ['春天', '夏天', '秋天', '冬天'], 'A', '文中提到"春天来了"，并描写了春天的景象'),
                ('文中提到了哪些花？', ['桃花、杏花、梨花', '桃花、牡丹、梨花', '桃花、杏花、玫瑰', '玫瑰、杏花、梨花'], 'A', '文中明确提到"桃花、杏花、梨花"')
            ]
        },
        # 添加更多阅读理解文章...
    ]

    for passage in passages:
        for question, options, answer, explanation in passage['questions']:
            questions.append({
                'subject': 'chinese',
                'question_type': 'choice',
                'content': f'阅读以下短文：\n\n{passage["text"]}\n\n{question}',
                'options': json.dumps([f'{chr(65+i)}. {opt}' for i, opt in enumerate(options)]),
                'answer': answer,
                'explanation': explanation,
                'difficulty': 3,
                'category': '阅读理解'
            })

    # 语言基础（25题）
    for i in range(25):
        questions.append({
            'subject': 'chinese',
            'question_type': 'choice',
            'content': f'下列词语的使用正确的是：',
            'options': json.dumps([
                'A. 这件事情让他焦头烂额，高兴得不得了。',
                'B. 他做事总是半途而废，从来不会放弃。',
                'C. 这个问题很简单，我一目了然就明白了。',
                'D. 他说话总是语无伦次，条理非常清楚。'
            ]),
            'answer': 'C',
            'explanation': '一目了然：一眼就看清楚了，形容事物清晰明白，容易理解。',
            'difficulty': min(2 + i//5, 5),
            'category': '词语运用'
        })

    # 写作（25题）
    writing_topics = [
        '我的理想', '难忘的一天', '我最敬佩的人', '一次成功的经历',
        '我的好朋友', '最喜欢的季节', '一次失败的教训', '我的家乡',
        '一件快乐的事', '我的学习方法', '一次旅行见闻', '我的课外活动',
        '一个难忘的人', '我的业余爱好', '一次运动会', '我的成长经历',
        '一次帮助他人', '我的读书体会', '一次参观活动', '我的暑假生活',
        '一次野外观察', '我的新年愿望', '一次实践活动', '我的校园生活',
        '一次义工经历'
    ]

    for i, topic in enumerate(writing_topics):
        questions.append({
            'subject': 'chinese',
            'question_type': 'choice',
            'content': f'以"{topic}"为题写一篇作文，下列哪个开头最好？',
            'options': json.dumps([
                f'A. 说起{topic}，让我想起一件难忘的事。',
                f'B. 每个人都有关于{topic}的故事。',
                f'C. {topic}是一个值得深思的话题。',
                f'D. 生活中处处都有关于{topic}的感悟。'
            ]),
            'answer': 'A',
            'explanation': 'A选项开门见山，直接引入主题，并暗示后文将要讲述的具体事例。',
            'difficulty': min(2 + i//5, 5),
            'category': '作文指导'
        })

    return questions

def generate_english_questions():
    questions = []
    
    # 语法题（35题）
    grammar_patterns = [
        ('If it _____ tomorrow, we will go to the park.', ['rains', 'will rain', 'is raining', 'rained'], 'A', '在if条件句中，表示将来可能发生的事情时，条件句要用一般现在时'),
        ('She _____ in this company for ten years by next month.', ['will work', 'will be working', 'will have worked', 'works'], 'C', '表示到将来某时为止的动作，用将来完成时'),
        ('The book _____ by many students.', ['reads', 'is reading', 'is read', 'read'], 'C', '被动语态，表示书被阅读'),
        ('I wish I _____ fly like a bird.', ['can', 'could', 'will', 'would'], 'B', '在wish后面接虚拟语气，表示不可能实现的愿望'),
        ('He told me that he _____ busy the next day.', ['is', 'was', 'will be', 'would be'], 'D', '间接引语中的时态变化'),
        # ... 添加更多语法模式
    ]

    for i, (question, options, answer, explanation) in enumerate(grammar_patterns):
        questions.append({
            'subject': 'english',
            'question_type': 'choice',
            'content': f'Choose the correct answer: {question}',
            'options': json.dumps([f'{chr(65+j)}. {opt}' for j, opt in enumerate(options)]),
            'answer': answer,
            'explanation': explanation,
            'difficulty': min(2 + i//7, 5),
            'category': '语法'
        })

    # 词汇题（35题）
    vocabulary = [
        ('happy', ['happier', 'happiest', 'happiness', 'happily']),
        ('strong', ['stronger', 'strongest', 'strength', 'strongly']),
        ('teach', ['teaches', 'taught', 'teacher', 'teaching']),
        ('write', ['writes', 'wrote', 'written', 'writing']),
        ('good', ['better', 'best', 'well', 'goods']),
        ('high', ['higher', 'highest', 'height', 'highly']),
        ('long', ['longer', 'longest', 'length', 'longly']),
        ('wide', ['wider', 'widest', 'width', 'widely']),
        ('deep', ['deeper', 'deepest', 'depth', 'deeply']),
        ('warm', ['warmer', 'warmest', 'warmth', 'warmly']),
        # ... 添加更多词汇
    ]

    for i, (word, forms) in enumerate(vocabulary):
        questions.append({
            'subject': 'english',
            'question_type': 'choice',
            'content': f'Which is NOT a correct form of the word "{word}"?',
            'options': json.dumps([f'{chr(65+j)}. {form}' for j, form in enumerate(forms)]),
            'answer': 'D' if 'ly' in forms[3] and word not in ['deep', 'warm'] else 'C',
            'explanation': f'The word "{word}" has these forms: {", ".join(forms[:-1])}',
            'difficulty': min(2 + i//7, 5),
            'category': '词形变化'
        })

    # 阅读理解（30题）
    passages = [
        {
            'text': '''Tom is very busy today. He gets up at 7:00 and has breakfast at 7:30. 
            He goes to school at 8:00 and has four classes in the morning. After lunch, 
            he has two more classes. After school, he goes to the library to do his homework. 
            He comes home at 6:00 and has dinner with his family. 
            Then he watches TV for an hour before going to bed at 9:30.''',
            'questions': [
                ('What time does Tom get up?', ['6:00', '7:00', '7:30', '8:00'], 'B', 'The text clearly states "He gets up at 7:00"'),
                ('How many classes does Tom have in total?', ['4', '5', '6', '7'], 'C', 'He has four classes in the morning and two more after lunch'),
                ('What does Tom do after school?', ['Goes home', 'Plays sports', 'Goes to the library', 'Watches TV'], 'C', 'The text mentions "After school, he goes to the library"')
            ]
        },
        # ... 添加更多阅读理解文章
    ]

    for passage in passages:
        for question, options, answer, explanation in passage['questions']:
            questions.append({
                'subject': 'english',
                'question_type': 'choice',
                'content': f'Read the passage:\n\n{passage["text"]}\n\n{question}',
                'options': json.dumps([f'{chr(65+i)}. {opt}' for i, opt in enumerate(options)]),
                'answer': answer,
                'explanation': explanation,
                'difficulty': 3,
                'category': '阅读理解'
            })

    return questions

def init_questions():
    # 生成所有题目
    all_questions = (
        generate_math_questions() +
        generate_chinese_questions() +
        generate_english_questions()
    )
    
    # 添加所有题目到数据库
    for q in all_questions:
        question = Question(**q)
        db.session.add(question)
    
    db.session.commit()
    print(f"成功添加 {len(all_questions)} 道题目到数据库")

if __name__ == '__main__':
    with app.app_context():
        # 创建表
        db.create_all()
        # 清空现有数据
        db.session.query(Question).delete()
        db.session.commit()
        # 添加新数据
        init_questions()
        print("数据库初始化完成！") 
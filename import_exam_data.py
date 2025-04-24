# -*- coding: utf-8 -*-
from app import app, db, Question
import json

def import_exam_questions():
    questions_data = [
        # 数学 2020-2025
        {
            "subject": "math",
            "year": 2024,
            "questions": [
                # 难度1：基础计算
                {
                    "content": "计算：25 × 4 ÷ 2 = ?",
                    "options": None,
                    "answer": "50",
                    "explanation": "按照运算顺序：\n1. 先算乘法：25 × 4 = 100\n2. 再算除法：100 ÷ 2 = 50",
                    "question_type": "calculation",
                    "difficulty": 1,
                    "category": "基础运算"
                },
                # 难度2：简单应用题
                {
                    "content": "小明有30颗糖果，他分给了同学一些糖果后还剩下8颗，他分给了同学多少颗糖果？",
                    "options": None,
                    "answer": "22",
                    "explanation": "用减法计算：\n30 - 8 = 22\n所以小明分给同学22颗糖果",
                    "question_type": "calculation",
                    "difficulty": 2,
                    "category": "简单应用题"
                },
                # 难度3：分数计算
                {
                    "content": "计算：2/3 + 1/6 = ?",
                    "options": None,
                    "answer": "5/6",
                    "explanation": "1. 通分：2/3 = 4/6\n2. 相加：4/6 + 1/6 = 5/6",
                    "question_type": "calculation",
                    "difficulty": 3,
                    "category": "分数运算"
                },
                # 难度4：复杂应用题
                {
                    "content": "一个水箱中有水120升，每分钟放入8升水，同时每分钟放出5升水。20分钟后水箱中有多少升水？",
                    "options": None,
                    "answer": "180",
                    "explanation": "1. 每分钟净增加水量：8 - 5 = 3升\n2. 20分钟增加水量：3 × 20 = 60升\n3. 最终水量：120 + 60 = 180升",
                    "question_type": "calculation",
                    "difficulty": 4,
                    "category": "复杂应用题"
                },
                # 数学 难度4题目
                {
                    "content": "在△ABC中，∠A=30°，BC=8，AB=4，求△ABC的面积。",
                    "options": None,
                    "answer": "8",
                    "explanation": "1. 在△ABC中，已知一个角和两条边\n2. 三角形面积公式：S=(1/2)ab·sinC\n3. 代入数据：S=(1/2)×4×8×sin30°\n4. sin30°=0.5\n5. 所以S=(1/2)×4×8×0.5=8",
                    "question_type": "calculation",
                    "difficulty": 4,
                    "category": "几何题"
                },
                {
                    "content": "甲、乙两人同时从A地出发到B地，甲的速度是乙的2倍。当甲到达B地时，乙在距离B地15千米处。已知A、B两地相距45千米，求甲的速度是多少千米/小时？",
                    "options": None,
                    "answer": "30",
                    "explanation": "1. 设乙的速度为x千米/小时\n2. 则甲的速度为2x千米/小时\n3. 当甲到达B地时，乙走了30千米（45-15=30）\n4. 根据时间相等：45/(2x)=30/x\n5. 解得：x=15\n6. 所以甲的速度是30千米/小时",
                    "question_type": "calculation",
                    "difficulty": 4,
                    "category": "应用题"
                },
                # 数学 难度4题目（第二批）
                {
                    "content": "一个圆柱形容器，底面半径为5厘米，高为10厘米。现在向容器中倒入一个半径为2厘米的实心铁球，然后加入水直到容器装满。问：需要加入多少毫升水？（π取3.14）",
                    "options": None,
                    "answer": "707.3",
                    "explanation": "1. 圆柱体积=πr²h=3.14×5²×10=785立方厘米\n2. 铁球体积=(4/3)πr³=(4/3)×3.14×2³=33.5立方厘米\n3. 需要加入的水的体积=785-33.5=751.5立方厘米\n4. 1立方厘米=1毫升\n所以需要加入751.5-44.2=707.3毫升水",
                    "question_type": "calculation",
                    "difficulty": 4,
                    "category": "立体几何"
                },
                {
                    "content": "有一个数列：2, 3, 5, 9, 17, ___。这个数列的下一个数应该是多少？",
                    "options": None,
                    "answer": "33",
                    "explanation": "分析数列规律：\n每项与前一项的差：\n3-2=1\n5-3=2\n9-5=4\n17-9=8\n可以发现差值是以2的幂次递增：2⁰=1, 2¹=2, 2²=4, 2³=8\n所以下一个差值应该是2⁴=16\n因此下一个数是17+16=33",
                    "question_type": "calculation",
                    "difficulty": 4,
                    "category": "数列规律"
                },
                {
                    "content": "一个正方形，每条边长为8厘米。在正方形内部有一个圆，圆与正方形的每条边都相切。求这个圆的面积。",
                    "options": None,
                    "answer": "50.24",
                    "explanation": "1. 当圆与正方形的每条边相切时，圆的直径等于正方形的边长\n2. 所以圆的半径等于正方形边长的一半：r=8÷2=4厘米\n3. 圆的面积=πr²=3.14×4²=50.24平方厘米",
                    "question_type": "calculation",
                    "difficulty": 4,
                    "category": "几何"
                },
                # 数学 难度4题目（第三批）
                {
                    "content": "在一个长方体容器中，底面是边长为6厘米的正方形，高为h厘米。现在向容器中倒入800立方厘米的水，水深为5厘米。求这个容器的高h。",
                    "options": None,
                    "answer": "30",
                    "explanation": "1. 容器底面积=6×6=36平方厘米\n2. 水的体积=底面积×水深\n3. 800=36×5\n4. 验证等式成立\n5. 由于水深为5厘米，容器高度h必须大于5厘米\n6. 根据实际情况，h=30厘米",
                    "question_type": "calculation",
                    "difficulty": 4,
                    "category": "立体几何"
                },
                {
                    "content": "在一次随机调查中，某校学生对数学课的喜好程度分为：非常喜欢、比较喜欢、一般、不太喜欢四个等级。调查100名学生后，得到以下数据：非常喜欢20人，比较喜欢45人，一般25人，不太喜欢10人。如果从这100名学生中随机选择一名学生，求这名学生喜欢数学（非常喜欢或比较喜欢）的概率。",
                    "options": None,
                    "answer": "0.65",
                    "explanation": "1. 喜欢数学的学生=非常喜欢+比较喜欢=20+45=65人\n2. 总人数=100人\n3. 概率=喜欢的人数/总人数=65/100=0.65",
                    "question_type": "calculation",
                    "difficulty": 4,
                    "category": "概率统计"
                },
                {
                    "content": "已知函数f(x)=ax²+bx+c的图像过点A(1,2)和B(2,1)，且与x轴交于点C(3,0)。求参数a、b、c的值。",
                    "options": None,
                    "answer": "a=-1,b=4,c=-1",
                    "explanation": "1. 根据三点坐标：\n   f(1)=a+b+c=2\n   f(2)=4a+2b+c=1\n   f(3)=9a+3b+c=0\n2. 解方程组：\n   a+b+c=2\n   4a+2b+c=1\n   9a+3b+c=0\n3. 解得：a=-1,b=4,c=-1",
                    "question_type": "calculation",
                    "difficulty": 4,
                    "category": "函数与代数"
                },
                {
                    "content": "在△ABC中，AB=5，BC=6，AC=7，点D是BC上一点，AD⊥BC，求AD的长度。",
                    "options": None,
                    "answer": "4.8",
                    "explanation": "1. 根据海伦公式，先求三角形面积：\n   p=(5+6+7)/2=9\n   S=√(p(p-a)(p-b)(p-c))=√(9(4)(3)(2))=14.4\n2. AD为高，则：\n   S=(BC×AD)/2\n3. 14.4=(6×AD)/2\n4. 解得：AD=4.8",
                    "question_type": "calculation",
                    "difficulty": 4,
                    "category": "几何计算"
                },
                {
                    "content": "某商店购进一批商品，每件进价80元。如果定价120元销售，预计能售出200件；如果定价100元销售，预计能售出300件。为了获得最大利润，应当定价多少元？",
                    "options": None,
                    "answer": "100",
                    "explanation": "1. 设定价为120元时：\n   利润=(120-80)×200=8000元\n2. 设定价为100元时：\n   利润=(100-80)×300=6000元\n3. 比较两种情况：\n   120元定价利润为8000元\n   100元定价利润为6000元\n4. 因此应定价120元",
                    "question_type": "calculation",
                    "difficulty": 4,
                    "category": "应用题"
                },
                {
                    "content": "已知等比数列{an}的前三项为：a₁=2，a₂=6，a₃=18。求该数列的前10项的和。",
                    "options": None,
                    "answer": "39364",
                    "explanation": "1. 求公比q：q=a₂/a₁=6/2=3\n2. 通项公式：an=a₁q^(n-1)=2×3^(n-1)\n3. 等比数列求和公式：Sn=a₁(1-q^n)/(1-q)\n4. 代入n=10：\n   S₁₀=2(1-3^10)/(1-3)\n   =2(1-59049)/(-2)\n   =39364",
                    "question_type": "calculation",
                    "difficulty": 4,
                    "category": "数列"
                }
            ]
        },
        # 语文 2020-2025
        {
            "subject": "chinese",
            "year": 2024,
            "questions": [
                # 难度1：基础词语
                {
                    "content": "下列词语中的字形全部正确的是（）",
                    "options": json.dumps([
                        "A. 欢呼雀跃 蓬勃发展",
                        "B. 徘徊不定 异曲同工",
                        'C. "望子成龙 美不胜收"',
                        "D. 循循善诱 按部就班"
                    ]),
                    "answer": "D",
                    "explanation": "A项：正确\nB项：正确\nC项：引号使用错误\nD项：全部正确",
                    "question_type": "choice",
                    "difficulty": 1,
                    "category": "字形辨析"
                },
                # 难度2：成语运用
                {
                    "content": "下列句子中，成语使用恰当的是（）",
                    "options": json.dumps([
                        "A. 这个问题很简单，我一目了然就想到了答案",
                        "B. 他对工作兢兢业业，从不马马虎虎",
                        "C. 这次比赛他们全力以赴，结果事半功倍",
                        "D. 他的画技出神入化，令人叹为观止"
                    ]),
                    "answer": "D",
                    "explanation": "A项：一目了然形容看一眼就明白，不能'想到'\nB项：重复使用了表示认真和马虎的词语\nC项：事半功倍形容省力却收到加倍的效果，与全力以赴矛盾\nD项：使用正确",
                    "question_type": "choice",
                    "difficulty": 2,
                    "category": "成语运用"
                },
                # 难度3：阅读理解
                {
                    "content": "阅读下面的句子：\n春天来了，小草从土里钻出来，伸展着嫩绿的叶子。\n这句话运用了什么修辞手法？",
                    "options": json.dumps([
                        "A. 比喻",
                        "B. 拟人",
                        "C. 夸张",
                        "D. 对偶"
                    ]),
                    "answer": "B",
                    "explanation": "句子中把小草比作人，用'钻出来'和'伸展'这些通常用于描写人的动作来描写小草，这是拟人的修辞手法。",
                    "question_type": "choice",
                    "difficulty": 3,
                    "category": "修辞手法"
                },
                # 难度4：古诗文阅读
                {
                    "content": "阅读下面这首诗：\n独坐幽篁里，弹琴复长啸。\n深林人不知，明月来相照。\n这首诗抒发了作者怎样的情感？",
                    "options": json.dumps([
                        "A. 对官场的失意",
                        "B. 对自然的热爱",
                        "C. 超然物外的闲适",
                        "D. 对友人的思念"
                    ]),
                    "answer": "C",
                    "explanation": "这首诗描写了诗人独处竹林，与琴声、明月为伴的场景，表达了诗人超然物外、与自然相融的闲适心境。",
                    "question_type": "choice",
                    "difficulty": 4,
                    "category": "古诗文阅读"
                },
                # 语文 难度4题目
                {
                    "content": "阅读下面的文言文，回答问题：\n陈涉少时，尝与人佣耕，辍耕之垄上，怅恨久之，曰：'苟富贵，无相忘。'佣者笑而应曰：'若为佣耕，何富贵也？'陈涉太息曰：'嗟乎，燕雀安知鸿鹄之志哉！'\n这段文言文主要表达了作者怎样的思想感情？",
                    "options": json.dumps([
                        "A. 对命运的无奈和感叹",
                        "B. 对理想的坚定追求",
                        "C. 对现实的不满和批评",
                        "D. 对他人的轻蔑态度"
                    ]),
                    "answer": "B",
                    "explanation": "这段文言文通过陈涉与佣者的对话，展现了陈涉虽身处低微但心怀大志的形象。'燕雀安知鸿鹄之志'一句，表达了他对理想的坚定追求，不甘平庸的志向。",
                    "question_type": "choice",
                    "difficulty": 4,
                    "category": "文言文阅读"
                },
                {
                    "content": "阅读下面的诗句：\n商女不知亡国恨，隔江犹唱后庭花。\n这首诗表达了诗人怎样的情感？",
                    "options": json.dumps([
                        "A. 对歌女的同情",
                        "B. 对时局的担忧",
                        "C. 对往事的追忆",
                        "D. 对现实的讽刺"
                    ]),
                    "answer": "B",
                    "explanation": "这是杜牧的诗作，诗中表面写歌女在亡国后仍在歌唱艳曲，实则表达了诗人对时局的深切忧虑。'后庭花'是亡国之音，暗指当时社会的奢靡风气可能导致亡国。",
                    "question_type": "choice",
                    "difficulty": 4,
                    "category": "诗歌鉴赏"
                },
                # 语文 难度4题目（第二批）
                {
                    "content": "阅读下面的文言文，回答问题：\n庖丁为文惠君解牛，手之所触，肩之所倚，足之所履，膝之所倚，砉然响然，奏刀騞然，莫不中音。合于《桑林》之舞，乃中《经首》之会。\n文中'砉然响然'运用了什么修辞手法？这样写有什么表达效果？",
                    "options": json.dumps([
                        "A. 拟声词，生动形象地描绘了庖丁熟练解牛的场景",
                        "B. 叠词，突出强调解牛的动作节奏感",
                        "C. 夸张，突出庖丁解牛技艺的高超",
                        "D. 比喻，将解牛比作音乐演奏"
                    ]),
                    "answer": "A",
                    "explanation": "'砉然响然'是拟声词，模仿解牛时发出的声音，生动形象地描绘了庖丁解牛时干净利落、节奏分明的动作，突出其技艺的精湛。",
                    "question_type": "choice",
                    "difficulty": 4,
                    "category": "文言文阅读"
                },
                {
                    "content": "分析下面这首诗的写作特点：\n白日依山尽，黄河入海流。\n欲穷千里目，更上一层楼。\n这首诗在结构上有什么特点？",
                    "options": json.dumps([
                        "A. 首联写景，末联抒情，前后照应",
                        "B. 上下两联互为因果，结构严谨",
                        "C. 前两句铺垫，后两句深化主题",
                        "D. 上下两联形成对比，突出主题"
                    ]),
                    "answer": "B",
                    "explanation": "这首诗上下两联互为因果：首联写看到的景象（日落、河流），表明视线受阻；末联是为了看得更远而采取的行动，两联之间有密切的因果关系，结构严谨。",
                    "question_type": "choice",
                    "difficulty": 4,
                    "category": "诗歌鉴赏"
                }
            ]
        },
        # 英语 2020-2025
        {
            "subject": "english",
            "year": 2024,
            "questions": [
                # 难度1：基础词汇
                {
                    "content": "Choose the correct word: The opposite of 'hot' is ________.",
                    "options": json.dumps([
                        "A. warm",
                        "B. cool",
                        "C. cold",
                        "D. wet"
                    ]),
                    "answer": "C",
                    "explanation": "'Cold' is the opposite (antonym) of 'hot'. While 'cool' is also related, 'cold' is the most direct opposite.",
                    "question_type": "choice",
                    "difficulty": 1,
                    "category": "词汇"
                },
                # 难度2：简单语法
                {
                    "content": "Fill in the blank: She ________ to school every day.",
                    "options": json.dumps([
                        "A. go",
                        "B. goes",
                        "C. going",
                        "D. went"
                    ]),
                    "answer": "B",
                    "explanation": "第三人称单数（she）在一般现在时中，动词要加's'。",
                    "question_type": "choice",
                    "difficulty": 2,
                    "category": "语法"
                },
                # 难度3：情景对话
                {
                    "content": "Complete the dialogue:\nA: Would you like some tea?\nB: ________",
                    "options": json.dumps([
                        "A. Yes, I would.",
                        "B. Yes, I do.",
                        "C. Yes, I am.",
                        "D. Yes, I can."
                    ]),
                    "answer": "A",
                    "explanation": "当被问'Would you like...'时，正确的回答应该用相同的助动词'would'。",
                    "question_type": "choice",
                    "difficulty": 3,
                    "category": "情景对话"
                },
                # 难度4：阅读理解
                {
                    "content": "Read the passage:\nTom loves reading. He reads different kinds of books, but his favorite books are science fiction. He usually borrows books from the library, but sometimes he buys books online. Last month, he read five books.\n\nQuestion: Which statement is NOT true according to the passage?",
                    "options": json.dumps([
                        "A. Tom enjoys reading science fiction most.",
                        "B. Tom only reads science fiction books.",
                        "C. Tom borrows books from the library.",
                        "D. Tom read five books last month."
                    ]),
                    "answer": "B",
                    "explanation": "根据文章，Tom读各种类型的书(different kinds of books)，只是最喜欢科幻类(favorite books are science fiction)。因此B选项'Tom只读科幻小说'与文章内容不符。",
                    "question_type": "choice",
                    "difficulty": 4,
                    "category": "阅读理解"
                },
                # 英语 难度4题目
                {
                    "content": "Read the passage and answer the question:\n\nIn recent years, scientists have made remarkable progress in understanding how the brain processes information during sleep. While we sleep, our brains are far from inactive. Instead, they are busy consolidating memories, processing emotions, and preparing for the next day. This discovery has led to new theories about the role of sleep in learning and memory formation.\n\nWhat is the main idea of this passage?",
                    "options": json.dumps([
                        "A. Sleep is important for physical rest",
                        "B. The brain remains active during sleep",
                        "C. Scientists study sleep patterns",
                        "D. Memory formation occurs only during sleep"
                    ]),
                    "answer": "B",
                    "explanation": "The passage primarily discusses how the brain remains active during sleep, processing information and performing various functions. This is supported by examples of brain activities like memory consolidation and emotional processing.",
                    "question_type": "choice",
                    "difficulty": 4,
                    "category": "阅读理解"
                },
                {
                    "content": "Complete the sentence with the correct form:\nIf he ________ (study) harder last semester, he ________ (pass) the exam.",
                    "options": json.dumps([
                        "A. studied, would pass",
                        "B. had studied, would have passed",
                        "C. has studied, would pass",
                        "D. studied, had passed"
                    ]),
                    "answer": "B",
                    "explanation": "This is a third conditional sentence expressing an impossible past condition and its result. The correct structure is: If + past perfect (had + past participle), would have + past participle.",
                    "question_type": "choice",
                    "difficulty": 4,
                    "category": "语法"
                },
                # 英语 难度4题目（第二批）
                {
                    "content": "Read the passage and answer the question:\n\nThe concept of 'digital natives' versus 'digital immigrants' has been widely discussed in educational circles. While younger generations who grew up with technology are often assumed to be naturally skilled at using digital tools, recent research suggests that this distinction may be oversimplified. Many young people, despite their familiarity with social media and entertainment apps, lack critical digital literacy skills needed for academic and professional success.\n\nWhat is the main argument of this passage?",
                    "options": json.dumps([
                        "A. Young people are better at using technology than older generations",
                        "B. The digital native concept is too simplistic and potentially misleading",
                        "C. Digital literacy skills are essential for academic success",
                        "D. Social media use doesn't guarantee digital competence"
                    ]),
                    "answer": "B",
                    "explanation": "The passage challenges the simple division between 'digital natives' and 'digital immigrants', suggesting that this categorization is oversimplified ('may be oversimplified'). It points out that despite growing up with technology, young people may still lack important digital skills.",
                    "question_type": "choice",
                    "difficulty": 4,
                    "category": "阅读理解"
                },
                {
                    "content": "Choose the best way to combine these sentences:\nThe storm was severe. It caused significant damage. Many buildings were destroyed. The power was out for days.\n",
                    "options": json.dumps([
                        "A. The severe storm caused significant damage, destroying many buildings and leaving the power out for days.",
                        "B. The storm was severe and it caused significant damage and many buildings were destroyed and the power was out for days.",
                        "C. Because the storm was severe, it caused significant damage, also many buildings were destroyed, and the power was out for days.",
                        "D. The storm, which was severe, caused significant damage, and many buildings were destroyed, while the power was out for days."
                    ]),
                    "answer": "A",
                    "explanation": "Option A is the most concise and well-structured combination, using participle phrases ('destroying', 'leaving') to show the relationship between events while avoiding unnecessary repetition and maintaining clear logical connections.",
                    "question_type": "choice",
                    "difficulty": 4,
                    "category": "句子重组"
                }
            ]
        }
    ]

    try:
        with app.app_context():
            # 遍历所有题目数据并添加到数据库
            for subject_data in questions_data:
                subject = subject_data["subject"]
                year = subject_data["year"]
                
                for q_data in subject_data["questions"]:
                    # 创建新的题目对象
                    question = Question(
                        subject=subject,
                        content=q_data["content"],
                        options=q_data["options"],
                        answer=q_data["answer"],
                        explanation=q_data["explanation"],
                        question_type=q_data["question_type"],
                        difficulty=q_data["difficulty"],
                        category=q_data["category"]
                    )
                    
                    # 添加到数据库
                    db.session.add(question)
            
            # 提交所有更改
            db.session.commit()
            print("Successfully imported exam questions!")
            
            # 打印导入后的题目统计
            math_count = Question.query.filter_by(subject="math").count()
            chinese_count = Question.query.filter_by(subject="chinese").count()
            english_count = Question.query.filter_by(subject="english").count()
            
            print(f"\nCurrent question count in database:")
            print(f"Math: {math_count}")
            print(f"Chinese: {chinese_count}")
            print(f"English: {english_count}")
            print(f"Total: {math_count + chinese_count + english_count}")
            
            # 打印每个难度等级的题目数量
            for difficulty in range(1, 5):
                count = Question.query.filter_by(difficulty=difficulty).count()
                print(f"Difficulty {difficulty}: {count} questions")
            
            # 打印难度4题目的分类统计
            difficulty_4_categories = db.session.query(Question.category, db.func.count(Question.id)).\
                filter_by(difficulty=4).\
                group_by(Question.category).\
                all()
            
            print("\nDifficulty 4 questions by category:")
            for category, count in difficulty_4_categories:
                print(f"{category}: {count} questions")
            
    except Exception as e:
        print(f"Error importing questions: {e}")
        db.session.rollback()

if __name__ == "__main__":
    import_exam_questions() 
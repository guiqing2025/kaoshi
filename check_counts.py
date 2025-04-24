import sqlite3

def check_question_counts():
    try:
        conn = sqlite3.connect('exam.db')
        cursor = conn.cursor()
        
        # 查询各科目题目数量
        subjects = ['math', 'chinese', 'english']
        for subject in subjects:
            count = cursor.execute(
                'SELECT COUNT(*) FROM questions WHERE subject = ?', 
                (subject,)
            ).fetchone()[0]
            print(f'{subject.capitalize()} questions: {count}')
            
    except sqlite3.Error as e:
        print(f'数据库错误: {e}')
    except Exception as e:
        print(f'发生错误: {e}')
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == '__main__':
    check_question_counts() 
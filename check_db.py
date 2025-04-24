print("Script starting...")
import sqlite3
import sys  # 添加sys模块导入

print("Script starting...")  # Add initial debug output

def check_db_content():
    print("Entering check_db_content function...")
    print("开始检查数据库...")
    sys.stdout.flush()
    try:
        print("尝试连接数据库...")
        sys.stdout.flush()
        conn = sqlite3.connect('exam.db')
        cursor = conn.cursor()
        print("成功连接到数据库！")
        sys.stdout.flush()
        
        # 检查表是否存在
        print("检查数据库表...")
        sys.stdout.flush()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print(f"找到 {len(tables)} 个表")
        sys.stdout.flush()
        print("数据库中的表：")
        for table in tables:
            print(f"- {table[0]}")
            sys.stdout.flush()
            
        # 如果question表存在，检查其结构
        print("\n正在检查question表结构...")
        sys.stdout.flush()
        try:
            cursor.execute("PRAGMA table_info(question);")
            columns = cursor.fetchall()
            if columns:
                print("\nquestion表的结构：")
                for col in columns:
                    print(f"- {col[1]} ({col[2]})")
                    sys.stdout.flush()
            else:
                print("question表没有列信息")
                sys.stdout.flush()
        except sqlite3.Error as e:
            print(f"检查question表结构时出错: {e}")
            sys.stdout.flush()
            
        # 检查每个科目的记录数
        print("\n正在统计各科目题目数量...")
        sys.stdout.flush()
        try:
            cursor.execute("SELECT subject, COUNT(*) FROM question GROUP BY subject;")
            counts = cursor.fetchall()
            print("\n各科目题目数量：")
            for subject, count in counts:
                print(f"- {subject}: {count}题")
                sys.stdout.flush()
        except sqlite3.Error as e:
            print(f"统计科目题目数量时出错: {e}")
            sys.stdout.flush()
                
        # 显示每个科目的一个样例记录
        print("\n正在获取各科目样例记录...")
        sys.stdout.flush()
        for subject in ['math', 'chinese', 'english']:
            try:
                cursor.execute("SELECT * FROM question WHERE subject = ? LIMIT 1;", (subject,))
                row = cursor.fetchone()
                if row:
                    print(f"\n{subject}科目样例：")
                    print(row)
                    sys.stdout.flush()
                else:
                    print(f"\n未找到{subject}科目的记录")
                    sys.stdout.flush()
            except sqlite3.Error as e:
                print(f"获取{subject}科目样例时出错: {e}")
                sys.stdout.flush()
                    
    except sqlite3.Error as e:
        print(f"数据库错误: {e}")
        sys.stdout.flush()
    except Exception as e:  # 添加通用异常捕获
        print(f"发生错误: {e}")
        sys.stdout.flush()
    finally:
        if 'conn' in locals():
            conn.close()
            print("数据库连接已关闭")
            sys.stdout.flush()

if __name__ == '__main__':
    print("Main block starting...")
    check_db_content() 
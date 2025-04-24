from app import app, db

def update_database():
    with app.app_context():
        # 删除旧的 user_answer 表
        db.session.execute('DROP TABLE IF EXISTS user_answer')
        db.session.commit()
        
        # 重新创建所有表
        db.create_all()
        print("数据库表结构已更新！")

if __name__ == '__main__':
    update_database() 
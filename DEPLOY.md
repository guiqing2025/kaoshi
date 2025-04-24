# 部署指南

## PythonAnywhere 免费部署步骤

1. 注册账号
- 访问 www.pythonanywhere.com
- 注册一个免费账号

2. 上传代码
- 点击 Files 标签
- 使用 Upload a file 上传所有项目文件
- 或使用 git clone（如果项目在GitHub上）

3. 设置虚拟环境
```bash
mkvirtualenv --python=/usr/bin/python3.8 myenv
workon myenv
pip install -r requirements.txt
```

4. 配置Web应用
- 点击 Web 标签
- 点击 Add a new web app
- 选择 Flask
- 设置 Source code: /home/你的用户名/你的项目目录
- 设置 Working directory: /home/你的用户名/你的项目目录
- 设置 WSGI configuration file:
```python
import sys
path = '/home/你的用户名/你的项目目录'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

5. 设置环境变量
- 在 Web 标签页下找到 Environment variables
- 添加必要的环境变量（如数据库URL等）

6. 重启应用
- 点击 Reload 按钮

## 注意事项
- 免费账号的网站每天有一定的CPU时间限制
- 每3个月需要登录一次以保持网站活跃
- 数据库建议使用PythonAnywhere提供的MySQL
- 静态文件（CSS/JS等）需要在Web配置中设置静态文件路径 
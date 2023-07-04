import os


basedir = os.path.abspath(os.path.dirname(__file__))#获取当前.py文件的绝对路径
from dotenv import load_dotenv

load_dotenv(os.path.join(basedir, 'microblog.env'))

class Config:
		SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'

		SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
		SQLALCHEMY_TRACK_MODIFICATIONS = False

		MAIL_SERVER = os.environ.get('MAIL_SERVER')
		MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
		MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
		MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'false').lower() in ['true', 'on', '1']
		MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
		MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  # 客户端授权密码

		ADMINS = ['your-email@example.com']
		POSTS_PER_PAGE = 3

		LANGUAGES = ['en', 'zh']

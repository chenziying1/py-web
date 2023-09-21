# -*- coding: utf-8 -*-
# time:2023/8/10 9:02
# file test.py
# outhor:czy
# email:1060324818@qq.com

from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace these values with your MySQL server credentials
user = 'sa'
password = ''
host = 'localhost'
database_name = 'flask_yiyao' #需要提前在mysql上新建这个数据库

# Create a database connection
engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database_name}")
Base = declarative_base()

# Define the User and Post models

class ys(Base):
    __tablename__ = 'ys'
    id = Column(Integer, primary_key=True)
    用户名 = Column(String(50), nullable=False)
    账号 = Column(String(100), nullable=False)
    密码 = Column(String(500), nullable=False)
    状态 = Column(String(100), nullable=False)
    邮箱 = Column(String(100), nullable=False)
    开处方权限 = Column(String(50), nullable=False)
    用药方案权限 = Column(String(100), nullable=False)
    健康档案权限 = Column(String(50), nullable=False)
    用药管理权限 = Column(String(100), nullable=False)
    评价权限 = Column(String(50), nullable=False)

class hz(Base):
    __tablename__ = 'hz'
    id = Column(Integer, primary_key=True)
    用户名 = Column(String(50), nullable=False)
    账号 = Column(String(100), nullable=False)
    密码 = Column(String(500), nullable=False)
    状态 = Column(String(100), nullable=False)
    邮箱 = Column(String(100), nullable=False)
    健康档案权限 = Column(String(50), nullable=False)
    用药管理权限 = Column(String(100), nullable=False)
    评价权限 = Column(String(50), nullable=False)



class yw(Base):
    __tablename__ = 'yw'
    id = Column(Integer, primary_key=True)
    药物名称 = Column(String(50), nullable=False)
    药物厂商 = Column(String(100), nullable=False)
    状态 = Column(String(50), nullable=False)

class 用药方案(Base):
    __tablename__ = '用药方案'
    id = Column(Integer, primary_key=True)
    处方名称 = Column(String(50), nullable=False)
    患者名称 = Column(String(50), nullable=False)
    用药名称 = Column(String(50), nullable=False)
    用药计量 = Column(String(50), nullable=False)
    时间 = Column(String(50), nullable=False)
    状态 = Column(String(50), nullable=False)
    备注 = Column(String(50), nullable=False)
    医生名称 = Column(String(50), nullable=False)
    实际服用时间 = Column(String(50), nullable=False)
    计划服用时间 = Column(String(50), nullable=False)

class 管理用户(Base):
    __tablename__ = '管理用户'
    id = Column(Integer, primary_key=True)
    医生名称 = Column(String(50), nullable=False)
    患者名称 = Column(String(50), nullable=False)

class 评价(Base):
    __tablename__ = '评价'
    id = Column(Integer, primary_key=True)
    患者名称 = Column(String(50), nullable=False)
    评价内容 = Column(String(50), nullable=False)
    处方名称 = Column(String(50), nullable=False)
    评价时间 = Column(String(50), nullable=False)

class 用药方案提醒(Base):
    __tablename__ = '用药方案提醒'
    id = Column(Integer, primary_key=True)
    患者名称 = Column(String(50), nullable=False)
    提醒时间 = Column(String(50), nullable=False)

class 药物提醒(Base):
    __tablename__ = '药物提醒'
    id = Column(Integer, primary_key=True)
    患者名称 = Column(String(50), nullable=False)
    服用时间 = Column(String(50), nullable=False)
    药物名称 = Column(String(50), nullable=False)
    用药方案名称 = Column(String(50), nullable=False)

# Create the tables
Base.metadata.create_all(engine)

if __name__ == "__main__":
    try:
        Session = sessionmaker(bind=engine)
        session = Session()

        print("Database and tables created successfully.")

    except Exception as e:
        print("Error:", e)

    finally:
        session.close()



'''
Create by YO
@Time:
'''
from flask_login import login_manager, UserMixin

'''
Create by YO
@Time:
'''
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, Float, SmallInteger

db=SQLAlchemy()    #实例化sqlalchemy对象

class User(db.Model,UserMixin):
    # __tablename__='login_register'
    id = Column(Integer,autoincrement=True,primary_key=True)
    #autoincrement自增长
    username=Column(String(50),nullable=False)
    password=Column(String(128),nullable=True)


    # 没有这个的话，使用{{users}}显示的就是一个对象
    def __repr__(self):
        return self.username


# #打上下面的装饰器flask才知道要调用下面这个函数
@login_manager.user_loader
def get_user(user_id):
    #对主键的查询是没有必要使用filler_by的
    return User.query.get(user_id)
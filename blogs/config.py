'''
Create by YO
@Time: 
'''
DEBUG=True
#配置sqlalchemy连接数据库，因为是机密文件，所以放在这里，下面的SQLALCHEMY_DATABASE_URI=是固定的，不可变，改了字母的话FLASK会找不到数据库配置连接
#sqlalchemy不会要求你一定要是用那种驱动，cymysql是一种驱动模式，需要自己安装
SQLALCHEMY_DATABASE_URI='mysql+cymysql://root:762382@localhost:3306/blog'
SECRET_KEY='ASDADASDAASCA12412'
SQLALCHEMY_TRACK_MODIFICATIONS=False
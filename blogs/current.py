'''
Create by YO
@Time: 
'''
from flask import Flask
from flask_login import LoginManager
from flask import session,redirect,url_for,flash

from blogs.front_back import front
from blogs.modles.dbmodels import db

login_manager = LoginManager()


def create_app():
    app=Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    db.init_app(app)


    login_manager.init_app(app)
    login_manager.login_view="url_for('front.login')"
    # login_manager.login_message='请先登录或注册'

    db.create_all(app=app)
    return app


def register_blueprint(app):
    from blogs.front_back import front
    app.register_blueprint(front)


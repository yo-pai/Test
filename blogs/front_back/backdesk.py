'''
Create by YO
@Time: 
'''
from flask import render_template, session, redirect, url_for
from blogs.front_back import front
from flask_login import login_required
#只需要在需要验证的地方加上@login_required装饰器就可以实现

@front.route('/index')
# @login_check
def index():
    return render_template("index.html")

@front.route('/article_detail')
# @login_check
def article_detail():
    return render_template("article_detail.html")

@front.route('/add_article')
@login_required
def add_article():
    return render_template("add_article.html")


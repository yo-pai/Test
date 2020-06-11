'''
Create by YO
@Time: 
'''
from flask import render_template, redirect, url_for, request, flash, session
from blogs.front_back import front
from blogs.modles.dbmodels import User, db
import hashlib

from utils import login_check


@front.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    elif request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        user=User.query.filter_by(username=username,password=password).first()
        if user:
            session['user']=username
            print(session['user'])
            flash('登录成功')
            return redirect(url_for('front.index'))
        else:
            flash('登录失败')
            return redirect(url_for('front.login'))

@front.route('/register',methods=['GET','POST'])
def register():
        # 如果是get请求的话就返回页面，post请求的话就接收表单数据
        if request.method == 'GET':
            return render_template("register.html")
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            check_password = request.form.get('check_password')

            if username and password and password == check_password:
                md5 = hashlib.md5()
                md5.update(password.encode('utf-8'))
                user = User()

                user.username = username
                # 使用hashlib加密密码再存入数据库,拿到md5.hexdigest()加密后的密码
                user.password = md5.hexdigest()
                user.password=password
                print(username,password)

            try:
               db.session.add(user)
               db.session.commit()
               flash('注册成功，欢迎访问我的个人博客！')
               return redirect(url_for('front.register'))
            except Exception:
               flash('注册失败，请检查密码后重新注册')
               return redirect(url_for('front.register'))
        else:
             flash('注册失败')
             return redirect(url_for('front.register'))

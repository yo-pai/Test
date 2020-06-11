'''
Create by YO
@Time: 2020/5/31
'''

from flask import session,redirect,url_for,flash
def login_check(func):
    def inner(*args,**kwargs):
        #如果session里面是有user的话，那么允许放访问
        if not session.get('user'):
            flash('请登录后再来操作')
            return redirect(url_for('front.login'))

        return func(*args,**kwargs)
    return inner

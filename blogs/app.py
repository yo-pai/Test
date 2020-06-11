'''
Create by YO
@Time:
'''
from flask import Flask, render_template, request, jsonify
# from blogs.models.db import db, User2

from blogs.current import create_app

app=create_app()



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=81)
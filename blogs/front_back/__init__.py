'''
Create by YO
@Time: 
'''
from flask import Blueprint
front=Blueprint('front',__name__)
from blogs.front_back import admit_register
from blogs.front_back import backdesk

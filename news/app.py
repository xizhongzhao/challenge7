#!/usr/bin/env python3
#
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sys 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/shiyanlou'
db = SQLAlchemy(app)
sys.path.append('/home/shiyanlou/challeng7/news')

class File(db.Model):
    __tablename__ = 'file'
    id = db.Column(db.Integer,primary_key=True,index=True)
    title = db.Column(db.String(80),unique=True)
    created_time = db.Column(db.DateTime,nullable=True)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    category = db.relationship('Category',backref=db.backref('posts',lazy='dynamic'))
    content = db.Column(db.Text)

    def __init__(self,title,created_time,category,content):
        self.title = title
        if created_time is None:
            created_time = created_time
        self.created_time = created_time
        self.category = category
        self.content = content

    def __repr__(self):
        return '<Article %r>' %self.title

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer,primary_key=True,index=True)
    name = db.Column(db.String(80))

    def __init__(self,name):
        self.name=name

    def __repr__(self):
        return '<Category %r>' %self.name



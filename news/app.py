#!/usr/bin/env python3
#
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/shiyanlou'
db = SQLAlchemy(app)

class File(db.Model):
    id = db.Column(db.Integer,primary_key=True,index=True)
    title = db.Column(db.String(80),unique=True)
    created_time = db.Column(db.DateTime,nullable=True)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    category = db.relationship('Category',backref='files')
    content = db.Column(db.Text)
    
    def __init__(self,title,created_time,category_id,content):
        self.title = title
        self.created_time = created_time
        self.category_id = category_id
        self.content = content
    
    def __repr__(self):
        return '<File %r>' %self.title

class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True,index=True)
    name = db.Column(db.String(80))
    
    def __init__(self,name):
       self.name = name

    def __repr__(self):
        return '<Category %r>' %self.name 

@app.route('/')
def index():
    pass


@app.route('/files/<file_id>')
def file(file_id):
    pass

if __name__ == '__main__':
    app.run()

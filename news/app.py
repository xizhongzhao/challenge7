#/usr/bin/env python3

import json
import os,os.path
from flask import Flask,abort,render_template

def filedict_from_json(filename_arg):
    with open(filename_arg,'r') as file:
        filedict = json.loads(file.read())
    return filedict

filename_list = os.listdir('../files')
file_dict_list = [ filedict_from_json('../files/'+filename_json) \
                  for filename_json in filename_list ]
title_list = [ file_dict.get('title')  for file_dict in file_dict_list ]


app = Flask(__name__)

@app.route('/')
def index():
    title_list = [ file_dict.get('title') for file_dict in file_dict_list ]
    return render_template('index.html',title_list=title_list)

@app.route('/files/<filename>')
def file(filename):
    try:
        file_dict = filedict_from_json('../files/'+filename+'.json')
    except:
        return render_template('404.html'),404
    return render_template("file.html",file_dict=file_dict)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404

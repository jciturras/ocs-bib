# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 18:12:13 2021

@author: Julio
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello this is the new version!"

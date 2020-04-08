from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import argparse
from app import app
from flask import Flask, render_template, url_for, request, session, flash, redirect

__version__ = '0.0.0'
__author__ = 'Aaron Ma'

@app.route('/')
def route():
    return redirect('/index')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about/about.html')

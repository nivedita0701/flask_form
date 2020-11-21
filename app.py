from flask import Flask, render_template, Markup, request, redirect
from config import col, col_results
import requests
from form import myForm
from flask_static_compress import FlaskStaticCompress
from currenttime import yourtime, prettytime
import logging

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'OPTIONS'])
def home():
    """Landing page."""
    recent_searches = list(col_results)
    return render_template('contact.html', form=myForm(), recents=recent_searches)
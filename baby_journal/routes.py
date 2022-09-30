"""
flask routes module
v1.0
"""

# Import dependencies
from flask import render_template, request, redirect, url_for
from baby_journal import app, db
# from baby_journal.database import Category, Task

from jinja2 import TemplateNotFound
from werkzeug.security import generate_password_hash, check_password_hash

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/404")
def error():
    return "test"

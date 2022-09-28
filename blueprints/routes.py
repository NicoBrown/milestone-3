"""
flask routes module
v1.0
"""

# Import dependencies
from flask import (
    Blueprint, flash, render_template,
    redirect, request, session, url_for)
from jinja2 import TemplateNotFound
from werkzeug.security import generate_password_hash, check_password_hash
# from forms import RegistrationForm, SignInForm

from blueprints import app


@app.route("/")
def home():
    return render_template("" "home.html")

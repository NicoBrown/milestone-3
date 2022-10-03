"""
flask routes module
v1.0
"""

# Import dependencies
from flask import (Flask, render_template, request,
                   redirect, url_for, flash, session)
from baby_journal import app, db
from baby_journal.database import Children, Records

from jinja2 import TemplateNotFound
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login_form.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register_form.html")


@app.route("/logout")
def logout():
    """remove user from session cookie"""
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

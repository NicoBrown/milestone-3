"""
User Auth module
v1.0
"""

# Import dependencies
from flask import (
    Blueprint, flash, render_template,
    redirect, request, session, url_for)
from jinja2 import TemplateNotFound
from werkzeug.security import generate_password_hash, check_password_hash
# from forms import RegistrationForm, SignInForm

# Initiate Blueprint
auth = Blueprint(
    "auth", __name__,
    static_folder="static", template_folder="templates")

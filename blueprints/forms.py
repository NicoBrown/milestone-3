"""
Forms module
v1.0
"""

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


# Initiate Blueprint
forms = Blueprint(
    "forms", __name__,
    static_folder="../static", template_folder="./templates")

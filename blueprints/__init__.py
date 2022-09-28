"""
init file
v1.0
"""
import os
from flask import (Flask, flash, render_template, url_for, Blueprint)
from blueprints.database import connection

#import blueprints
from blueprints.auth import auth
from blueprints.forms import forms

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

# register blueprints
app.register_blueprint(auth)
app.register_blueprint(forms)

cursor = connection.cursor()
# Print PostgreSQL details
print("PostgreSQL server information")
print(connection.get_dsn_parameters(), "\n")

from blueprints import routes  # noqa

"""
Database Python module
"""
# Import dependencies
import os
import psycopg2
if os.path.exists("env.py"):
    import env  

from baby_journal import db


user = os.environ.get("USER")
password = os.environ.get("password")
host = os.environ.get("host")
port = os.environ.get("port")
database = os.environ.get("dbname")


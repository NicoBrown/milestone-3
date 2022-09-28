"""
Database Python module
"""
# Import dependencies
import os
import psycopg2
if os.path.exists("env.py"):
    import env

user = os.environ.get("user")
password = os.environ.get("password")
host = os.environ.get("host")
port = os.environ.get("port")
database = os.environ.get("dbname")

# Connect to an existing database
connection = psycopg2.connect(
    user=user,
    password=password,
    host=host,
    port=port,
    database=database)

cursor = connection.cursor()

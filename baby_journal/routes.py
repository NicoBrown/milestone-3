"""
flask routes module
v1.0
"""

# Import dependencies
from flask import (Flask, render_template, request,
                   redirect, url_for, flash, session)
from baby_journal import app, db
from baby_journal.database import Children, Records, User
from flask_sqlalchemy import SQLAlchemy
from datetime import date


from jinja2 import TemplateNotFound
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if Username exists in db
        existing_user = User.query.filter_by(
            email=request.form.get("email").lower()).first()

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user.password, request.form.get("password")):
                flash("Welcome")
                session["email"] = request.form.get("email").lower()
                return redirect(url_for("children_home"))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login_form.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = User.query.filter_by(
            email=request.form.get("email").lower()).first()

        if existing_user:
            flash("email address already exists")
            return redirect(url_for("login"))

        user_record = User(
            email=request.form.get("email").lower(),
            password=generate_password_hash(request.form.get("password")),
            address=request.form.get("address").lower(),
            phone_number=request.form.get("phone").lower(),
        )

        db.session.add(user_record)
        db.session.commit()

        # put the new user into 'session' cookie
        session["email"] = request.form.get("email").lower()
        flash("Registration Successful!")
        return redirect(url_for("children_home"))

    return render_template("register_form.html")


@ app.route("/children_home", methods=["GET", "POST"])
def children_home():
    if "email" in session:

        useremail = session.get("email")

        user = User.query.filter_by(
            email=useremail).first()

        childrenlists = Children.query.filter_by(
            parent_id=user.id).all()

       # return list of children
        if (childrenlists):
            return render_template("children_home.html", children=childrenlists)
        else:
            return render_template("children_home.html")

    return redirect(url_for("home"))


@ app.route("/child_home/<int:child_id>", methods=["GET", "POST"])
def child_home(child_id):

    child_records = Records.query.filter_by(
        child_id=child_id).order_by(Records.date_time.desc()).all()

    child_record = Children.query.filter(
        Children.id == child_id).first()

    return render_template("child_home.html", records=child_records, child=child_record)


@ app.route("/add_record/<int:child_id>", methods=["GET", "POST"])
def add_record(child_id):
    if request.method == "POST":

        record = Records(
            title=request.form.get("title").lower(),
            activity=request.form.get("activity"),
            duration=request.form.get("duration"),
            quantity=request.form.get("quantity"),
            units=request.form.get("units"),
            location=request.form.get("location"),
            notes=request.form.get("notes"),
            date_time=date.today(),
            child_id=child_id,
        )

        db.session.add(record)
        db.session.commit()

        flash("Record Added Successfully!")
        return redirect(url_for("child_home", child_id=child_id))

    return render_template("add_record.html", child_id=child_id)


@ app.route("/edit_record/<int:record_id>", methods=["GET", "POST"])
def edit_record(record_id):
    if request.method == "POST":

        record = Records.query.filter_by(id=record_id).first()

        record.title = request.form.get("title")
        record.activity = request.form.get("activity")
        record.duration = request.form.get("duration")
        record.quantity = request.form.get("quantity")
        record.units = request.form.get("units")
        record.location = request.form.get("location")
        record.notes = request.form.get("notes")

        db.session.commit()
        flash("Record edited Successfully!")
        return redirect(url_for("child_home", child_id=record.child_id))

    record = Records.query.filter_by(
        id=record_id).first()

    return render_template("edit_record.html", record=record, child_id=record.child_id)


@ app.route("/add_child", methods=["GET", "POST"])
def add_child():
    if request.method == "POST":
        # check if username already exists in db
        existing_child = db.session.query(Children.first_name).filter(
            Children.first_name == request.form.get("first_name").lower()).all()

        if existing_child:
            flash("child name already exists")
            return redirect(url_for("add_child"))

        useremail = session.get("email")

        user = User.query.filter_by(
            email=useremail).first()

        child_record = Children(
            first_name=request.form.get("first_name").lower(),
            last_name=request.form.get("last_name").lower(),
            allergies=request.form.get("allergies").lower(),
            date_of_birth=request.form.get("date_of_birth").lower(),
            parent_id=user.id,
        )

        db.session.add(child_record)
        db.session.commit()

        flash("child Added Successfully!")
        return redirect(url_for("children_home"))

    return render_template("add_child.html")


@ app.route("/children_home/<int:child_id>", methods=["GET", "POST"])
def delete_child(child_id):

    child_record = Children.query.filter(
        Children.id == child_id).first()

    db.session.delete(child_record)

    db.session.commit()

    flash("child removed Successfully!")
    return redirect(url_for("children_home"))


@ app.route("/logout")
def logout():
    """remove user from session cookie"""
    flash("You have been logged out")
    session.pop("email")
    return redirect(url_for("home"))

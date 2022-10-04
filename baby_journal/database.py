"""
Database Python module
"""

# Import dependencies
from baby_journal import db


class User(db.Model):
    """user database model - Returns: __repr__:self"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(255), nullable=True)

    def __str__(self):
        #     # __repr__ to represent self as a string
        return self


class Children(db.Model):
    """children database model - Returns: __repr__:self"""
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    allergies = db.Column(db.String(30), nullable=True)
    date_of_birth = db.Column(db.Date, index=True, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey(
        "user.id", ondelete="CASCADE"))

    def __str__(self):
        # __repr__ to represent self as a string
        return self


class Records(db.Model):
    """records database model - Returns: __repr__:self"""

    __tablename__ = "records"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    notes = db.Column(db.Text, nullable=True)
    duration = db.Column(db.Integer, nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    units = db.Column(db.String(30), nullable=True)
    quantity = db.Column(db.Float, nullable=True)
    location = db.Column(db.String(50), nullable=True)
    child_id = db.Column(db.Integer, db.ForeignKey(
        "children.id", ondelete="CASCADE"))

    def __str__(self):
        # __repr__ to represent self as a string
        return self

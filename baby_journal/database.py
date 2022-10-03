"""
Database Python module
"""

# Import dependencies
from baby_journal import db


class User(db.Model):
    """User database model - Returns: __repr__:self"""

    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    children = db.relationship(
        "Children", back_populates="parent_id",
        cascade="all, delete",
        passive_deletes=True
    )
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.Integer, nullable=True)
    address = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        #     # __repr__ to represent self as a string
        return self


class Children(db.Model):
    """Children database model - Returns: __repr__:self"""
    __tablename__ = "Children"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    allergies = db.Column(db.String(30), nullable=True)
    age = db.Column(db.Integer, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey(
        'User.id', ondelete="CASCADE"))

    def __repr__(self):
        # __repr__ to represent self as a string
        return self


class Records(db.Model):
    """Records database model - Returns: __repr__:self"""

    __tablename__ = "Records"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    notes = db.Column(db.Text, nullable=True)
    duration = db.Column(db.Integer, nullable=False)
    date_time = db.Column(db.Date, nullable=False)
    units = db.Column(db.String(30), nullable=True)
    quantity = db.Column(db.Float, nullable=True)
    location = db.Column(db.String(50), nullable=True)
    child_id = db.Column(db.Integer, db.ForeignKey(
        "Children.id", ondelete="CASCADE"))

    def __repr__(self):
        # __repr__ to represent self as a string
        return self

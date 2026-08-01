from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(120), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    phone = db.Column(db.String(20), unique=True)

    password = db.Column(db.String(255), nullable=False)

    role = db.Column(
        db.Enum('admin', 'fan', 'volunteer'),
        default='fan'
    )

    profile_image = db.Column(db.String(255))

    language = db.Column(db.String(30), default="English")

    is_active = db.Column(db.Boolean, default=True)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    tickets = db.relationship(
        "Ticket",
        backref="user",
        lazy=True,
        cascade="all, delete"
    )

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User {self.full_name}>"
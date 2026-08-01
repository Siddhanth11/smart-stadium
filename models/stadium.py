from database import db


class Stadium(db.Model):
    __tablename__ = "stadiums"

    id = db.Column(db.Integer, primary_key=True)

    stadium_name = db.Column(
        db.String(150),
        nullable=False
    )

    city = db.Column(db.String(100))

    state = db.Column(db.String(100))

    country = db.Column(db.String(100))

    address = db.Column(db.String(255))

    capacity = db.Column(db.Integer)

    latitude = db.Column(db.Float)

    longitude = db.Column(db.Float)

    total_gates = db.Column(db.Integer)

    total_parking_slots = db.Column(db.Integer)

    emergency_exit_count = db.Column(db.Integer)

    wifi_available = db.Column(
        db.Boolean,
        default=True
    )

    food_courts = db.Column(db.Integer)

    washrooms = db.Column(db.Integer)

    medical_rooms = db.Column(db.Integer)

    created_at = db.Column(
        db.DateTime,
        default=db.func.now()
    )

    matches = db.relationship(
        "Match",
        backref="stadium",
        lazy=True,
        cascade="all, delete"
    )

    def __repr__(self):
        return f"<Stadium {self.stadium_name}>"
from database import db
from datetime import datetime


class Analytics(db.Model):
    __tablename__ = "analytics"

    id = db.Column(db.Integer, primary_key=True)

    match_id = db.Column(
        db.Integer,
        db.ForeignKey("matches.id"),
        nullable=False
    )

    total_attendance = db.Column(
        db.Integer,
        default=0
    )

    predicted_attendance = db.Column(
        db.Integer,
        default=0
    )

    crowd_density = db.Column(db.Float)

    parking_usage = db.Column(db.Float)

    ticket_sales = db.Column(db.Integer)

    food_sales = db.Column(db.Float)

    merchandise_sales = db.Column(db.Float)

    average_wait_time = db.Column(db.Float)

    energy_consumption = db.Column(db.Float)

    water_consumption = db.Column(db.Float)

    waste_generated = db.Column(db.Float)

    sustainability_score = db.Column(db.Float)

    ai_summary = db.Column(db.Text)

    generated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    match = db.relationship(
        "Match",
        backref=db.backref(
            "analytics",
            uselist=False
        )
    )

    def __repr__(self):
        return f"<Analytics Match {self.match_id}>"
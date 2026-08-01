from database import db
from datetime import datetime


class Match(db.Model):
    __tablename__ = "matches"

    id = db.Column(db.Integer, primary_key=True)

    team1_id = db.Column(
        db.Integer,
        db.ForeignKey("teams.id"),
        nullable=False
    )

    team2_id = db.Column(
        db.Integer,
        db.ForeignKey("teams.id"),
        nullable=False
    )

    stadium_id = db.Column(
        db.Integer,
        db.ForeignKey("stadiums.id"),
        nullable=False
    )

    match_date = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    tournament = db.Column(db.String(100))

    match_type = db.Column(db.String(50))

    status = db.Column(
        db.Enum("Scheduled", "Live", "Completed", "Cancelled"),
        default="Scheduled"
    )

    team1_score = db.Column(db.String(50))

    team2_score = db.Column(db.String(50))

    winner = db.Column(db.String(100))

    toss_winner = db.Column(db.String(100))

    toss_decision = db.Column(db.String(50))

    weather = db.Column(db.String(100))

    attendance = db.Column(db.Integer)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    tickets = db.relationship(
        "Ticket",
        backref="match",
        lazy=True,
        cascade="all, delete"
    )

    def __repr__(self):
        return f"<Match {self.id}>"
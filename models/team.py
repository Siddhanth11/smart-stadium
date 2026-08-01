from database import db


class Team(db.Model):
    __tablename__ = "teams"

    id = db.Column(db.Integer, primary_key=True)

    team_name = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )

    city = db.Column(db.String(100))

    coach = db.Column(db.String(100))

    captain = db.Column(db.String(100))

    logo = db.Column(db.String(255))

    founded_year = db.Column(db.Integer)

    stadium_name = db.Column(db.String(100))

    championships = db.Column(
        db.Integer,
        default=0
    )

    players = db.relationship(
        "Player",
        backref="team",
        lazy=True,
        cascade="all, delete"
    )

    home_matches = db.relationship(
        "Match",
        foreign_keys="Match.team1_id",
        lazy=True
    )

    away_matches = db.relationship(
        "Match",
        foreign_keys="Match.team2_id",
        lazy=True
    )

    def __repr__(self):
        return f"<Team {self.team_name}>"
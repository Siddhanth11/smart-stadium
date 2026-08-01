from database import db


class Player(db.Model):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(100),
        nullable=False
    )

    age = db.Column(db.Integer)

    jersey_number = db.Column(db.Integer)

    position = db.Column(db.String(50))

    nationality = db.Column(db.String(80))

    batting_style = db.Column(db.String(50))

    bowling_style = db.Column(db.String(50))

    role = db.Column(db.String(50))

    image = db.Column(db.String(255))

    matches_played = db.Column(
        db.Integer,
        default=0
    )

    runs = db.Column(
        db.Integer,
        default=0
    )

    wickets = db.Column(
        db.Integer,
        default=0
    )

    catches = db.Column(
        db.Integer,
        default=0
    )

    strike_rate = db.Column(db.Float)

    economy = db.Column(db.Float)

    team_id = db.Column(
        db.Integer,
        db.ForeignKey("teams.id"),
        nullable=False
    )

    def __repr__(self):
        return f"<Player {self.name}>"
from flask import Flask, render_template, request, redirect, url_for, flash
from database import mysql
from config import Config
from routes.auth import auth_bp
app = Flask(__name__)

app.config.from_object(Config)
app.secret_key = "your_secret_key"
app.register_blueprint(auth_bp)

mysql.init_app(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():

    cur = mysql.connection.cursor()

    cur.execute("SELECT COUNT(*) FROM teams")
    teams = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM players")
    players = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM matches")
    matches = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM tickets")
    tickets = cur.fetchone()[0]

    cur.close()

    return render_template(
        "dashboard.html",
        teams=teams,
        players=players,
        matches=matches,
        tickets=tickets
    )


@app.route("/teams")
def teams():

    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM teams")

    data = cur.fetchall()

    cur.close()

    return render_template("teams.html", teams=data)


@app.route("/add_team", methods=["POST"])
def add_team():

    name = request.form["team_name"]

    coach = request.form["coach"]

    cur = mysql.connection.cursor()

    cur.execute(
        "INSERT INTO teams(team_name,coach) VALUES(%s,%s)",
        (name, coach)
    )

    mysql.connection.commit()

    cur.close()

    flash("Team Added Successfully")

    return redirect(url_for("teams"))


@app.route("/matches")
def matches():

    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM matches")

    data = cur.fetchall()

    cur.close()

    return render_template("matches.html", matches=data)


@app.route("/tickets")
def tickets():

    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM tickets")

    data = cur.fetchall()

    cur.close()

    return render_template("tickets.html", tickets=data)


@app.route("/analytics")
def analytics():

    cur = mysql.connection.cursor()

    cur.execute("SELECT COUNT(*) FROM tickets")
    tickets = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM matches")
    matches = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM teams")
    teams = cur.fetchone()[0]

    cur.close()

    return render_template(
        "analytics.html",
        tickets=tickets,
        matches=matches,
        teams=teams
    )


if __name__ == "__main__":
    app.run(debug=True)
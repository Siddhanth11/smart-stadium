from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from database import db
from models.user import User

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        full_name = request.form.get("full_name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password = request.form.get("password")
        confirm = request.form.get("confirm_password")
        role = request.form.get("role", "fan")

        if not full_name or not email or not password:
            flash("Please fill all required fields.", "danger")
            return redirect(url_for("auth.register"))

        if password != confirm:
            flash("Passwords do not match.", "danger")
            return redirect(url_for("auth.register"))

        existing = User.query.filter_by(email=email).first()

        if existing:
            flash("Email already registered.", "warning")
            return redirect(url_for("auth.register"))

        user = User(
            full_name=full_name,
            email=email,
            phone=phone,
            role=role
        )

        user.password = generate_password_hash(password)

        db.session.add(user)
        db.session.commit()

        flash("Registration Successful.", "success")

        return redirect(url_for("auth.login"))

    return render_template("register.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user is None:
            flash("User not found.", "danger")
            return redirect(url_for("auth.login"))

        if not check_password_hash(user.password, password):
            flash("Invalid Password.", "danger")
            return redirect(url_for("auth.login"))

        session["user_id"] = user.id
        session["user_name"] = user.full_name
        session["role"] = user.role

        flash("Login Successful.", "success")

        if user.role == "admin":
            return redirect(url_for("admin.dashboard"))

        if user.role == "volunteer":
            return redirect(url_for("volunteer.dashboard"))

        return redirect(url_for("fan.dashboard"))

    return render_template("login.html")

@auth_bp.route("/logout")
def logout():

    session.clear()

    flash("Logged out successfully.", "info")

    return redirect(url_for("auth.login"))

from functools import wraps


def login_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):

        if "user_id" not in session:

            flash("Please login first.", "warning")

            return redirect(url_for("auth.login"))

        return f(*args, **kwargs)

    return decorated_function

def admin_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):

        if "role" not in session:

            flash("Unauthorized.", "danger")
            return redirect(url_for("auth.login"))

        if session["role"] != "admin":

            flash("Admin Access Only.", "danger")
            return redirect(url_for("fan.dashboard"))

        return f(*args, **kwargs)

    return decorated_function
def admin_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):

        if "role" not in session:

            flash("Unauthorized.", "danger")
            return redirect(url_for("auth.login"))

        if session["role"] != "admin":

            flash("Admin Access Only.", "danger")
            return redirect(url_for("fan.dashboard"))

        return f(*args, **kwargs)

    return decorated_function
def volunteer_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):

        if "role" not in session:

            return redirect(url_for("auth.login"))

        if session["role"] != "volunteer":

            flash("Volunteer Access Only.", "danger")

            return redirect(url_for("fan.dashboard"))

        return f(*args, **kwargs)

    return decorated_function
def fan_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):

        if "role" not in session:

            return redirect(url_for("auth.login"))

        if session["role"] != "fan":

            flash("Access Denied.", "danger")

            if session["role"] == "admin":
                return redirect(url_for("admin.dashboard"))

            if session["role"] == "volunteer":
                return redirect(url_for("volunteer.dashboard"))

        return f(*args, **kwargs)

    return decorated_function
def get_current_user():
    """
    Returns the currently logged-in user.
    """

    if "user_id" not in session:
        return None

    return User.query.get(session["user_id"])
@auth_bp.route("/profile")
@login_required
def profile():

    user = get_current_user()

    if not user:
        flash("User not found.", "danger")
        return redirect(url_for("auth.logout"))

    return render_template(
        "profile.html",
        user=user
    )
@auth_bp.route("/update-profile", methods=["GET", "POST"])
@login_required
def update_profile():

    user = get_current_user()

    if not user:
        flash("User not found.", "danger")
        return redirect(url_for("auth.logout"))

    if request.method == "POST":

        full_name = request.form.get("full_name")
        phone = request.form.get("phone")
        language = request.form.get("language")

        if not full_name:
            flash("Full name is required.", "danger")
            return redirect(url_for("auth.update_profile"))

        user.full_name = full_name
        user.phone = phone
        user.language = language

        db.session.commit()

        session["user_name"] = user.full_name

        flash("Profile updated successfully.", "success")

        return redirect(url_for("auth.profile"))

    return render_template(
        "update_profile.html",
        user=user
    )
@auth_bp.route("/delete-account", methods=["POST"])
@login_required
def delete_account():

    user = get_current_user()

    if not user:
        flash("User not found.", "danger")
        return redirect(url_for("auth.logout"))

    db.session.delete(user)
    db.session.commit()

    session.clear()

    flash("Your account has been deleted.", "info")

    return redirect(url_for("auth.register"))
@auth_bp.route("/dashboard")
@login_required
def dashboard():

    role = session.get("role")

    if role == "admin":
        return redirect(url_for("admin.dashboard"))

    if role == "volunteer":
        return redirect(url_for("volunteer.dashboard"))

    return redirect(url_for("fan.dashboard"))

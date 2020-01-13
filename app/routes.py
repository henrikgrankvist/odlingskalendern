from flask import render_template, request, url_for, redirect, flash
from app import app, db
from app.forms import LoginForm, RegisterForm
from app.models import User
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Hem')

@app.route('/login', methods=["GET", "POST"])
def login():

    # if the user is already logged in. Redirect them away
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = LoginForm()

    if form.validate_on_submit(): # validate_on_submit is needed to validate the output according to forms.py
        user = User.query.filter_by(username=form.username.data).first()

        # user is None if it was not found in the database
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))

        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get("next")

        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("index")

        # Redirect the user to the page they got from.
        return redirect(next_page)

    return render_template("login.html", title='Logga in', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route('/register', methods=["GET", "POST"])
def register():

    # if the user is already logged in. Redirect them away
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = RegisterForm()

    if form.validate_on_submit():
        user = User(username=form.username.data)

        # Check if username (email) is already registered
        if User.query.filter_by(username=form.username.data).first() is not None:
            flash("Epost-adressen är redan registerad.")
            return redirect(url_for("register"))

        user.set_password(form.password.data)
        current_user.joined_date = datetime.utcnow() # Set the time when the user registered
        db.session.add(user)
        db.session.commit()

        flash('Grattis, du är nu en registerad medlem!')
        return redirect(url_for('login'))

    return render_template("register.html", title='Registera ny medlem', form=form)

@app.route('/page')
@login_required
def page():
    return render_template("page.html", title='Test page')

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    users = User.query.all()
    return render_template("user.html", title='User page', user=user, users=users)

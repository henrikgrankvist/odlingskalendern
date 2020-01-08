from flask import render_template, request, url_for, redirect, flash
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Hem')

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()

    #if request.method == "POST":
    if form.validate_on_submit(): # validate_on_submit is needed to validate the output according to forms.py
        flash('Inloggningen misslyckades')
        return redirect(url_for("login"))

    return render_template("login.html", title='Logga in', form=form)

@app.route('/page')
def page():
    return render_template("page.html", title='Test page')

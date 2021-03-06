from flask import Flask
from config import Config
import os
from flask_sqlalchemy import SQLAlchemy # pip install flask-sqlalchemy
from flask_login import LoginManager # pip install flask-login
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = "login" # if a page requires login to be viewed, redirect them to the login page
migrate = Migrate(app, db)


from app import routes, models

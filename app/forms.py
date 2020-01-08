from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, InputRequired

class LoginForm(FlaskForm):
    username = StringField('Epost', [Email(message='Not a valid email address.'), DataRequired()], render_kw={"placeholder": "user@example.com"})
    #username = StringField('Epost')
    password = PasswordField('Lösenord', [DataRequired(message="Ange ditt lösenord")], render_kw={"placeholder": "Lösenord"})
    #password = PasswordField('Lösenord')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Logga in')

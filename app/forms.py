from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, InputRequired, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Epost', validators=[Email(message='Du har angett en ogiltig epost adress'), DataRequired()], render_kw={"placeholder": "user@example.com"})
    password = PasswordField('Lösenord', validators=[DataRequired(message="Ange ett lösenord")], render_kw={"placeholder": "Lösenord"})
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Logga in')

class RegisterForm(FlaskForm):
    username = StringField('Epost', validators=[Email(message='Du har angett en ogiltig epost adress'), DataRequired()], render_kw={"placeholder": "user@example.com"})
    password = PasswordField('Lösenord', validators=[DataRequired(message="Ange ett lösenord")], render_kw={"placeholder": "Lösenord"})
    password2 = PasswordField('Repetera Lösenord', validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Repetera lösenord"})
    submit = SubmitField('Registera')

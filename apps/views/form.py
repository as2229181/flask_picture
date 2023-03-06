from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,validators
from wtforms.validators import DataRequired

class NewUserForm(FlaskForm):
    username=StringField("username",validators=[DataRequired()])
    email=StringField("email",validators=[DataRequired()])
    password=PasswordField("Set your password",[validators.DataRequired(message='You should enter password!!!'),validators.EqualTo('confirm', message='Passwords must match')
    ])
    Submit=SubmitField("Submit")
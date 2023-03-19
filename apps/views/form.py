from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,validators,TextAreaField
from wtforms.validators import DataRequired,EqualTo
from wtforms.widgets import TextArea
from flask_ckeditor import CKEditorField

class NewUserForm(FlaskForm):
    name=StringField("Your name",validators=[DataRequired()])
    username=StringField("username",validators=[DataRequired()])
    email=StringField("email",validators=[DataRequired()])
    password=PasswordField("Set your password",validators=[DataRequired(message='You should enter password!!!'),EqualTo('password2', message='Passwords must match')])
    About_me=TextAreaField("About you",validators=[DataRequired()])
    password2=PasswordField("Conform your password",validators=[DataRequired(message='You should enter password!!!')])

    Submit=SubmitField("Submit")

class PasswordForm(FlaskForm):
    email=StringField("What's your email",validators=[DataRequired()])
    password=PasswordField("What's your password",validators=[DataRequired()])
    Submit=SubmitField("Submit")

class PostForm(FlaskForm):
    title=StringField("Title",validators=[DataRequired(message="Could not be blanked yo!")])
    #content=StringField("Content",validators=[DataRequired(message="Could not be blanked yo!")],widget=TextArea())
    content=CKEditorField("Content",validators=[DataRequired(message="Could not be blanked yo!")],widget=TextArea())
    # author=StringField("Author",validators=[DataRequired(message="Could not be blanked yo!")])
    slug=StringField("Slug",validators=[DataRequired(message="Could not be blanked yo!")])
    Submit=SubmitField("Submit")
class LoginForm(FlaskForm):
    username=StringField("Username",validators=[DataRequired()])
    password=PasswordField("Password",validators=[DataRequired()])
    Submit=SubmitField("Submit")
class SearchForm(FlaskForm):
    searched=StringField("Searched",validators=[DataRequired()])
    Submit=SubmitField("Submit")
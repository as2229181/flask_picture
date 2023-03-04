from flask import render_template,request
from apps.models.user import User,create_

class views:
    
    def index():
        stuff="This is my <strong>first</strong> web"
        return render_template("index.html",stuff=stuff) 
    def users(username):
        return render_template("user/users.html",username=username)
    def new():
        return render_template("user/new.html")
    def create():
        username = request.form["username"]
        email=request.form["email"]
        password=request.form["password"]
        create_(username,email,password)
        return "create success"

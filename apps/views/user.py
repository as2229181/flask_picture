from flask import render_template,request

class views:
    def index():
        return render_template("user/index.html")
    def new():
        return render_template("user/new.html")
    def create(self):
        username = request.form["username"]
        email=request.form["email"]
        password=request.formp["password"]
        return "create.{}".format(username)

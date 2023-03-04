from apps import app
from apps.views.user import views
from flask import render_template

@app.route("/",methods=["GET"])
def index():
    return views.index()
@app.route("/home/<username>",methods=["GET"])
def users(username):
    return views.users(username)

@app.route("/new",methods=["GET"])
def new():
    return views.new()
@app.route("/create",methods=["POST"] )
def create():
    return views.create()



@app.errorhandler(404)
def page_not_found(e):
    return render_template("error/404.html"),404


app.run(debug=True)

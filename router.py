from apps import app

from apps.views.user import views
from flask import render_template,flash,request

@app.route("/",methods=["GET"])
def index():
    return views.index()
@app.route("/user/<username>",methods=["GET"])
def users(username):
    return views.users(username)

@app.route("/new",methods=["GET"])
def new():
    return views.new()

@app.route("/create",methods=["GET","POST"] )
def create():
    return views.create()


@app.route("/update/<int:id>",methods=["GET","POST"])
def update(id):
    return views.Update(id)

@app.route("/delete/<int:id>",methods=["GET","POST"])
def delete(id):
    return views.Delete(id)

    
        



@app.errorhandler(404)
def page_not_found(e):
    return render_template("error/404.html"),404

if __name__ == "__main__":
    app.run(debug=True)

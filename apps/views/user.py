from flask import render_template,request,flash,redirect,url_for
from apps.models.user import User,create_,update_,delete_
from apps.views.form import NewUserForm
from flask_sqlalchemy import query

class views:
    
    def index():
        stuff="This is my <strong>first</strong> web"
        return render_template("index.html",stuff=stuff) 
    def users(username):
        return render_template("user/users.html",username=username)
    def new():
        form=NewUserForm()
        return render_template("user/new.html",form=form)
           
    def create():
        username = request.form["username"]
        email=request.form["email"]
        password=request.form["password"]
        user=User.query.filter_by(email=email).first()
        our_users=User.query.order_by(User.id)
        form=NewUserForm()
        if user is None:
            create_(username,email,password)
            flash("Create successed")
            return render_template("user/new.html",username=username,form=form,our_users=our_users)
        else:
            form=NewUserForm()
            flash("email was been registed")
            return render_template("user/new.html",form=form,our_users=our_users)
    def Update(id):
        form=NewUserForm()
        our_users=User.query.order_by(User.id)
        id=id
        if request.method=="POST":
            username=request.form["username"]
            email=request.form["email"]
            password=request.form["password"]
            try:
                update_(id,username,email,password)
                flash("Account update successfully")
                return render_template("/user/update.html",form=form,our_users=our_users)
            except:
                flash("Error!Please try again!")
                return render_template("/user/update.html",form=form,our_users=our_users)
        else:
            return render_template("/user/update.html",form=form,our_users=our_users)
    def Delete(id):
        our_users=User.query.order_by(User.id)
        form=NewUserForm()
        try:
            delete_(id)
            flash("User delete successfully!")
            return render_template("user/new.html",form=form,our_users=our_users)
        except:
            flash("Please try again")
            return render_template("user/new.html",form=form,our_users=our_users)


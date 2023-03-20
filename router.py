from apps import app
from apps.views.form import PasswordForm,PostForm,SearchForm
from apps.views.user import views
from flask import render_template,flash,request,redirect,url_for
from apps.models.user import User,check_password_hash,create_post_
from flask_login import login_required,logout_user,current_user
from apps.models.user import Posts




@app.route("/login",methods=["GET","POST"])
def login():
    return views.Login()
 
#pass stuff To Navbar
@app.context_processor #讓某個變數可以套到所有的template去
def base():
    form=SearchForm()
    return dict(form=form)


#creat search function
@app.route("/search",methods=["POST"])
def search():
    form=SearchForm()
    posts=Posts.query
    if form.validate_on_submit():
        #get data form  subnitted form
        post_searched=form.searched.data
        #query database
        posts=posts.filter(Posts.content.like('%'+post_searched+'%'))
        posts=posts.order_by(Posts.title).all()
        return render_template("user/search.html",form=form,searched=post_searched,posts=posts)
@app.route("/logout",methods=["GET","POST"])
@login_required
def logout():
    logout_user()
    flash("You have been logout!")
    return redirect(url_for("login"))
@app.route("/dashboard",methods=["GET","POST"])
@login_required
def dashboard():
    return views.Dashboard()

@app.route("/",methods=["GET"])
def index():
    return views.index()
@app.route("/user/<username>",methods=["GET"])
def users(username):
    return views.users(username)

@app.route("/new",methods=["GET"])
def new():
    if current_user.is_active:
        return redirect(url_for("users",username=current_user.username))
    else:
        return views.new()

@app.route("/create",methods=["GET","POST"] )
def create():
    return views.create()

@login_required
@app.route("/update/<int:id>",methods=["GET","POST"])
def update(id):
    return views.Update(id)
@login_required
@app.route("/delete/<int:id>",methods=["GET","POST"])
def delete(id):
    return views.Delete(id)

@app.route("/test_pw",methods=["GET","POST"])
def test_pw():
    email= None
    password= None
    pw_to_check=None
    passed=None
    About_me=None
    
    form=PasswordForm()
    if form.validate_on_submit():
        email=form.email.data
        password=form.password.data
        form.email.data=''
        form.password.data=''
        form.About_me.data=''
        pw_to_check= User.query.filter_by(email=email).first()
        passed=check_password_hash(pw_to_check.password_hash,password)
    return render_template(
        "user/test.html",
        email=email,
        password=password,
        form=form,
        passed=passed,
        About_me=About_me,
        pw_to_check=pw_to_check)

@app.route("/add_post",methods=["GET","POST"])
@login_required
def add_post():
    form=PostForm()
    if form.validate_on_submit():
        poster= current_user.id
        title=form.title.data
        content=form.content.data
        # author=form.author.data
        slug=form.slug.data
        create_post_(title,content,poster,slug)
        form.content.data=""
        form.title.data=""
        # form.author.data=""
        form.slug.data=""
        flash("POST create successfully")
    return render_template("user/add-post.html",form=form)

@app.route("/show_post",methods=["GET"])
def show_post():
    return views.Show_post()

@app.route("/show_post/<int:id>",methods=["GET"])
def show_post_id(id):    
    return views.Show_post_id(id)

@app.route("/post/edit/<int:id>",methods=["GET","POST"])
@login_required
def edit_post_id(id):
    return views.Edit_post_id(id)

@app.route("/post/delete/<int:id>",methods=["GET","POST"])
@login_required
def delete_post_id(id):
    return views.Delete_post_id(id)


@app.route("/photo_uploads",methods=["GET","POST"])
def upload_photos():
    return views.Upload_photo()

@app.route("/admin")
@login_required
def admin():# 只能給superuser使用的頁面 去管理使用者?
    id==current_user.id
    if id == 1:
        return render_template("user/admin.html")
    else:
        flash("Sorry you must be admin to access the admin page ")
        return redirect(url_for("dashboard"))






    
        



@app.errorhandler(404)
def page_not_found(e):
    return render_template("error/404.html"),404
@app.errorhandler(500)
def page_not_found(e):
    return render_template("error/500.html"),500

if __name__ == "__main__":
    app.run(debug=True)

from flask import render_template,request,flash,redirect,url_for
from apps.models.user import User,create_,update_,delete_,create_post_,show_post_,show_post_id,Posts,edit_post_id,check_password_hash,Photos
from apps.views.form import NewUserForm,PostForm,LoginForm,PhotosForm
from flask_sqlalchemy import query
from .. import db,login_manager,app,allowed_file
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_login import login_user,LoginManager,login_required,logout_user,current_user
from werkzeug.utils import secure_filename
import os,uuid

class views:
    
    def index():
        stuff="This is my <strong>first</strong> web"
        return render_template("index.html",stuff=stuff)
    def Login():
        form=LoginForm()
        if form.validate_on_submit():
            username=form.username.data
            password=form.password.data
            user1=User.query.filter_by(username=username).first()
            hash_password=user1.password_hash
            if user1 is not None:
                if check_password_hash(hash_password,password):
                    login_user(user1)
                    flash("Login successfully!!!!")
                    return redirect(url_for("dashboard"))
                else:
                    flash("Your password is wrong, please try again!!!!")
            else:
                flash("User doesn't exist!!!!")
        return render_template("user/login.html",form=form)
    def Dashboard():
        
        return render_template("user/dashboard.html")
    def users(username):
        return render_template("user/users.html",username=username)
    def new():
        form=NewUserForm()
        return render_template("user/new.html",form=form)
           
    def create():
        name = request.form["name"]
        username = request.form["username"]
        email=request.form["email"]
        password=request.form["password"]
        About_me=request.form["About_me"]
        user=User.query.filter_by(email=email).first()
        our_users=User.query.order_by(User.id)
        form=NewUserForm()
        if user is None:
            create_(name,username,email,password,About_me=About_me)
            flash("Create successed")
            return render_template("user/new.html",username=username,form=form,our_users=our_users)
        else:
            form=NewUserForm()
            flash("email was been registed")
            return render_template("user/new.html",form=form,our_users=our_users)
    def Update(id):
        form=NewUserForm()
        our_users=User.query.get_or_404(id)
        if request.method=="POST":
            name=form.name.data
            username=form.username.data
            email=form.email.data
            About_me=form.About_me.data
            try:
                update_(id,name,username,email,About_me)
                flash("Account update successfully")
                return render_template("/user/update.html",id=id,form=form,our_users=our_users)
            except:
                flash("Error!Please try again!")
                return render_template("/user/update.html",id=id,form=form,our_users=our_users)
        else:
            return render_template("/user/update.html",id=id,form=form,our_users=our_users)
    def Delete(id):
        our_users=User.query.order_by(User.id)
        form=NewUserForm()
        if id == current_user.id:
            try:
                delete_(id)
                flash("User delete successfully!")
                return render_template("user/new.html",form=form,our_users=our_users)
            except:
                flash("Please try again")
                return render_template("user/new.html",form=form,our_users=our_users)
        else:
            flash("Sorry you can't delete that user!!")
            return redirect(url_for("dashboard"))
    def Show_post():
        posts=show_post_()
        return render_template("user/show-post.html",posts=posts) 
    def Show_post_id(id):
        post_id=show_post_id(id)
        return render_template("user/show_post_id.html",post_id=post_id)
    def Edit_post_id(id):
        post=Posts.query.get_or_404(id)
        form=PostForm()
        if form.validate_on_submit():
            post.title=form.title.data
            # post.author=form.author.data
            post.content=form.content.data
            post.slug=form.slug.data
            edit_post_id(post)
            flash("Update successfully!!")
            return redirect(url_for("show_post_id",id=post.id))
        if current_user.id == post.poster.id:
            form.title.data=post.title
        # form.author.data=post.author
            form.content.data=post.content
            form.slug.data=post.slug
            return render_template("user/edit_post.html",form=form)
        else:
            flash("You're not the author of this article!!!!")
            posts=show_post_()
            return render_template("user/show-post.html",posts=posts)
    def Delete_post_id(id):
        post_to_delete=Posts.query.get_or_404(id)
        id=current_user.id
        if id == post_to_delete.id:
            try:
                db.session.delete(post_to_delete)
                db.session.commit()
                flash("Post delete successfully")
                posts=Posts.query.order_by(Posts.date_posted).all()
                return render_template("user/show-post.html",posts=posts)
            except:
                flash("Somthing wrong with delete post")
                posts=Posts.query.order_by(Posts.date_posted).all()
                return render_template("user/show-post.html",posts=posts)
        else:
            flash("You can't delete the post,you are not the author!!!!!")
            posts=Posts.query.order_by(Posts.date_posted).all()
            return render_template("user/show-post.html",posts=posts)
    # def Upload_photo():
    #     upload_photos=Photos.query.order_by(Photos.id) 
    #     form=PhotosForm()
    #     if form.validate_on_submit():
    #         Name=form.Name.data
    #         Description=form.Description.data
    #         Filename=images.save(form.Photo.data)
    #         Image_path=images.url(Filename)
    #         photo=Photos(Name=Name,Description=Description,Filename=Filename,Image_path=Image_path)
    #         db.session.add(photo)
    #         db.session.commit()
    #         flash("Upload successfully!!!!")
    #         return redirect(url_for("dashboard"))
           
    #     return render_template("user/upload_image.html",form=form,upload_photos=upload_photos)     
        
    def Upload_photo():
        form=PhotosForm()
        if form.validate_on_submit():
            Name=form.Name.data
            photo=form.Photo.data
            Description=form.Description.data
            if allowed_file(photo.filename):
                photoer= current_user.id
                Filename=str(uuid.uuid4())+secure_filename(photo.filename) #secure_filename只能將當按名的特殊符號去除
                photo.save(os.path.join(app.config['UPLOAD_FOLDER'],Filename))
                photo=Photos(Name=Name,Description=Description,Filename=Filename,photoer_id=photoer)
                db.session.add(photo)
                db.session.commit()
                flash('Photo upload successfully!!!')
                Image_path=url_for('view_photo',photo_id=photo.id)
                return redirect(url_for("view_photo"))
        return render_template('user/upload_image.html',form=form)
    def Delete_photo_id(id):
        photo_to_delete=Photos.query.get_or_404(id)
        if current_user.id==photo_to_delete.photoer.id:
            try:
                filename=photo_to_delete.Filename
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'],filename))
                db.session.delete(photo_to_delete)
                db.session.commit()
                flash("Photo delete successfully!!")
                photos=Photos.query.order_by(Photos.id).all()
                return render_template('user/show_photos.html',photos=photos)
            except Exception as e:
                print(e)
                flash("Somthing wrong with delete photo")
                photos=Photos.query.order_by(Photos.Upload_time).all()
                return render_template("user/show-post.html",photos=photos)
        else:
            photos=Photos.query.order_by(Photos.Upload_time).all()
            flash("You're not yhe author of this photo you can not delete photo!!!!")
            return  render_template("user/show-post.html",photos=photos)



       

            


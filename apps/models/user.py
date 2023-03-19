from .. import db,login_manager
from sqlalchemy import desc
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(20),nullable=False)#如果是新增的column 要設定default='default value'
    username= db.Column(db.String(80),unique=True,nullable=False)
    email= db.Column(db.String(80),unique=True,nullable=False)
    About_me=db.Column(db.Text(512),nullable=True)
    password_hash= db.Column(db.String(128),unique=True,nullable=False)
    #user can have many post
    posts=db.relationship("Posts",backref='poster')#psoter like a fake Column
    @property#將函式變成只能讀取的特性，不能更新或式刪除
    def password(self):
        raise AttributeError('Password is not a readable attribute! ')
    @password.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)
    
    def verify_password(self,password):
        return   check_password_hash(self.password_hash,password)

    

def create_(name,username,email,password,About_me):
    if User.query.count()== 0:  #query查詢 如果從資料庫中查詢資料筆數為id=1
        user=User(id=1,name=name,username=username,email=email,password=password,About_me=About_me)
    else:  
        oldUser = User.query.order_by(desc('id')).first()#從小排到大的第一個去
        user=User(id=oldUser.id+1,name=name,username=username,email=email,password=password,About_me=About_me)#再傳到views->create(呈現畫面後)傳到model(處理資料)->存到User(上方的class user)資料結構後給這裡
    db.session.add(user)
    db.session.commit()
    return

def update_(id,name,username,email,About_me):
    user=User.query.filter_by(id=id).first()
    user.name=name
    user.username=username
    user.email=email
    user.About_me=About_me
    db.session.commit()
    return
def delete_(id):
    user=User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(255),unique=True,nullable=False)
    content=db.Column(db.String(512),nullable=False)
    # author=db.Column(db.String(255),nullable=False)
    date_posted=db.Column(db.DateTime,default=datetime.utcnow)
    slug=db.Column(db.String(255))
    #ForeignKey to link users(refer to primary key to the user)
    poster_id=db.Column(db.Integer,db.ForeignKey("user.id"))

def create_post_(title,content,poster,slug,About_me):
    post=Posts(title=title,content=content,poster_id=poster,slug=slug,About_me=About_me)
    db.session.add(post)
    db.session.commit()
    return
def show_post_():
    post=Posts.query.order_by(Posts.date_posted).all()
    return post
def show_post_id(id):
    post_id=Posts.query.filter_by(id=id).all()
    return post_id
def edit_post_id(post):
    db.session.add(post)
    db.session.commit()
    return
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()
from .. import db
from sqlalchemy import desc
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(80),unique=True,nullable=False)
    email= db.Column(db.String(80),unique=True,nullable=False)
    password_hash= db.Column(db.String(128),unique=True,nullable=False)
    @property#將函式變成只能讀取的特性

def create_(username,email,password):
    if User.query.count()== 0:  #query查詢 如果從資料庫中查詢資料筆數為id=1
        user=User(id=1,username=username,email=email,password=password)
    else:  
        oldUser = User.query.order_by(desc('id')).first()#從小排到大的第一個去
        user=User(id=oldUser.id+1,username=username,email=email,password=password)#再傳到views->create(呈現畫面後)傳到model(處理資料)->存到User(上方的class user)資料結構後給這裡
    db.session.add(user)
    db.session.commit()
    return

def update_(id,username,email,password):
    user=User.query.filter_by(id=id).first()
    user.username=username
    user.email=email
    user.password=password
    db.session.commit()
    return
def delete_(id):
    user=User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return

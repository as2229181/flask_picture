from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from flask_login import LoginManager, LoginManager
from flask_ckeditor import CKEditor
from flask_uploads import UploadSet,configure_uploads,IMAGES
import os
login_manager = LoginManager()
app = Flask(__name__)
app.config.from_object('config')
app.config['SECRET_KEY']= "12345678"
db = SQLAlchemy(app)
migrate=Migrate(app,db)
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please login'
app.secret_key = "681eea015d3956ead9bcc2c3dca1eda75c49a2fb2e4d532876b841770c03acdd"
ckeditor = CKEditor(app)
UPLOAD_FOLDER = 'static'
app.config["UPLOADED_PHOTOS_DEST"]=os.path.join(app.root_path,'static')
photos=UploadSet("photos",IMAGES)
configure_uploads(app, photos)
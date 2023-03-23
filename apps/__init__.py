from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from flask_login import LoginManager, LoginManager
from flask_ckeditor import CKEditor
from werkzeug.utils import secure_filename
# from flask_uploads import UploadSet,configure_uploads,IMAGES
import os,logging
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
app.config['UPLOAD_FOLDER'] ="C:/Users/as222/flask_project2/apps/static/image/upload"
ALLWOED_EXTENSIONS=set({'png','jpg','jpeg','gif'})

# images=UploadSet("photos",IMAGES)
# configure_uploads(app, images)
# UPLOADS_AUTOSERVE=True
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLWOED_EXTENSIONS




formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('flask.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
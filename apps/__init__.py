from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
app = Flask(__name__)
app.config.from_object('config')
app.config['SECRET_KEY']= "12345678"
db = SQLAlchemy(app)
migrate=Migrate(app,db)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = ""

database = SQLAlchemy(app)
bcrypt = Bcrypt(app) # criptografia
login_manager = LoginManager(app) # login
login_manager.login_view = "homepage" # Login será feito em homepage

from fakepinterest import routes
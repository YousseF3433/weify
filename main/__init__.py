from os import environ as env

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__, static_folder="assets")
app.secret_key = "SdmnjasbdhjAsdGsd5sd4421312545#$%@#$@%$%68a76d78ad5adaasdasdas" #env['secret_key']

app.config['UPLOAD_FOLDER'] = 'main/assets/img/'
app.config['ALLOWED_EXTENSIONS'] = {"png", "jpg", "jpge"}
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
 
db = SQLAlchemy(app) 
migrate = Migrate(app, db)
app.app_context().push()
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)
mail = Mail(app)

from .arabic import ar_bp

app.register_blueprint(ar_bp, url_prefix='/ar')

from .routs import *
from .errors import *
from .admin import *
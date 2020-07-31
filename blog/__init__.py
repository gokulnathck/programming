from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'SecretKeyShouldBeSecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gokul:gokul@localhost/base'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)
auth = HTTPBasicAuth()

from .models.details import Usersdetails,Postsdetails
from .routes import routes

from flask_restful import Resource
from datetime import datetime,timedelta
from ..models.details import Usersdetails
from flask import jsonify,request
from werkzeug.security import check_password_hash
from .. import app,db
import jwt

class LoginR(Resource):
    def post(self, username):
        author = request.authorization
        users = Usersdetails.query.filter_by(username=username).first()
        if not users:
            return jsonify({"Message": "please enter a valid user username"})
        if users.username == author.username and check_password_hash(users.password, author.password):
            token = jwt.encode({"userid":users.userid, "exp":datetime.utcnow() + timedelta(minutes=60)}, app.config["SECRET_KEY"])
            return jsonify({'token': token.decode('UTF-8')})
        return jsonify({"Message": "Invalid credentials"})



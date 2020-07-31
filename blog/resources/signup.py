from flask_restful import Resource
from ..models.details import Usersdetails
from flask import jsonify,request
from werkzeug.security import generate_password_hash
from .. import db


class SignupR(Resource):
    def post(self):
        data = request.json
        if not data['username']:
                return jsonify({"Message": " username is required"})
        if Usersdetails.query.filter_by(username=data['username']).first():
            return jsonify({"Message": "Username already exists"})
        username = data['username']
        if not data['email']:
                return jsonify({"Message": " email is required"})
        if Usersdetails.query.filter_by(email=data['email']).first():
            return jsonify({"Message": "email already exists"})
        email = data['email']
        if not data['phone']:
                return jsonify({"Message": " phone is required"})
        if Usersdetails.query.filter_by(phone=data['phone']).first():
            return jsonify({"Message": "phone number already exists"})
        phone = data['phone']
        if not data['password']:
                return jsonify({"Message": " password is required"})
        password = generate_password_hash(data['password'])
        user = Usersdetails(username=username, email=email, phone=phone, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify({"Message": "Successfully Registered"})

from flask_restful import Resource
from ..models.details import Usersdetails
from flask import jsonify, request
from .token import token_required
from .. import db
from werkzeug.security import generate_password_hash


class UserR(Resource):
    @token_required
    def get(self, userdata, username):
        user = Usersdetails.query.filter_by(username=username).first()
        if not user:
            return jsonify({"Message":"Incorrect username"})
        if userdata['userid'] == user.userid:
            data = dict(username=user.username,email=user.email,phone=user.phone)
            return jsonify({"user": data})
        return jsonify({"Message": "Unauthorised Access"})

    @token_required
    def put(self, userdata, username):
        user = Usersdetails.query.filter_by(username=username).first()
        if not user:
            return jsonify({"Message":"Incorrect username"})
        if userdata['userid'] == user.userid:
            data = request.json
            users = Usersdetails.query.filter_by(userid=user.userid).first() 
            if Usersdetails.query.filter_by(username=data['username']).first():
                return jsonify({"Message": "username already exists"})
            users.username = data['username']      
            if Usersdetails.query.filter_by(email=data['email']).first():
                return jsonify({"Message": "Email already exists"})
            users.email = data['email']        
            if Usersdetails.query.filter_by(phone=data['phone']).first():
                return jsonify({"Message": "Phone already exists"})
            users.phone = data['phone']         
            users.password = generate_password_hash(data['password'])
            db.session.commit()
            return jsonify({"Message": "Successfully Updated"})
        return jsonify({"Message": "Unauthorised Access"})

    @token_required
    def patch(self, userdata, username):
        user = Usersdetails.query.filter_by(username=username).first()
        if not user:
            return jsonify({"Message":"Incorrect username"})
        if userdata['userid'] == user.userid:
            data = request.json
            users = Usersdetails.query.filter_by(userid=user.userid).first()
            if 'username' in data:
                if not Usersdetails.query.filter_by(username=data['username']).first():
                    users.username = data['username']        
                    db.session.commit()
                    return jsonify({"Message": "username Successfully Updated"})
                else:
                    return jsonify({"Message": "Email already exists"})
            if 'email' in data:
                if not Usersdetails.query.filter_by(email=data['email']).first():
                    users.email = data['email']        
                    db.session.commit()
                    return jsonify({"Message": "email Successfully Updated"})
                else:
                    return jsonify({"Message": "Email already exists"})
            if 'phone' in data:
                if not Usersdetails.query.filter_by(phone=data['phone']).first():
                    users.phone = data['phone']
                    db.session.commit()
                    return jsonify({"Message": "phone Successfully Updated"})
                else:
                    return jsonify({"Message": "Phone already exists"})
            if 'password' in data:
                users.password = generate_password_hash(data['password'])
                db.session.commit()
                return jsonify({"Message": "password Successfully Updated"})
            return jsonify({"Message":"You need anyone of username,email,phone,password to use patch method"})
        return jsonify({"Message": "Unauthorised Access"})

    @token_required
    def delete(self, userdata, username):
        user = Usersdetails.query.filter_by(username=username).first()
        if not user:
            return jsonify({"Message":"Incorrect username"})
        if userdata['userid'] == user.userid:
            db.session.delete(Usersdetails.query.filter_by(userid=user.userid).first())
            db.session.commit()
            return jsonify({"Message": "Successfully Deleted"})    
        return jsonify({"Message": "Unauthorised Access"})

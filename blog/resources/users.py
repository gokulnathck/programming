from flask_restful import Resource
from ..models.details import Usersdetails
from flask import jsonify

class UsersR(Resource):
    def get(self):
        users = Usersdetails.query.all()
        totalusers = []
        for user in users:
            data = {}
            data['username'] = user.username
            totalusers.append(data)
        return jsonify({'users': totalusers})


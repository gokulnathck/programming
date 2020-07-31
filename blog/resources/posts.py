from flask_restful import Resource
from ..models.details import Postsdetails, Usersdetails
from flask import jsonify

class PostsR(Resource):
    def get(self):
        posts = Postsdetails.query.all()
        totalposts = []
        for post in posts:
            user = Usersdetails.query.filter_by(userid=post.userid).first()
            data = {}
            data['title'] = post.title
            data['content'] = post.content
            data['username'] = user.username
            totalposts.append(data)
        return jsonify({'posts': totalposts})


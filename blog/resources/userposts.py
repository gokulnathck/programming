from flask_restful import Resource
from ..models.details import Postsdetails,Usersdetails
from flask import jsonify,request
from .token import token_required
from .. import db

class UserpostsR(Resource):
    @token_required
    def get(self, userdata, username):
        user = Usersdetails.query.filter_by(username=username).first()
        if not user:
            return jsonify({"Message":"Incorrect username"})
        if userdata['userid'] == user.userid:
            userposts = [] 
            posts = Postsdetails.query.filter_by(userid=user.userid).all()
            for post in posts:
                data = {}
                data['postid'] = post.postid
                data['title'] = post.title
                data['content'] = post.content
                userposts.append(data)
            return jsonify({'posts': userposts})                
        return jsonify({"Message": "Unauthorised Access"})

    @token_required
    def post(self,userdata,username):
        user = Usersdetails.query.filter_by(username=username).first()
        if not user:
            return jsonify({"Message":"Incorrect username"})
        if userdata['userid'] == user.userid:
            data = request.json
            if not data['title']:
                return jsonify({"Message": " Title is required"})
            title = data['title']
            if not data['content']:
                return jsonify({"Message": " Content is required"})
            content = data['content']
            userid = user.userid
            post = Postsdetails(title=title,content=content,userid=userid)
            db.session.add(post)
            db.session.commit()
            return jsonify({"Message":"Successfully posted"})
        else:
            return jsonify({"Message": "Unauthorised Access"})

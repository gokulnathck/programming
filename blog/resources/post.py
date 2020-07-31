from flask_restful import Resource
from ..models.details import Postsdetails,Usersdetails
from flask import jsonify,request
from .token import token_required
from .. import db

class PostR(Resource):
    @token_required
    def get(self, userdata, username,postid):
        user = Usersdetails.query.filter_by(username=username).first()
        if not user:
            return jsonify({"Message":"Incorrect username"})

        if userdata['userid'] == user.userid:
            post = Postsdetails.query.filter_by(postid=postid).first()
            if not post:
                return jsonify({"Message:Incorrect postid"})
            data = {}
            data['postid'] = post.postid
            data['title'] = post.title
            data['content'] = post.content
            return jsonify({'posts': usersposts})                
        
        return jsonify({"Message": "Unauthorised Access"})

    @token_required
    def put(self, userdata, username,postid):
        user = Usersdetails.query.filter_by(username=username).first()
        if not user:
            return jsonify({"Message":"Incorrect username"})
        if userdata['userid'] == user.userid:
            post = Postsdetails.query.filter_by(postid=postid).first()
            if not post:
                return jsonify({"Message:Incorrect postid"})
            data = request.json
            if not data['title']:
                return jsonify({"Message":"Title is required"})
            post.title = data['title']      
            if not data['content']:
                return jsonify({"Message":"Content is required"})
            post.content = data['content']         
            db.session.commit()
            return jsonify({"Message": "Successfully Updated"})
        return jsonify({"Message": "Unauthorised Access"})

    @token_required
    def patch(self, userdata, username,postid):
        user = Usersdetails.query.filter_by(username=username).first()
        if not user:
            return jsonify({"Message":"Incorrect username"})
        if userdata['userid'] == user.userid:
            post = Postsdetails.query.filter_by(postid=postid).first()
            if not post:
                return jsonify({"Message:Incorrect postid"})
            data = request.json
            if 'title' in data:
                post.title = data['title']
                db.session.commit() 
                return jsonify({"Message":"Title is updated"})
            if 'content' in data:
                post.content = data['content']
                db.session.commit()         
                return jsonify({"Message":"Content is updated"})
            return jsonify({"Message": "enter either title or content to patch"})
        return jsonify({"Message": "Unauthorised Access"})

    @token_required
    def delete(self, userdata, username,postid):
        user = Usersdetails.query.filter_by(username=username).first()
        if not user:
            return jsonify({"Message":"Incorrect username"})
        if userdata['userid'] == user.userid:
            post = Postsdetails.query.filter_by(postid=postid).first()
            if not post:
                return jsonify({"Message:Incorrect postid"})
            db.session.delete(post)
            db.session.commit()
            return jsonify({"Message": "Successfully Deleted"})    
        return jsonify({"Message": "Unauthorised Access"})

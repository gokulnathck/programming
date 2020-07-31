from .. import db

class Usersdetails(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    phone = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    posts = db.relationship('Postsdetails',backref='author',lazy=True)

class Postsdetails(db.Model):
    postid = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(30),nullable=False)
    content = db.Column(db.Text,nullable=False)
    userid = db.Column(db.Integer,db.ForeignKey('usersdetails.userid'),nullable=False)
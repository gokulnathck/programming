from functools import wraps
from .. import app
import jwt
from flask import jsonify,request

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "x-access-token" in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({"Message":"Token is missing"})
        try:
            userdata = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({"Message": "Token is invalid or expired"})
        return f(userdata=userdata, *args, **kwargs)
    return decorated


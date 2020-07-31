from .. import api
from ..resources.signup import SignupR
from ..resources.login import LoginR
from ..resources.users import UsersR
from ..resources.user import UserR
from ..resources.posts import PostsR
from ..resources.userposts import UserpostsR
from ..resources.post import PostR

api.add_resource(SignupR, '/users/signup')
api.add_resource(LoginR, '/users/<string:username>/login')
api.add_resource(UsersR, '/users')
api.add_resource(UserR, '/users/<string:username>')
api.add_resource(PostsR, '/users/posts')
api.add_resource(UserpostsR, '/users/posts/<string:username>')
api.add_resource(PostR, '/users/posts/<string:username>/<int:postid>')
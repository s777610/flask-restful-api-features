from flask import request, g, url_for
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token
from models.user import UserModel
from schemas.user import UserSchema
from oa import github

from models.user import UserModel

user_schema = ()

"""in order to begin the authorization flow
we send users to GitHub authorization page with our details,
GitHub see those details, then send the user over to the log in page"""
class GithubLogin(Resource):
    @classmethod
    def get(cls):
        # where do we wanna go once the user has been authorised
        # github.authorize is name of our endpoint, in app.py
        # _external=True means build the full URL like, http://localhost:5000/login/github/authorized
        return github.authorize(url_for("github.authorize", _external=True))


"""
when users access this resource, they've already given us authorization
to use their details for our app. what we have to do is take those details,
take what GitHub has forwarded to us, and send it over to GitHub as post request
to retrieve the user's access token, then use access token to get back users"""
class GithubAuthorize(Resource):
    @classmethod
    def get(cls):
        # this make post request to GitHub and give back to us access token in response
        resp = github.authorized_response() # authorized_response() give us access token

        if resp is None or resp.get('access_token') is None:
            error_response = {
                "error": request.args['error'],
                "error_description": request.args['error_description']
            }
            return error_response

        g.access_token = resp['access_token'] # put access token into g
        github_user = github.get('user')  # this uses the access_token from the tokengetter function in oa.py
        github_username = github_user.data['login'] # s777610 in this case
        
        user = UserModel.query.filter_by(username=github_username).first()

        if not user:
            user = UserModel(username=github_username, password=None)
            user.save_to_db()

        access_token = create_access_token(identity=user.id, fresh=True)
        refresh_token = create_refresh_token(user.id)

        return {"access_token": access_token, "refresh_token": refresh_token}, 200
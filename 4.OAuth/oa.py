import os
from flask_oauthlib.client import OAuth

"""
OAuth standard is a standard, 
it means that GitHub, Twitter, Facebook, Instagram,
all of those use the same stuff. only difference is URL 
consumer_key and consumer_secret are part of standard of OAuth 2.0

To connect to a remote application create a OAuth object and, 
register a remote application(Github) on it using the remote_app() method

1. onsumer_key=os.getenv("GITHUB_CONSUMER_KEY")
Unique identifier of our app

2. request_token_params={"scope": "user:email"}
add &scope=user:email to requests when we do authorization, 
this gives GitHub information regarding what data we will want to access, 
if we get authorization.

3. access_token_method="POST"
This is that second request. Once the user has authorised us,
we're going to get the access token from the API by 
sending a post request with our client ID and client secret

4. access_token_url
what we send the data(client ID, client secret) to so we can get back the access token.

5. authorize_url
where we send the user in that initial request with client ID and state.
"""
oauth = OAuth()

github = oauth.remote_app(
    'github',
    consumer_key=os.getenv("GITHUB_CONSUMER_KEY"), 
    consumer_secret=os.getenv("GITHUB_CONSUMER_SECRET"), 
    request_token_params={"scope": "user:email"}, 
    base_url="https://api.github.com/",
    request_token_url=None,
    access_token_method="POST",
    access_token_url="https://github.com/login/oauth/access_token",
    authorize_url="https://github.com/login/oauth/authorize"
)
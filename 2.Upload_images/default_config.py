# Those default will be used while developing
import os

DEBUG = True
SQLALCHEMY_DATABASE_URI = "sqlite:///data.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True
UPLOADED_IMAGES_DEST = os.path.join("static", "images")  # manage root folder
JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]
SECRET_KEY = os.environ["APP_SECRET_KEY"]
UPLOADED_IMAGES_DEST = os.path.join("static", "images") # where to store images, must be same as IMAGE_SET in default_config.py
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = [
    "access",
    "refresh",
]  # allow blacklisting for access and refresh tokens

# Those config will be used while deploying
import os

DEBUG = False
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///data.db")

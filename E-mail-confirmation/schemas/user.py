from ma import ma # ma is object, whcih we have link to ma.init_app(app) in app.py
from models.user import UserModel


# return a dictionary with those keys
class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        # it tell marshmallow that this field is for loading data
        load_only = ("password",)
        dump_only = ("id", "activated")

    


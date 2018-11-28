from ma import ma # ma is object, whcih we have link to ma.init_app(app) in app.py
from marshmallow import pre_dump # a method running before you dump a user model into json
from models.user import UserModel


# return a dictionary with those keys
class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        # it tell marshmallow that this field is for loading data
        load_only = ("password",)
        dump_only = ("id", "confirmation")

    @pre_dump
    def _pre_dump(self, user: UserModel):
        """dump will not indude old expired confirmations"""
        user.confirmation = [user.most_recent_confirmation]
        return user

    


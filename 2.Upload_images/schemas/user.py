from ma import ma
from marshmallow import pre_dump
from models.user import UserModel


class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel #  come from flask marshmallow
        load_only = ("password",)
        dump_only = ("id", "confirmation")

    @pre_dump
    def _pre_dump(self, user: UserModel):
        user.confirmation = [user.most_recent_confirmation]
        return user

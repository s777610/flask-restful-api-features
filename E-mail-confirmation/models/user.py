from flask import request, url_for
from requests import Response
from db import db
from libs.mailgun import Mailgun
from models.confirmation import ConfirmationModel

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    # nullable=False
    # when we load data from JSON into Marshmallow, 
    # it's going to check whether they are require
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    
    # lazy="dynamic", not get confirmation from db when create UserModel
    # cascade="all, delete-orphan", whenever delete a user, also delete all confirmation related to that user
    confirmation = db.relationship(
        "ConfirmationModel", lazy="dynamic", cascade="all, delete-orphan"
    )

    @property
    def most_recent_confirmation(self) -> "ConfirmationModel":
        return self.confirmation.order_by(db.desc(ConfirmationModel.expire_at)).first()

    """
    # we don't need it because nullable=False for username and password
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
    
    but!
    UserModel(username='bob', password='1234') <- still allowed
    """

    @classmethod
    def find_by_username(cls, username: str) -> "UserModel":
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email: str) -> "UserModel":
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id: int) -> "UserModel":
        return cls.query.filter_by(id=_id).first()

    # Response is something another API gives us
    def send_confirmation_email(self) -> Response:
        """  request.url_root is http://127.0.0.1:5000/
        url_for() is going to calculate the address for a particular resource or route in flask.
        "userconfirm" is UserConfirm resources 
        url_for("userconfirm", user_id=self.id) is /user_confirm/1 for example
        link is http://127.0.0.1:5000/user_confirm/1  """
        
        link = request.url_root[0:-1] + url_for(
            "confirmation", confirmation_id=self.most_recent_confirmation.id
        )
        subject = "Registration confirmation"
        text = f"Please click the link to confirm your registration: {link}"
        html = f'<html>Please click the link to confirm your registration: <a href="{link}">{link}</a></html>'

        return Mailgun.send_email([self.email], subject, text, html)
        
        

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

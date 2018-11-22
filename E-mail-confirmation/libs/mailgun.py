import os
from typing import List
from requests import Response, post

FAILED_LOAD_API_KEY = "Failed to load Mailgun API key."
FAILED_LOAD_DOMAIN = "Railed to load Mailgun Domain."
ERROR_SENDING_EMAIL = "Error in sending comfirmation email, user registration failed."

# give your exception name(MailGunException)
# when raise MailGunException, message will be printed
class MailGunException(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class Mailgun:
    MAILGUN_DOMAIN = os.environ.get("MAILGUN_DOMAIN") # can be none
    MAILGUN_API_KEY = os.environ.get("MAILGUN_API_KEY") # can be none
    FROM_TITLE = "Stores Restful API"
    FROM_EMAIL = "postmaster@sandbox52569de6abca49879c3f30758bce0d53.mailgun.org"

    # Response is something another API gives us
    @classmethod
    def send_email(cls, email: List[str], sebject: str, text: str, html: str) -> Response:
        if cls.MAILGUN_API_KEY is None:
            raise MailGunException(FAILED_LOAD_API_KEY)

        if cls.MAILGUN_DOMAIN is None:
            raise MailGunException(FAILED_LOAD_DOMAIN)

        # need to send post request to Mailgun API
        response = post(
            f"https://api.mailgun.net/v3/{cls.MAILGUN_DOMAIN}/messages",
            auth=("api", cls.MAILGUN_API_KEY),
            data={
                "from": f"{cls.FROM_TITLE} <{cls.FROM_EMAIL}>",
                "to": email,
                "subject": sebject,
                "text": text,
                "html": html
            },
        )

        if response.status_code != 200:
            raise MailGunException(ERROR_SENDING_EMAIL)
        
        return response 
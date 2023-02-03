from werkzeug.security import check_password_hash
from bson import ObjectId


class User:
    def __init__(self, _id, username, email, password):
        self._id = _id
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return self._id

    def get_username(self):
        return self.username

    def check_password(self, password_input):
        return check_password_hash(self.password, password_input)

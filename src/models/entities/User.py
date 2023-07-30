from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin):
    
    def __init__(self, id, fullname, email, password) -> None:
        self.id = id
        self.fullname = fullname
        self.email = email
        self.password = password

    @classmethod
    def check_password(self, inputPassword, password):
        return inputPassword == password
    
    
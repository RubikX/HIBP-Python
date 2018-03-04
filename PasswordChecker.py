import requests
from hashlib import sha1

class PasswordChecker:

    API = 'https://api.pwnedpasswords.com/range/'

    def __init__(self):
        self.api_version = 2
        self.user_agent = "PasswordChecker-Python"

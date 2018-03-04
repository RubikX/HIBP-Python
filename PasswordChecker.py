import requests
import argparse
import hashlib
import getpass

class PasswordChecker:

    API = 'https://api.pwnedpasswords.com/range/'

    def __init__(self):
        self.api_version = "2"
        self.user_agent = 'PasswordChecker-Python'

    def get_hash(self, password):
        hash_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        return hash_password
    
    def request(self, url, hash):
        headers = {
            'api-version' : self.api_version,
            'User-Agent' : self.user_agent
        }
        return requests.get(url+hash, headers=headers)
    
    def checker(self, password):
        pwned = False
        count = 0
        for line in self.request(self.API, self.get_hash(password)[:5]).iter_lines():
            tokens = line.decode('utf-8').split(':')
            if ((self.get_hash(password)[:5] + tokens[0]) == self.get_hash(password)):
                pwned = True
                count = tokens[1]
                break
        if pwned:
            print('This password has been pwned.', end='\n')
            print('Seen {} times!'.format(count))
        else:
            print('Not pwned!')        

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Check if password has been pwned.")
    parser.add_argument("--p", dest="pwd", type=str, help="The password to check.")
    args = parser.parse_args()
    if args.pwd is not None:
        PasswordChecker().checker(args.pwd)
    else:
        pwd = getpass.getpass("Please enter password to check: ")
        PasswordChecker().checker(pwd)


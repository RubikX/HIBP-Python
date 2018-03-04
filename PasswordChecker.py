import requests
import argparse
import hashlib
import getpass
import re

class PasswordChecker:

    API_range = 'https://api.pwnedpasswords.com/range/'
    API_breachedaccount = 'https://haveibeenpwned.com/api/v2/breachedaccount/'

    def __init__(self):
        self.api_version = "2"
        self.user_agent = 'PasswordChecker-Python'

    def get_hash(self, password):
        hash_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        return hash_password
    
    def request_password(self, url, hash):
        headers = {
            'api-version' : self.api_version,
            'User-Agent' : self.user_agent
        }
        return requests.get(url+hash, headers=headers)
    
    def pass_checker(self, password):
        pwned = False
        count = 0
        for line in self.request_password(self.API_range, self.get_hash(password)[:5]).iter_lines():
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

    def request_acc(self, url, account):
        headers = {
            'api-version' : self.api_version,
            'User-Agent' : self.user_agent
        }
        return requests.get(url+account+'?truncateResponse=true', headers=headers)

    def acc_checker(self, account):
        nameregex = re.compile(r'"Name":"(.*?)"')
        mo = nameregex.findall(self.request_acc(self.API_breachedaccount, account).text)
        if len(mo) == 0:
            print("This account has not been pwned.")
        else:
            print("This account has been pwned in the following sites: ", end="\n")
            for i in mo:
                print(i)

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Check if password has been pwned.")
    parser.add_argument("--p", dest="pwd", type=str, nargs='?', help="The password to check.")
    parser.add_argument("--a", dest="acc", type=str, nargs='?', help="The account to check.")
    args = parser.parse_args()
    if args.pwd is not None:
        PasswordChecker().pass_checker(args.pwd)
    if args.acc is not None:
        PasswordChecker().acc_checker(args.acc)

from .account import Account

class User :
    def __init__(self,username : str) :
        self.username = username
        self.account = Account()
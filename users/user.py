import uuid

class User:
    def __init__(self, nickname, passwd) -> None:
        self.user_id = str(uuid.uuid4())
        self.nickname = nickname
        self.passwd = passwd
        self.wallets = []

    def add_wallet(self, wallet):
        self.wallets.append(wallet)

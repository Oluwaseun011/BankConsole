from models.Account import Account
import datetime


class Overdraft:
    def __init__(self, account: Account, amount: float, status: str):
        self.account = account
        self.amount = amount
        self.date = datetime.date.today()
        self.status = "inactive"

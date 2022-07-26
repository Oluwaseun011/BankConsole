from models.AccountHolder import AccountHodler
import datetime


class Account:
    def __init__(self, id: int, account_holder: AccountHodler, pin: int):
        self.id = id
        self.account_holder = account_holder
        self.account_number = None
        self.pin = pin
        self.account_type = None
        self.account_balance = 0.0
        self.date_of_creation = datetime.date.today()
        self.account_status = 'active'

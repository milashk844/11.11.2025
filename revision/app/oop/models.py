import uuid
from typing import Self

class FinancialCalculator:
    def __init__(self):
        self.accounts: list[BankAccount] = list

class Person(FinancialCalculator):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.tin = uuid.uuid4()
        self.money = 0

class BankAccount:
    def __init__(self, client: Person, bank: "Bank"):
        self.client = client
        self.balance = 0
        self.bank = Bank

    def __str__(self): -> str:

    def deposit(self, amount: float):
        amount = abs(amount)
        self.balance += amount


    def withraw(self, amount: float):
        amount = abs(amount)
        self.balance -= amount

    def transfer(self, amount: float, other: Self):
        amount = abs(amount)
        self.withraw(amount)
        other.deposit(amount)

class Bank:
    def __init__(self, name: str):
        self.accounts: list[BankAccount] = []
        self.name = f"PAT {name.upper()}"
    def open_account(self, client: Person):
        new_account = BankAccount(client, bank= self
        self.accounts.append(new_account)
        client.accounts.append(new_account)

    return new_account


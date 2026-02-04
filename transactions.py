from datetime import date, datetime
import db
import sqlite3

### Everything related to one time purchases ###

categories: list[str] = ['spesa', 'games', 'sport', 'libri', 'cinesate', 'uni', 'medicine', 'altro']

class Transaction():
    def __init__(self, amount: float, category: int, date: date, description: str= ""):
        self.amount = amount
        self.category = category
        self.date = date
        if description.strip() != "":
            self.description = description.strip()

    def set_date(self, date: date):
        self.date = date
    
    def set_amount(self, amount: float):
        self.amount = amount
    
    def set_category(self, category: int):
        if category <= len(categories):
            self.category = category

    def set_description(self, description: str):
        self.description = description

    def get_date(self) -> date:
        return self.date
    
    def get_amount(self) -> float:
        return self.amount
    
    def get_category(self) -> int:
        return self.category

    def get_description(self) -> str:
        return self.description
    
    def has_description(self) -> bool:
        return self.description != ""

new_transactions: list[Transaction] = []

# get category of new transaction
def ask_category() -> int:
    while True:
        print("Scegli la categoria dell'acquisto tra le seguenti:")
        for i in range(len(categories)):
            print(f'{i+1}. {categories[i]}')
        category_input = input('>')
        if not(category_input.isdigit()):
            print('try again')
            continue
        if int(category_input) > 0 and int(category_input) <= len(categories):
            return int(int(category_input) - 1)
        print('try again')

# get amount for new transaction    
def ask_amount() -> float:
    while True:
        print("enter amount")
        amount = input(">")
        if amount.isdigit():
            return float(amount)
        print("try again")

# get description
def ask_description() -> str:
    print("Write a short description (or leave blank)")
    desc = input("> ")
    return desc.strip()

# save transaction in db
def save_transaction(amount: float, category: int, description: str = "") -> bool:
    today: date = date.today()
    transaction: Transaction = Transaction(amount, category, today, description)
    new_transactions.append(transaction)
    if db.insert_transaction(amount, today, category, description) != -1:
        return True
    return False

# begin a new transaction
def new_transaction() -> bool:
    amount: float = 0.00
    cat: int = 0
    cat = ask_category()
    amount = ask_amount()
    description = ask_description()
    return save_transaction(amount, cat, description.strip())

def get_total_amount_month(date: date=date.today()) -> float:
    transactions: list[sqlite3.Row] = db.get_month_transactions(date)
    total: float = 0.0
    for t in transactions:
        total += t['amount']
    return total


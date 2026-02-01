import db
from transactions import ask_amount, ask_description
from datetime import datetime, date

### Everything related to recurring payments ###

class Recurring():
    def __init__(self, amount: float, date: date, description: str = "", recurrence: int = 1):
        self.amount = amount
        self.description = description
        self.date = date
        self.recurrence = recurrence

    def get_amount(self) -> float:
        return self.amount
    def get_description(self) -> str:
        return self.description.strip()
    def get_date(self) -> date:
        return self.date
    def get_recurrence(self) -> int:
        return self.recurrence

# get number of months for each recurrence of payment
def ask_recurrence() -> int:
    while True:
        print("Insert months of payment recurrence (leave blank for 1)")
        rec = input("> ")
        rec = rec.strip()
        if rec == "":
            return 1
        if rec.isdigit():
            return int(rec)
        print("try again")

# save recurring in db
def save_recurring(recurring_obj: Recurring) -> int:
    return db.insert_recurring(recurring_obj.get_amount(), recurring_obj.get_date(), recurring_obj.get_description(), recurring_obj.get_recurrence())
    
# create new recurring payment
def new_recurring() -> bool:
    amount: float = ask_amount()
    description: str = ask_description()
    today: date = date.today()
    recurrence: int = ask_recurrence()
    recurring_obj = Recurring(amount, today, description, recurrence)
    save_recurring(recurring_obj)
    return True
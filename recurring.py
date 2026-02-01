import db
from transactions import ask_amount, ask_description
from datetime import datetime, date

### Everything related to recurring payments ###

class Recurring():
    def __init__(self, amount: float, date: date, description: str = ""):
        self.amount = amount
        self.description = description
        self.date = date

    def get_amount(self) -> float:
        return self.amount
    def get_description(self) -> str:
        return self.description.strip()
    def get_date(self) -> date:
        return self.date

# save recurring in db
def save_recurring(recurring_obj: Recurring) -> bool:
    return db.insert_recurring(recurring_obj.get_amount(), recurring_obj.get_date(), recurring_obj.get_description())
    
# create new recurring payment
def new_recurring() -> bool:
    amount: float = ask_amount()
    description: str = ask_description()
    today: date = date.today()
    recurring_obj = Recurring(amount, today, description)
    save_recurring(recurring_obj)
    return True
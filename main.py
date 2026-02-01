from datetime import date, datetime
import db
import transactions
import recurring
from transactions import Transaction

actions: str = 'arpq'

def welcome():
    print("Personal Expense Tracker")
    print("Select action")
    print("a: add new transaction")
    print("m: add monthly recurring payment")
    print("r: add recurring payment every x months")
    print("p: print monthly stats")
    print("q: quit")

def ask_action() -> str:
    action = ''
    while True:
        action = input(">")
        if action.strip().lower() in actions:
            return action
        print("try again")

def main():
    welcome()
   
    while True:
        print('-------')
        action: str = ask_action()
        match action:
            case 'a': # new transaction
                transactions.new_transaction()
            case 'r': # new recurring
                recurring.new_recurring()
            case 'p': # print stats
                print() # todo
                exit()
            case 'q': # quit
                exit()
            case '_':
                print()
                exit()

if __name__=='__main__':
    main()
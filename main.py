from datetime import date, datetime
import db
import transactions
import recurring
from transactions import Transaction
import sys

actions: str = 'arpq'

def help():
    print("Usage:")
    print("Select an action by adding the letter on the same line")
    print("a: add new transaction")
    print("m: add monthly recurring payment")
    print("p: print monthly stats")

def ask_action() -> str:
    action = ''
    while True:
        action = input(">")
        if action.strip().lower() in actions:
            return action
        print("try again")

def main():
    # welcome()
    if len(sys.argv) <= 1:
        help()
        exit()

    action = sys.argv[1]
    match action:
        case 'a': # new transaction
            transactions.new_transaction()
        case 'r': # new recurring
            recurring.new_recurring()
        case 'p': # print stats
            print(transactions.get_total_amount_month())
            exit()
        case 'h':
            help()
            exit()
        case 'q': # quit
            exit()
        case '_':
            print()
            exit()

if __name__=='__main__':
    main()
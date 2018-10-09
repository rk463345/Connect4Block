# driver for Connect4Block
import sys
import connect4
import crackhash
import ledger
from chain import Chain


def find_patient():
    connect4.clear()
    input('fEnter SSN to get patient information:\n')

def add_transaction():
    data = input("Enter the directory for file to be added to the block chain:\n")

    connect4.create_block(data)

def mine():
    crackhash.mine_hash()

def main():
    while True:
        print("*" * 18)
        print("What would you like to do?\n"
             "Add transaction = 1\n"
            "Mine blocks = 2\n"
            "Find Data = 3\n"
            "exit = q")
        print("*" * 18)

        choice = input("CHOICE = ")
        if choice == "1":
            add_transaction()
        elif choice == "2":
            mine()
        elif choice =="2":
            find_patient()
        elif choice == "q":
            print("EXITING")
            sys.exit()
        else:
            connect4.clear()
            print("INVALID SELECTION, Try again...")

while __name__ == main():
    main()
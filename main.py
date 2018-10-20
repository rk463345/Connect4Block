# driver for Connect4Block
import sys
import connect4
import ledger
import os
# todo make ledger actually use previous hash function for ledger with genesis blocks
# todo fix search function
# todo modify and implement p2p
# todo research HIPA compliance possibly add in encryption for ledger

def find_patient():
    connect4.clear()
    ssn = input('fEnter SSN to get patient information:\n')
    data = ledger.search_ledger(ssn)
    for item in data:
        print(item)

def add_transaction():
    data = input("Enter the directory for file to be added to the block chain:\n")
    if os.path.exists(data):
        connect4.create_block(data)
    else:
        print('Invalid directory')

def main():
    while True:
        print("*" * 18)
        print("What would you like to do?\n"
             "Add transaction = 1\n"
            "Mine blocks = 2\n"
            "Find Patient (currently not working)= 3\n"
            "exit = q")
        print("*" * 18)

        choice = input("CHOICE = ")
        if choice == "1":
            add_transaction()
        elif choice == "2":
            connect4.cracking()
        elif choice =="3":
            find_patient()
        elif choice == "q":
            print("EXITING")
            connect4.writechain()
            sys.exit()
        else:
            connect4.clear()
            print("INVALID SELECTION, Try again...")

while __name__ == main():
    main()
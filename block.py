# A simple block for concept demo

from random import getrandbits
import hashlib  #needed to be able to hash the data with SHA-256
from os import urandom   #needed for the random seed
import json #used for strings in order for them to be cross programming language compatible


class Block:

    def __init__(self,  p_transaction = ""):
        """Initializes the Block data structure"""
        self.pTransaction = p_transaction  # contains the previous transaction hash
        self.parsedData = []   # holds the data parsed for it to be hashed
        self.seed = urandom(19) # random pulled from system call
        self.vHash = "" # holds the verification hash
        self.bloc = []
        self.final_hash = "" # final hash to be put into the chain

    def package_block(self):
        """checks to make sure data is in type str and then hashes with SHA-256 and returns hash"""
        if len(self.pTransaction) == "":
            # check to see if there is a previous transaction, if not generates a random string to be hashed
            self.pTransaction = getrandbits(256)
            # gets random bits to be hashed in case of being first block
        if type(self.parsedData) != str:    # make sure parsed data is in string form
            self.parsedData = json.dumps(self.parsedData, sort_keys=True)
            # makes all pieces of data parsed form file to type str
        #to_hash = str(self.seed) + str(self.pTransaction) + str(self.parsedData) + str(self.parsedData)
        self.vHash = hashlib.sha256(str(self.parsedData).encode('utf-8')).hexdigest()
        # hashes the transaction data with sha-256 for a string encoded with utf-8
        self.bloc.append(self.pTransaction)
        self.bloc.append(self.parsedData)
        self.bloc.append(self.seed)
        self.block.append(self.vHash)
        # creates a string for final hash
        self.final_hash = hashlib.sha256(str(self.bloc).encode('utf-8')).hexdigest()
        # creates final hash
        print("success, block made with {} transaction(s)").format(len(self.bloc))
       
    def add_transaction(self, transaction):
        self.parsedData.append(transaction)
    
    def get_ptransaction(self):
        """returns the hash of the previous transaction"""
        return json.dumps(self.pTransaction, sort_keys=True)
    
    def get_verification_hash(self):
        """returns the has of the current transaction"""
        return json.dumps(self.cTransaction, sort_keys=True)

    def verify_block(self):
        """verifies that the block contents were not manipulated by comparing to hash"""
        if hashlib.sha256(str(self.parsedData).encode('utf-8')).hexdigest() == self.cTransaction:
            print('success')
        else:
            print('contents are not identical')
        #   TODO WRITE THIS FUNCTION

    def print_block(self):
        """prints the data of the block, most likely will be removed"""
        print(self.vHash)
        print(self.pTransaction)
        print(self.parsedData)
        print(self.seed)
        print(self.final_hash)
        self.verify_block()

    def return_un_hashed_set(self):
        """returns the list of data that will be hashed together for the final hash before being put onto the chain"""
        full_set = [self.pTransaction, self.parsedData, self.seed, self.cTransaction]
        return full_set

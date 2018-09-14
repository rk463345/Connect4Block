# A simple block chain for concept demo

from random import getrandbits
import hashlib  #needed to be able to hash the data with SHA-256
from os import urandom   #needed for the random seed
import json #in the case of parsed data not being a string json encoder can make a string


class Block:

    def __init__(self, parsed_data, p_transaction = ""):
        """Initializes the Block data structure"""
        self.pTransaction = p_transaction  #contains the previous transaction hash
        self.parsedData = parsed_data    #holds the data parsed for it to be hashed
        self.jsonData = ""
        self.seed = urandom(19)
        self.cTransaction = self.create_hash()  # contains the current transaction hash
        self.final_hash = ""

    def create_hash(self):
        """checks to make sure data is in type str and then hashes with SHA-256 and returns hash"""
        if len(self.pTransaction) < 1:
            self.pTransaction = getrandbits(256)
        if type(self.parsedData) != str: #make sure parsed data is in string form
            self.jsonData = json.dumps(self.parsedData, sort_keys=True) #makes all pieces of data parsed form file to type str
        to_hash = str(self.seed) + str(self.pTransaction) + str(self.parsedData) + str(self.parsedData)
        self.final_hash = hashlib.sha256(str(to_hash).encode('utf-8')).hexdigest()
        return hashlib.sha256(str(self.parsedData).encode('utf-8')).hexdigest() #hashes the data with sha-256 for a string encoded with utf-8

    def get_ptransaction(self):
        """returns the hash of the previous transaction"""
        return self.pTransaction

    def verify_block(self):
        """verifies that the block contents were not manipulated by comparing to hash"""
        if hashlib.sha256(str(self.parsedData).encode('utf-8')).hexdigest() == self.cTransaction:
            print('success')
        else:
            False
        #   TODO WRITE THIS FUNCTION

    def print_block(self):
        print(self.cTransaction)
        print(self.pTransaction)
        print(self.parsedData)
        print(self.seed)
        print(self.final_hash)
        self.verify_block()

    def return_un_hashed_set(self):
        full_set = [self.pTransaction, self.parsedData]
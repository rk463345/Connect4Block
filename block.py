# Connect4 block

# from random import getrandbits
import hashlib  # needed to be able to hash the data with SHA-256
# from os import urandom   #needed for the random seed
import json # used for strings in order for them to be cross programming language compatible

class Block:

    def __init__(self, index,  stamp, contents, p_hash):
        """Initializes the Block data structure"""
        self.index = json.dumps(index)  # index of the block that makes it unique
        self.stamp = json.dumps(stamp)  # contains the time stamp of the block
        self.pTransaction = json.dumps(p_hash)  # contains the previous transaction hash
        self.content = json.dumps(contents)   # holds the data parsed for it to be hashed
        self.final_hash = self.package_block()  # final hash to be put into the chain

    def package_block(self):
        """checks to make sure data is in type str and then hashes with SHA-256 and returns hash"""
        hash_block = hashlib.sha256()   # initiate hash variable
        contents = json.dumps(self.index +
                              self.stamp +
                              self.content +
                              self.pTransaction) # creates the string of the items to be hashed
        hash_block.update(contents) # updates the hash variable to have all the information from contents
        return hash_block.hexdigest()   # digests the hash and returns it

    def p_block(self):
        """returns the hash of this block for the next block"""
        return self.pTransaction

    def p_index(self):
        """returns the index of this block for the next block"""
        return int(self.index)


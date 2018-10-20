import hashlib
import string
import random
import datetime
import json

class Crack:
    def __init__(self, p_hash='0'):
        """Initializes the Block data structure"""
        self.index = str(random.randint(0,1000))  # index of the block that makes it unique
        self.stamp = self.date_stamp()  # contains the time stamp of the block
        self.pTransaction = p_hash  # contains the previous transaction hash
        self.ssn = self.make_ssn()  # calls make_ssn to generate a random ssn
        self.fname  = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(1,15))) # randomly generates a name
        self.lname = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(1,15)))
        self.dob = self.date_stamp()
        self.diag = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(1,15)))
        self.rx = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(1,40)))
        self.tx = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(1,15)))
        self.transaction = self.index + self.stamp + self.fname + ' ' \
                       + self.lname + ' ' + self.dob + ' ' + self.ssn + ' '  \
                       + self.diag + ' ' + self.tx + ' ' + self.rx + ' ' + self.pTransaction
        self.content = self.index + self.stamp + self.fname + ' ' \
                       + self.lname + ' ' + self.dob + ' ' + self.ssn + ' '  \
                       + self.diag + ' ' + self.tx + ' ' + self.rx + self.pTransaction
        self.final_hash = self.package_block()  # final hash to be put into the chain

    def make_ssn(self):
        """randomly generates a ssn"""
        first = str(random.randint(100, 999))
        second = str(random.randint(1, 99))
        third = str(random.randint(1000, 9999))
        if len(second) < 2:
            return first + '-' +  '0' + second + '-' + third
        else:
            return first + '-' + second + '-' + third

    def fhash(self):
        """returns the final hash"""
        return self.final_hash

    def contents(self):
        """returns the contents of the cracked hash"""
        return self.transaction + ' ' + self.final_hash

    def date_stamp(self):
        """randomly generates a date of birth"""
        year = str(random.randint(0, 3000))
        month = random.randint(1, 13)
        day = random.randint(1, 32)
        if month < 10:
            month = '0' + str(month)
        else:
            month = str(month)
        if day < 10:
            day = '0' + str(day)
        else:
            day = str(day)
        return year +'.' + day +'.' + month

    def package_block(self):
        """checks to make sure data is in type str and then hashes with SHA-256 and returns hash"""
        hash_block = hashlib.sha256()   # initiate hash variable
        contents = json.dumps(self.content).encode('UTF-8') # creates the string of the items to be hashed
        hash_block.update(contents) # updates the hash variable to have all the information from contents
        return hash_block.hexdigest()   # digests the hash and returns it

def mine_hash(block_hash):
    """Mines the hash by using the crack object the randomly generate"""
    count = 0
    while True:
        crack = Crack()
        print(block_hash)
        print(crack.fhash())
        count += 1
        if verify(block_hash, crack.fhash()):
            time = datetime.time.microsecond
            return [crack.contents(), time]
        elif count == 3000:
            return ['{} {} {} {} {} {} {} {} {} {} {}'.format("0", "Abraham",  "Lincoln",  "1809.02.12",
                                                       "444-45-6888",  "GreviousWound",  "Surgery",
                                                       "Whiskey", '0', block_hash, "somehash"), datetime.time.microsecond]

def verify(block_hash, crack_hash):
    """verifies that the hash has been cracked"""
    if block_hash == crack_hash:
        return True
    else:
        return False

# COLLECTION OF UTILITIES USED IN THE CREATION OF THE BLOCK
# AND ADDING TO THE CHAIN

from block import Block # importing object block
import datetime
import ledger
from chain import Chain
import os   # used for clearing the screen and detecting os
import crackhash
import uuid

init_chain = Chain()    # initializes the chain object
if init_chain.populate_chain() == 'done':
    print('Chain is populated')
else:
    print('Chain file not found... initializing file')
    file = open('chain.txt', 'w+')
    file.close()

def clear():
    """meant to clear the window when an invalid entry is made"""
    try:
        os.system('clear') # function call to clear the window (Unix Based)
    except:
        os.system('clr')    # function call to clear the window (Microsoft Windows)

def create_block(data):
    """creates the block object, builds block object, adds data to block, packages block, and then adds to chain"""
    if ledger.check_ledger() and init_chain.length() > 0:  # checks of ledger has a previous transaction
        phash = init_chain.get_hash(init_chain.length() -1)
        content = next_block(parse_doc(data), phash)   # function called to get the cleaned strings
        init_chain.add_to(content)  # call to create new block and add to chain
    elif ledger.check_ledger() and init_chain.length() < 0:
        phash = ledger.handle_sha256p()
        init_chain.add_to((genesis_block(), phash))
    else:
        init_chain.add_to(genesis_block(parse_doc(data))) # creates genesis block and adds it to the chain

def parse_doc(directory):
    """parses the incoming txt document to be added to the block"""
    transaction_string = ""  # initiate string to be concatenated
    data = open(directory)  # open directory of the file
    transaction  = data.read()  # read the data in
    data_list = transaction.split("\n")  # split the read data at the new line escape sequence
    for line in data_list:   # for loop to accumulate the data and be added to final string
        transaction_string = transaction_string + line    # concatenates string to be returned
    data.close()    # closes the file
    return transaction_string

def genesis_block(content, phash='0'):
    """used to create the original block for the block chain"""
    block = Block(0, datetime.datetime.now(), content, phash)
    return block.get_final_hash()

def next_block(contents, phash):
    """creates the new block to be added to the chain"""
    previous = ledger.handle_sha256p() # gets the hash from the previous block in the chain
    index = init_chain.length() + 1  # gets and creates the new index for the next block
    stamp = datetime.datetime.now()  # time stamps the block for when it was created
    block = Block(index, stamp, contents, previous)  # creates the new block
    return block.get_final_hash()

def cracking():
    count = 0
    while count < init_chain.length():
        count += 1
        crack = crackhash.mine_hash(init_chain.get_block())
        content = crack[0].split()
        ID = str(uuid.uuid4())
        chash = content[9]
        phash = content[10]
        lname = content[2]
        fname = content[1]
        ssn = content[4]
        dob = content[3]
        tx = content[6]
        rx = content[7]
        pid = "Process0"
        diag = content[5]
        ledger.add_to_ledger(ID, chash, phash, ssn, fname, dob, tx, rx, pid, lname, diag)

def writechain():
    init_chain.write_chain()
# COLLECTION OF UTILITIES USED IN THE CREATION OF THE BLOCK
# AND ADDING TO THE CHAIN

from block import Block # importing object block
import datetime
import ledger
from chain import Chain
import os   # used for clearing the screen and detecting os

def clear():
    """meant to clear the window when an invalid entry is madse"""
    try:
        os.system('clear') # function call to clear the window
    except:
        os.system('clr')

def create_block(data):
    """creates the block object, builds block object, adds data to block, packages block, and then adds to chain"""
    if ledger.check_ledger():  # checks of ledger has a previous transaction
        content = parse_doc(data)   # function called to get the cleaned strings
        next_block(Chain.length(), content)  # call to create new block
    else:
        genesis_block(data) # call to create first block of the chain

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

def genesis_block(content):
    """used to create the original block for the block chain"""
    return Block(0, datetime.datetime.now(), content, "0")

def next_block(prev_block, contents):
    """creates the new block to be added to the chain"""
    previous = prev_block.p_block # gets the hash from the previous block in the chain
    index = prev_block.p_index + 1  # gets and creates the new index for the next block
    stamp = datetime.datetime.now() # time stamps the block for when it was created
    return Block(index, stamp, contents, previous)  # creates the new block
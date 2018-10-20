# Chain class for holding the blocks

import os

class Chain:
    def __init__(self):
        """initialises the chain type to store blocks in"""
        self.index = 0  # keeps index of block in current instance
        self.default_chain = "chain.txt"    # default directory for the chain.txt file
        self.chain = [] # the list that holds the hashes to be solved

    def add_to(self, block):
        """adds a block to the chain"""
        self.chain.append(block)    # appends block to the chain

    def get_hash(self, index):
        return self.chain[index]

    def length(self):
        """returns the length of the chain"""
        return len(self.chain)

    def populate_chain(self):
        """function used to populate the chain with the data from chain.txt"""
        if os.path.exists(self.default_chain):  # checks to make sure that the file exists
            file = open(self.default_chain) # opens the chain.txt
            items = file.read() # reads the file
            items = items.split()   # splits the string into a list
            file.close()
            for item in items:
                self.add_to(item)   # adds items to the chain from the stored chain file
            return 'done'   # returns done when file has been fully parsed
        else:
            return 'emtpy'  # returns empty when the file is not found

    def get_block(self):
        """gets the block current block from the chain"""
        block = self.chain[self.index]  # retrieves the block to have work done
        self.index += 1 # increases the index for when the block is solved
        return block    # returns the block to have work done on it

    def write_chain(self):
        """writes the chain to a txt file for offline storage"""
        save = open(self.default_chain, "w+") # opens the chain.txt file
        chain_string = ''   # accumulator variable to hold the contents of the string to be written
        for block in range(self.index, self.length()):    # loops through the chain
            chain_string += self.chain[block]   # adds the block in the chain to the accumulator variable
        save.write(chain_string)    # writes the string to the chain.txt file for offline storage
        save.close()
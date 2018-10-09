# Chain class for holding the blocks
import os

class Chain:
    def __init__(self):
        """initialises the chain type to store blocks in"""
        self.index = 0
        self.default_chain = ""    # todo determine default directory
        self.chain = []

    def add_to(self, block):
        self.chain.append(block)

    def length(self):
        return len(self.chain)

    def populate_chain(self):
        if os.path.exists(self.default_chain):
            file = open(self.default_chain)
            items = file.read()
            items = items.split()
            file.close()
            for item in items:
                self.add_to(item)
            return 'done'
        else:
            return 'emtpy'

    def get_block(self):
        block = self.chain[self.index]
        self.index += 1
        return block

    def write_chain(self):
        save = open(self.default_chain)
        chain_string = ''
        for block in self.chain:
            chain_string += block
        save.write(chain_string)
        save.close()
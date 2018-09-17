from block import Block
import os
#from chain import Chain

block1 = Block()
while True:
  data_directory = input("enter the directory of the file to be parsed and added to the blockchain:\n")
  if os.path.isfile(data_directory):
    print("valid path")
    break
data  = open(data_directory)
while data.hasNext()
  block1.add_transaction(data.readline())
data.close()
x.print_block()


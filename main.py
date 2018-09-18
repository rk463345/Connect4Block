from block import Block
import time
import os
#from chain import Chain

print("searching for peers")
time.sleep(3)
print("connecting to peers")
time.sleep(5)
print("connected, receiving work")
time.sleep(2)
print("Ledger and work received")
block1 = Block()
block1.add_transaction("my medical records")
block1.package_block()
"""while True:
  data_directory = input("enter the directory of the file to be parsed and added to the blockchain:\n")
  if os.path.isfile(data_directory):
    print("valid path")
    break
with  open(data_directory) as data:
  transactions = data.readlines()
  for line in range(0, len(transactions)):
    block1.add_transaction(line)
data.close()"""
block1.print_block()


from hashlib import sha256
import string
import random
import datetime

def mine_hash(block_hash):
    while True:
        to_hash = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(28))
        crack = sha256()
        crack.update(to_hash)
        print(crack)
        if verify(block_hash, crack):
            time = datetime.time.microsecond
            return to_hash, time

def verify(block_hash, crack_hash):
    if block_hash == crack_hash:
        return True
    else:
        return False

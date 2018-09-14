import hashlib
import socket  # Import socket module
import struct
import sys
import time


def open_and_start(msg):
    # ups = []
    # with open('haveFun.txt', 'r') as hash_file:
    #    ups = hash_file.read().split()
    # f = open('crunch44.txt')
    # print(msg.strip())
    password = msg
    md5hash = 'd3b407ffc9597f4ddb65e7a0ebba0126'
    salt = '0.300202844568092'
    # for password in iter(msg):
    password_hash = salt + password.strip()
    m = hashlib.md5()
    m.update(password_hash.encode('utf-8'))
    password_hash = m.hexdigest()
    if str(password_hash) == md5hash:
        print('Password: ' + password)
        return password
        # f.close()


def main():
    # !/usr/bin/python3           # This is client.py file

    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = '192.168.0.9'
    port = 9999
    # connection to hostname on the port.
    s.connect((host, port))
    # Receive no more than 1024 bytes
    # msg = s.recv(10240)

    while True:
        msg = s.recv(102400000)
        msg = msg.decode('ascii')
        password_list = msg.split()
        for password in password_list:
            result = open_and_start(password)
            if result != None:
                s.send(password.encode('ascii'))
                print("Password: ")
                s.close()
                sys.exit()
            else:
                pass
                # beat = ""
                # s.send(beat.encode('ascii'))
                # print("Attempt: " + password)
                # time.sleep(2)


if __name__ == '__main__':
    main()

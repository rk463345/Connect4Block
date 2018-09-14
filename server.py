import hashlib
import socket
import sys
import time


def open_and_start():
    ups = []
    with open('haveFun.txt', 'r') as hash_file:
        ups = hash_file.read().split()
    f = open('crunch44.txt')
    for password in iter(f):
        password_hash = str(ups[2]) + password.strip()
        m = hashlib.md5()
        m.update(password_hash.encode('utf-8'))
        password_hash = m.hexdigest()
        if str(password_hash) == str(ups[1]): return password
    f.close()


def main():
    listen_for_workers()

    # print('The password is:', open_and_start())


def listen_for_workers():
    # create a socket object
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # serversocket.setsockopt(SO_REUSEADDR, 1)

    # get local machine name
    host = "192.168.0.9"  # socket.gethostname()

    port = 9999

    print(host)
    # bind to the port
    # try:
    serversocket.bind((host, port))
    # except:
    #    time.sleep(100)
    #    serversocket.bind((host, port))

    # queue up to 5 requests
    serversocket.listen(5)

    while True:
        # establish a connection
        clientsocket, addr = serversocket.accept()

        print("Got a connection from %s" % str(addr))

        clientsocket.settimeout(None)
        for password in sys.stdin:
            print(password)
            password = str(password + "\r\n")
            clientsocket.send(password.encode('ascii'))
            '''                                                                                                                                                                                                                                                                                                                
            checkin = clientsocket.recv(1024)                                                                                                                                                                                                                                                                                  
            if not checkin:                                                                                                                                                                                                                                                                                                    
                pass                                                                                                                                                                                                                                                                                                           
            else:                                                                                                                                                                                                                                                                                                              
                print(checkin.decode('ascii'))                                                                                                                                                                                                                                                                                 
                clientsocket.close()                                                                                                                                                                                                                                                                                           
                sys.exit()                                                                                                                                                                                                                                                                                                     
            '''


if __name__ == '__main__':
    main()
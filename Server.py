import socket

# if there is spaces, it is not a new client (new client data should be: "David")
def identifyClient(d):
    for i in range(len(d)):
        if d[i] == ' ':
            return False
    return True

def findClientName(d):
    b = 0
    for i in range(len(d)):
        if d[i] == ':':
            b = i
            break
    return d[:b]


UDP_IP = '0.0.0.0'
UDP_PORT = 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
sock.bind((UDP_IP, UDP_PORT))
clients = {}
while True:
    data, addr = sock.recvfrom(1024)
    # 1. new client, flag == true => new client
    print(f'(*) data received to server: {data.decode()}')


    flag = identifyClient(data.decode())
    if flag:
        print(f'(*) New client Name: {data.decode()}')
        clients[data.decode()] = addr
        print(f'(*) Name: {data.decode()}, address: {addr}')


    # 2. not new client (already exists, and about to send to another client)
    else:
        name = findClientName(data.decode())

        # check if name in clients:
        if name in clients:
            sock.sendto(data, clients[name])
        else:
            sock.sendto(f'There is no user named {name}'.encode(), addr)

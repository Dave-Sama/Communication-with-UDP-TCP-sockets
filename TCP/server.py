import socket
import threading

# step 1
ports = [1, 2, 3, 4, 5]

# step 2
index = int(input('(*) choose index 0-4: '))

# step 3
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
# sock.bind(('0.0.0.0', ports[index]))
sock.bind(('127.0.0.1', ports[index]))
sock.listen(1)


def respond_to_client(conn_socket, client_address):
    print('start listening from', client_address)

    data = conn.recv(1024)
    if client_address[0] == '127.0.0.1':
        conn.send(b'Echo: ' + ' world'.encode())

    print('received from', client_address, 'text', data.decode())
    conn.send(b'Echo: ' + data)


while True:
    try:
        for i in range(len(ports)):
            if i != index:
                sock.connect(('127.0.0.1', ports[i]))  # server ip, port
                print('Connected Successfully!')
                sock.send('hello '.encode())
                reply_data = sock.recv(1024)
                print('server reply:', reply_data.decode())

    except ConnectionRefusedError:
        print('Connection refused Error!')

    # stuck here!!
    conn, client_address = sock.accept()
    print(f'new connection from {client_address}')
    threading.Thread(target=respond_to_client, args=(conn, client_address)).start()

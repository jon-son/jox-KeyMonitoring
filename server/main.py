import socket
ip = input("ip:")
ip_port = (ip,9999)
sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
sk.bind(ip_port)

while True:
    try:
        data = sk.recv(1024)
        print(data.decode())
    except Exception as e:
        print(e)

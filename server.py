import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, aadr = sock.accept()
while True:
    data = conn.recv(1024)
    conn.send(data.upper())
    if data.decode() == "exit":
        break

conn.close()
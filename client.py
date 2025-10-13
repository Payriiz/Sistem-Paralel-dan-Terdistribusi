import socket
server_address = ('localhost', 12345)
SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(server_address)
print("Terhubung ke server. ketik (exit) untuk keluar")

while 1:
    pesan = input("Masukkan pesan: ").strip()

    if not pesan:
        continue
    s.send(pesan.encode('utf-8'))
    
    if pesan == 'exit':
        break

    msg = s.recv(SIZE).decode('utf-8')
    print("Server Balas: ", msg)
s.close()
print("Connection closed.")
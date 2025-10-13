import socket
server_address = ('0.0.0.0', 12345)
SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(server_address)

s.listen(5)

while 1:
    print("Waiting for connection")


    client, client_address = s.accept()
    print("Connection from: ", client_address)
    while 1:
        message = client.recv(SIZE)
        if not message: break
        message = message.decode('utf-8')
        print(f"Pesan Dari Client: {message}")
        
        if (message == "exit"):
            balas = "bye"
            client.send(balas.encode('utf-8'))
            print("Connection closed.")
            break
        
        balas = input("Masukkan Balasan: ").strip()
        if not balas or balas == "exit":
            balas = "Koneksi diputus oleh server"
            client.send(balas.encode('utf-8'))
            print("Connection closed by server.")
            break

        client.send(balas.encode('utf-8'))
        print(f"Balasan dikirim: {balas}")
    client.close()
s.close()
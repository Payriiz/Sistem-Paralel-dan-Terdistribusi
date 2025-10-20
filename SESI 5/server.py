import socket
from threading import Thread

HOST = '0.0.0.0'
PORT = 12345
clients = []

def broadcast(pesan, source):
    for client in clients:
        if client != source:
            try:
                client.send(pesan)
            except:
                remove(client)

def remove(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)
        client_socket.close()

def client_handler(client_socket, addr):
    print(f"[{addr[1]}] Bergabung.")
    
    join_msg = f"[INFO] Client {addr[1]} bergabung!".encode('utf-8')
    broadcast(join_msg, client_socket)

    while True:
        try:
            pesan = client_socket.recv(1024)
            if not pesan:
                break
            
            print(f"[{addr[1]}]: {pesan.decode('utf-8').strip()}")
            
            broadcast_pesan = f"[{addr[1]}] {pesan.decode('utf-8').strip()}".encode('utf-8')
            broadcast(broadcast_pesan, client_socket)
            
        except:
            break
            
    print(f"[{addr[1]}] Keluar.")
    remove(client_socket)

    leave_msg = f"[INFO] Client {addr[1]} keluar.".encode('utf-8')
    broadcast(leave_msg, None)

def main():
    server = socket.socket()
    try:
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"Server berjalan di {HOST}:{PORT}. Menunggu koneksi...")
    except Exception as e:
        print(f"Gagal inisialisasi server: {e}")
        return

    try:
        while True:
            client_socket, addr = server.accept()
            clients.append(client_socket)
            Thread(target=client_handler, args=(client_socket, addr)).start()
    except KeyboardInterrupt:
        print("\nServer dimatikan.")
    except Exception as e:
        print(f"Terjadi error: {e}")
    finally:
        server.close()

if __name__ == '__main__':
    main()
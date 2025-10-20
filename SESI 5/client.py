import socket
from threading import Thread
import sys

HOST = '127.0.0.1'  
PORT = 12345

def terima_pesan(sock):
    while True:
        try:
            pesan = sock.recv(1024).decode('utf-8')
            if not pesan:
                print("\n[DISCONNECTED] Server terputus.")
                break

            print(f"\n{pesan}")
            sys.stdout.write("Anda: ")
            sys.stdout.flush()
            
        except:
            print("\nKoneksi terputus.")
            break

def kirim_pesan(sock):
    while True:
        try:
            pesan = input("Anda: ").strip()
            if pesan.lower() == 'exit':
                break
            if pesan:
                sock.send(pesan.encode('utf-8'))
        except:
            break
    sock.close()

def main():
    client = socket.socket()
    try:
        client.connect((HOST, PORT))
        print(f"Terhubung ke server {HOST}:{PORT}. Ketik 'exit' untuk keluar.")

        t_terima = Thread(target=terima_pesan, args=(client,))
        t_kirim = Thread(target=kirim_pesan, args=(client,))
        
        t_terima.start()
        t_kirim.start()

        t_terima.join()
        t_kirim.join()

    except ConnectionRefusedError:
        print("Gagal terhubung. Pastikan server sudah berjalan.")
    except Exception as e:
        print(f"Terjadi error: {e}")
    finally:
        client.close()
        print("Aplikasi klien ditutup.")

if __name__ == '__main__':
    main()
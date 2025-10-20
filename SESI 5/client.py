import socket
from threading import Thread
import sys

HOST = '127.0.0.1'  # IP Server
PORT = 12345

def terima_pesan(sock):
    """Thread untuk menerima pesan dari server."""
    while True:
        try:
            pesan = sock.recv(1024).decode('utf-8')
            if not pesan:
                print("\n[DISCONNECTED] Server terputus.")
                break
            
            # Tampilkan pesan dan pastikan prompt input muncul lagi
            print(f"\n{pesan}")
            sys.stdout.write("Anda: ")
            sys.stdout.flush()
            
        except:
            print("\nKoneksi terputus.")
            break

def kirim_pesan(sock):
    """Thread untuk mengirim pesan ke server."""
    while True:
        try:
            # Menggunakan input()
            pesan = input("Anda: ").strip()
            if pesan.lower() == 'exit':
                break
            if pesan:
                sock.send(pesan.encode('utf-8'))
        except:
            break
    sock.close()

def main():
    """Inisialisasi koneksi klien."""
    client = socket.socket()
    try:
        client.connect((HOST, PORT))
        print(f"Terhubung ke server {HOST}:{PORT}. Ketik 'exit' untuk keluar.")
        
        # Mulai dua thread: satu untuk terima, satu untuk kirim
        t_terima = Thread(target=terima_pesan, args=(client,))
        t_kirim = Thread(target=kirim_pesan, args=(client,))
        
        t_terima.start()
        t_kirim.start()
        
        # Tunggu thread selesai
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
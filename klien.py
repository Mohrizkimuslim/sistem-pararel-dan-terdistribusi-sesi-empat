import socket
import threading
import sys

IP_SERVER = '192.168.1.21'   # Ganti sesuai IP server kamu
PORT = 65432

def menerima_loop(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("[i] Terputus dari server.")
                break
            print("\n" + data.decode(), end="\n> ")
        except:
            break

def utama():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((IP_SERVER, PORT))
        print(f"[i] Terhubung ke server {IP_SERVER}:{PORT}")
    except Exception as e:
        print(f"[!] Gagal konek ke server: {e}")
        sys.exit(1)

    threading.Thread(target=menerima_loop, args=(sock,), daemon=True).start()

    try:
        while True:
            pesan = input("> ")
            if pesan.lower() in ("keluar", "berhenti"):
                break
            sock.sendall(pesan.encode())
    except KeyboardInterrupt:
        pass
    finally:
        sock.close()
        print("\n[i] Terputus dari server.")

if _name_ == "_main_":
    utama()

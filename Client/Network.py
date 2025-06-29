import socket
import threading
import os


def part_a(): return "".join([chr(c) for c in [76, 105, 99]])  # 'Lic'
def part_b(): return "ense"
def part_c(): return ".key"

def error_prefix(): return "⚠️ "
def error_mid(): return "Unauthorized usage detected."
def error_suffix(): return " Get it legally at: https://github.com/YourRepo"

def assemble_license_file(): return part_a() + part_b() + part_c()

def deploy_roast():
    print(error_prefix() + error_mid() + error_suffix())

class NetworkClient:
    """
    Handles the connection between client and server.
    Manages sending and receiving messages asynchronously.
    """
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None
        self.running = False
        self._integrity_check()

    def _integrity_check(self):
        if not os.path.exists(assemble_license_file()):
            deploy_roast()
            exit()

    def connect(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            self.running = True
            print(f"[+] Connected to {self.host}:{self.port}")
        except Exception as e:
            print(f"[!] Connection failed: {e}")
            self.running = False

    def send(self, message):
        if self.socket and self.running:
            try:
                self.socket.sendall(message.encode())
            except Exception as e:
                print(f"[!] Failed to send message: {e}")
                self.running = False

    def receive_loop(self, callback):
        """
        Starts a thread that listens for incoming messages
        and sends them to the callback.
        """
        def loop():
            while self.running:
                try:
                    data = self.socket.recv(4096).decode()
                    if data:
                        callback("Server", data)
                    else:
                        print("[!] Server closed the connection.")
                        self.running = False
                        break
                except Exception as e:
                    print(f"[!] Receive error: {e}")
                    self.running = False
                    break

        threading.Thread(target=loop, daemon=True).start()

    def disconnect(self):
        self.running = False
        if self.socket:
            try:
                self.socket.close()
                print("[*] Disconnected from server.")
            except:
                pass
import sys
import socket
import threading
import platform

# Optional colors for drama
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    class Fore:
        RED = ''
        YELLOW = ''
        GREEN = ''
        CYAN = ''
        RESET = ''

    class Style:
        RESET_ALL = ''

# ========================
# ==== GUI Detection =====
# ========================
GUI_MODE = None

try:
    from Gui import CyberChatClientGUI, Communicator
    GUI_MODE = "PyQt6"
except ImportError as e:
    print(Fore.RED + "[!] PyQt6 GUI failed to load:", str(e))
    try:
        from tkinter import Tk, Text, Entry, Scrollbar, END, Button, BOTH, RIGHT, LEFT, Y
        GUI_MODE = "Tkinter"
    except ImportError as e:
        print(Fore.RED + "[!] Tkinter GUI failed to load:", str(e))
        GUI_MODE = None

# ===========================
# ==== Networking Client ====
# ===========================
class ChatClient:
    def __init__(self, host, port, username):
        self.server_addr = (host, port)
        self.username = username
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.socket.connect(self.server_addr)
            print(Fore.GREEN + f"[+] Connected to {self.server_addr[0]}:{self.server_addr[1]}")
            # Send username to server immediately after connecting
            self.socket.send(self.username.encode())
        except Exception as e:
            print(Fore.RED + f"[!] Connection failed: {e}")
            sys.exit(1)

    def send(self, msg):
        try:
            self.socket.send(msg.encode())
        except Exception:
            print(Fore.RED + "[-] Failed to send message.")

    def receive_loop(self, callback):
        while True:
            try:
                data = self.socket.recv(4096).decode()
                if not data:
                    break
                callback(data)
            except:
                break

# ==============================
# ==== Tkinter Fallback GUI ====
# ==============================
if GUI_MODE == "Tkinter":
    class TkinterClient:
        def __init__(self, client):
            self.client = client
            self.window = Tk()
            self.window.title("RealityPatch V1 - CyberChat (Tkinter)")
            self.window.configure(bg="#0d0d0d")

            self.chat_area = Text(self.window, bg="#0d0d0d", fg="#00FF00", insertbackground="white")
            self.chat_area.pack(side=LEFT, fill=BOTH, expand=True)

            scrollbar = Scrollbar(self.window, command=self.chat_area.yview)
            scrollbar.pack(side=RIGHT, fill=Y)
            self.chat_area['yscrollcommand'] = scrollbar.set

            self.input_field = Entry(self.window, bg="#1a1a1a", fg="#00FF00")
            self.input_field.pack(fill=BOTH)
            self.input_field.bind("<Return>", self.send_message)

            send_button = Button(self.window, text="Send", command=self.send_message, bg="#262626", fg="#00FF00")
            send_button.pack(fill=BOTH)

            self.client.receive_loop(self.display_message)

        def send_message(self, event=None):
            msg = self.input_field.get()
            if msg:
                self.client.send(msg)
                self.display_message(f"You: {msg}")
                self.input_field.delete(0, END)

        def display_message(self, msg):
            self.chat_area.insert(END, msg + "\n")
            self.chat_area.see(END)

        def run(self):
            self.window.mainloop()


# ====================================
# ========= Terminal CLI Mode =========
# ====================================
def cli_mode(client):
    def handle_incoming(msg):
        print(msg)

    threading.Thread(target=client.receive_loop, args=(handle_incoming,), daemon=True).start()

    while True:
        try:
            msg = input("> ")
            if msg.lower() in ["exit", "quit"]:
                break
            client.send(msg)
        except KeyboardInterrupt:
            break

    print(Fore.CYAN + "[*] Disconnected.")
    client.socket.close()

# =================================
# =========== Main ================
# =================================
if __name__ == "__main__":
    print(Fore.CYAN + "=== RealityPatch V1 - CyberChat Client ===\n")

    host = input("[?] Server address (Ngrok URL or LAN IP): ").strip()
    port = int(input("[?] Port (e.g. 12345): ").strip())
    username = input("[?] Enter a nickname (visible to admin): ").strip()

    if not username:
        print(Fore.RED + "[!] Username cannot be empty.")
        sys.exit(1)

    client = ChatClient(host, port, username)
    client.connect()

    if GUI_MODE == "PyQt6":
        print(Fore.GREEN + "[*] Launching PyQt6 GUI...\n")
        app = Communicator(client)
        app.run()

    elif GUI_MODE == "Tkinter":
        print(Fore.YELLOW + "[*] PyQt6 unavailable. Running Tkinter GUI...\n")
        tk_app = TkinterClient(client)
        tk_app.run()

    else:
        print(Fore.RED + "[!] GUI unavailable. Switching to Terminal CLI mode...\n")
        cli_mode(client)
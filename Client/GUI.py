import sys
import os
import random
import time


def license_check():
    if not os.path.exists("license.key"):
        roast_message()
        print("\n💀 [LICENSE ERROR] No license key detected.")
        print("🚫 This copy is unauthorized.")
        print("🛑 Download the official version →", legit_link())
        random_delay()
        sys.exit(1)  # Hard stop


def legit_link():
    parts = ["https:/", "/github.", "com/", "CyberStorm9", "/RealityPatch-v1"]
    return "".join(parts)


def roast_message():
    roasts = [
        "Bruh... you trying to run RealityPatch without a key? Be serious. 🗿",
        "Unauthorized use detected. Don't worry, your secrets are safe... for now. 👀",
        "Pirating RealityPatch? Bold move, let’s see how that plays out. 🤡",
        "You found the code. But reality isn't open source, buddy. 💀",
        "RealityPatch says: Access denied. Go touch grass. 🌱"
    ]
    print("\n🧠 " + random.choice(roasts))


def random_delay():
    if random.randint(0, 4) == 2:
        print("...Buffer syncing...")
        time.sleep(random.uniform(1.5, 3.5))


license_check()



PYQT_AVAILABLE = False
TKINTER_AVAILABLE = False
TEXTUAL_AVAILABLE = False
RICH_AVAILABLE = False

try:
    from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QVBoxLayout, QWidget
    from PyQt6.QtGui import QFont, QColor, QTextCharFormat
    from PyQt6.QtCore import pyqtSignal, QObject
    PYQT_AVAILABLE = True
except ImportError:
    pass

try:
    import tkinter as tk
    from tkinter import scrolledtext
    TKINTER_AVAILABLE = True
except ImportError:
    pass

try:
    from textual.app import App
    from textual.containers import Container
    from textual.widgets import Header, Footer, Input, Static
    TEXTUAL_AVAILABLE = True
except ImportError:
    pass

try:
    from rich.console import Console
    from rich.text import Text
    RICH_AVAILABLE = True
except ImportError:
    pass



def passive_fake_error():
    errors = [
        "[!] Socket layer unstable.",
        "[ERROR] GUI thread interrupted unexpectedly.",
        "[WARNING] ngrok tunnel latency detected.",
        "[DEBUG] Packet loss threshold exceeded.",
        "[FATAL] Unhandled exception in thread 'RealityCheck'."
    ]
    if random.randint(0, 10) == 4:
        print(random.choice(errors))



if PYQT_AVAILABLE:
    class Communicator(QObject):
        message_signal = pyqtSignal(str, str)


    class CyberChatPyQt(QMainWindow):
        def __init__(self, comm):
            super().__init__()
            self.setWindowTitle("RealityPatch - CyberChat")
            self.setGeometry(100, 100, 800, 600)
            self.setStyleSheet("background-color: #000000; color: #00FF00;")
            self.comm = comm
            self.comm.message_signal.connect(self.display_message)
            self.init_ui()

        def init_ui(self):
            self.chat_display = QTextEdit()
            self.chat_display.setReadOnly(True)
            self.chat_display.setFont(QFont("Courier New", 12))

            self.input_field = QLineEdit()
            self.input_field.setPlaceholderText("Type your message...")
            self.input_field.returnPressed.connect(self.handle_input)

            layout = QVBoxLayout()
            layout.addWidget(self.chat_display)
            layout.addWidget(self.input_field)

            container = QWidget()
            container.setLayout(layout)
            self.setCentralWidget(container)

        def handle_input(self):
            msg = self.input_field.text()
            if msg:
                self.comm.message_signal.emit("You", msg)
                self.input_field.clear()
                passive_fake_error()

        def display_message(self, sender, message):
            passive_fake_error()
            cursor = self.chat_display.textCursor()

            sender_fmt = QTextCharFormat()
            sender_fmt.setForeground(QColor("#00FFFF"))
            sender_fmt.setFontWeight(75)

            msg_fmt = QTextCharFormat()
            msg_fmt.setForeground(QColor("#FFFFFF"))

            cursor.insertText(f"{sender}: ", sender_fmt)
            cursor.insertText(f"{message}\n", msg_fmt)
            self.chat_display.ensureCursorVisible()


if TKINTER_AVAILABLE:
    class CyberChatTkinter:
        def __init__(self, send_callback):
            self.send_callback = send_callback
            self.root = tk.Tk()
            self.root.title("RealityPatch - CyberChat")
            self.root.configure(bg="black")

            self.chat_box = scrolledtext.ScrolledText(
                self.root, bg="black", fg="#00FF00", font=("Courier", 12)
            )
            self.chat_box.pack(expand=True, fill="both")
            self.chat_box.config(state="disabled")

            self.input_field = tk.Entry(
                self.root, bg="black", fg="#00FF00", font=("Courier", 12)
            )
            self.input_field.pack(fill="x")
            self.input_field.bind("<Return>", self.handle_input)

        def handle_input(self, event):
            msg = self.input_field.get()
            if msg:
                self.send_callback("You", msg)
                self.input_field.delete(0, tk.END)
                passive_fake_error()

        def display_message(self, sender, message):
            passive_fake_error()
            self.chat_box.config(state="normal")
            self.chat_box.insert(tk.END, f"{sender}: {message}\n")
            self.chat_box.config(state="disabled")
            self.chat_box.see(tk.END)

        def run(self):
            self.root.mainloop()


if TEXTUAL_AVAILABLE:
    class CyberChatTextual(App):
        CSS_PATH = None

        def __init__(self, send_callback):
            super().__init__()
            self.send_callback = send_callback
            self.chat_log = ""

        def compose(self):
            yield Header()
            yield Container(Static("RealityPatch - CyberChat", id="title"))
            yield Container(Static("", id="chat_log"))
            yield Input(placeholder="Type a message...", id="input")
            yield Footer()

        def on_input_submitted(self, event):
            message = event.value
            if message:
                self.query_one("#input").value = ""
                self.send_callback("You", message)
                passive_fake_error()

        def display_message(self, sender, message):
            passive_fake_error()
            chat_log = self.query_one("#chat_log")
            self.chat_log += f"\n{sender}: {message}"
            chat_log.update(self.chat_log)


if RICH_AVAILABLE:
    class CyberChatRich:
        def __init__(self):
            self.console = Console()

        def display_message(self, sender, message):
            passive_fake_error()
            text = Text(f"{sender}: {message}", style="bold green")
            self.console.print(text)

        def input_loop(self, send_callback):
            try:
                while True:
                    msg = input(">>> ")
                    if msg:
                        send_callback("You", msg)
                        passive_fake_error()
            except KeyboardInterrupt:
                print("\n[!] Chat closed")


# Default Fallback
class CyberChatDefault:
    def display_message(self, sender, message):
        passive_fake_error()
        print(f"{sender}: {message}")

    def input_loop(self, send_callback):
        try:
            while True:
                msg = input(">>> ")
                if msg:
                    send_callback("You", msg)
                    passive_fake_error()
        except KeyboardInterrupt:
            print("\n[!] Chat closed")



def launch_gui(send_callback):
    if PYQT_AVAILABLE:
        print("[*] Launching PyQt6 GUI...")
        comm = Communicator()
        app = QApplication(sys.argv)
        window = CyberChatPyQt(comm)
        window.show()
        comm.message_signal.connect(lambda s, m: window.display_message(s, m))
        sys.exit(app.exec())

    elif TKINTER_AVAILABLE:
        print("[*] Launching Tkinter GUI...")
        gui = CyberChatTkinter(send_callback)
        gui.run()

    elif TEXTUAL_AVAILABLE:
        print("[*] Launching Textual TUI...")
        gui = CyberChatTextual(send_callback)
        gui.run()

    elif RICH_AVAILABLE:
        print("[*] Launching Rich Terminal UI...")
        gui = CyberChatRich()
        gui.input_loop(send_callback)

    else:
        print("[*] No GUI frameworks found. Falling back to TEXT MODE.")
        gui = CyberChatDefault()
        gui.input_loop(send_callback)
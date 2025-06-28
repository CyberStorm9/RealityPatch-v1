# GUI.py
try:
    from PyQt6.QtWidgets import (
        QApplication, QMainWindow, QTextEdit, QLineEdit, QVBoxLayout, QWidget
    )
    from PyQt6.QtGui import QFont, QColor, QTextCharFormat
    from PyQt6.QtCore import Qt, pyqtSignal, QObject
    GUI_MODE = "pyqt6"
except ImportError:
    try:
        import tkinter as tk
        from tkinter import scrolledtext
        GUI_MODE = "tkinter"
    except ImportError:
        GUI_MODE = "terminal"


# ===== PyQt6 GUI =====
if GUI_MODE == "pyqt6":
    class Communicator(QObject):
        message_signal = pyqtSignal(str, str)


    class CyberChatClientGUI(QMainWindow):
        def __init__(self, communicator):
            super().__init__()
            self.setWindowTitle("RealityPatch V1 - CyberChat")
            self.setGeometry(100, 100, 800, 600)
            self.setStyleSheet("background-color: #0d0d0d; color: #00ff00;")

            self.comm = communicator
            self.comm.message_signal.connect(self.display_message)
            self.init_ui()

        def init_ui(self):
            self.chat_display = QTextEdit()
            self.chat_display.setReadOnly(True)
            self.chat_display.setFont(QFont("Courier New", 12))

            self.input_field = QLineEdit()
            self.input_field.setPlaceholderText("Enter message...")
            self.input_field.returnPressed.connect(self.handle_input)

            layout = QVBoxLayout()
            layout.addWidget(self.chat_display)
            layout.addWidget(self.input_field)

            container = QWidget()
            container.setLayout(layout)
            self.setCentralWidget(container)

        def handle_input(self):
            message = self.input_field.text().strip()
            if message:
                self.comm.message_signal.emit("You", message)
                self.input_field.clear()

        def display_message(self, sender, message):
            cursor = self.chat_display.textCursor()

            sender_fmt = QTextCharFormat()
            sender_fmt.setForeground(QColor("#00ffff"))
            sender_fmt.setFontWeight(75)

            msg_fmt = QTextCharFormat()
            msg_fmt.setForeground(QColor("#ffffff"))

            cursor.insertText(f"{sender}: ", sender_fmt)
            cursor.insertText(f"{message}\n", msg_fmt)
            self.chat_display.ensureCursorVisible()

# ===== Tkinter GUI =====
elif GUI_MODE == "tkinter":
    class Communicator:
        """Basic communicator for Tkinter"""
        def __init__(self):
            self.message_signal = None


    class CyberChatTkinterGUI:
        def __init__(self, communicator):
            self.comm = communicator
            self.root = tk.Tk()
            self.root.title("RealityPatch - CyberChat (Tkinter Fallback)")
            self.root.configure(bg="#0d0d0d")

            self.chat_display = scrolledtext.ScrolledText(
                self.root, bg="#1a1a1a", fg="#00ff00", font=("Courier", 12)
            )
            self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
            self.chat_display.config(state=tk.DISABLED)

            self.input_field = tk.Entry(
                self.root, bg="#333333", fg="#00ff00", font=("Courier", 12)
            )
            self.input_field.pack(padx=10, pady=10, fill=tk.X)
            self.input_field.bind("<Return>", self.handle_input)

            self.comm.message_signal = self.display_message

        def handle_input(self, event=None):
            message = self.input_field.get().strip()
            if message:
                self.comm.message_signal("You", message)
                self.input_field.delete(0, tk.END)

        def display_message(self, sender, message):
            self.chat_display.config(state=tk.NORMAL)
            self.chat_display.insert(tk.END, f"{sender}: {message}\n")
            self.chat_display.yview(tk.END)
            self.chat_display.config(state=tk.DISABLED)

        def run(self):
            self.root.mainloop()


# ===== Terminal Mode Placeholder =====
else:
    class Communicator:
        """Dummy communicator for terminal mode"""
        def __init__(self):
            self.message_signal = None

    # Terminal mode handled directly in client.py
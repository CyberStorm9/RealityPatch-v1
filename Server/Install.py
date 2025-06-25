import os
import sys
import subprocess
from pathlib import Path
from colorama import Fore, Style, init
import shutil

# Init colorama
init(autoreset=True)

# ==========================
# Required Python Libraries
# ==========================
REQUIREMENTS = [
    "pyngrok>=6.0.0",
    "colorama>=0.4.0"
]

# ==========================
# Install Python Dependencies
# ==========================
def run_command(cmd):
    try:
        subprocess.check_call(cmd, shell=True)
        return True
    except subprocess.CalledProcessError:
        return False

def install_dependencies():
    print(Fore.CYAN + "[*] Installing Python dependencies...\n")
    for package in REQUIREMENTS:
        print(Fore.YELLOW + f"  ├─ Installing {package}...")
        if run_command(f"{sys.executable} -m pip install {package}"):
            print(Fore.GREEN + f"  │   ✔ {package} installed.")
        else:
            print(Fore.RED + f"  │   ✘ Failed to install {package}.\n")

# ==========================
# Check ngrok Installation
# ==========================
def setup_ngrok():
    print(Fore.CYAN + "\n[*] Checking ngrok setup...")

    if not shutil.which("ngrok"):
        print(Fore.RED + "  ✘ ngrok not found on this system.")
        print(Fore.YELLOW + "  → Download it from: https://ngrok.com/download")
        print(Fore.YELLOW + "  → Unzip it and place it in a directory in your PATH")
        print(Fore.YELLOW + "  → Or simply place ngrok.exe next to this script")
    else:
        print(Fore.GREEN + "  ✔ ngrok is installed and ready.")

    input(Fore.CYAN + "\n[*] Have your ngrok auth token ready.\n    → If not, get it at: https://dashboard.ngrok.com/get-started/your-authtoken\n    → Press Enter to continue...")

# ==========================
# Optional Firewall Setup
# ==========================
def setup_firewall():
    print(Fore.CYAN + "\n[*] Configuring firewall (if needed)...")

    platform = sys.platform

    if platform.startswith("linux"):
        print(Fore.YELLOW + "  ├─ Allowing TCP port 5000 via ufw (if installed)...")
        run_command("sudo ufw allow 5000/tcp")
    elif platform == "darwin":
        print(Fore.YELLOW + "  ├─ macOS detected. Configure firewall manually if needed.")
    elif platform == "win32":
        print(Fore.YELLOW + "  ├─ Windows detected. Skipping firewall auto-config. Do it manually if needed.")
    else:
        print(Fore.RED + "  ├─ Unknown OS. Skipping firewall config.")

# ==========================
# Final Summary
# ==========================
def summary():
    print(Fore.MAGENTA + "\n[+] Setup complete.")
    print(Fore.GREEN + "[*] Run the server with:")
    print(Fore.YELLOW + "    python server.py")
    print(Fore.CYAN + "[*] You'll be prompted to enter your ngrok auth token at runtime if not set.")

# ==========================
# Main
# ==========================
if __name__ == "__main__":
    try:
        install_dependencies()
        setup_ngrok()
        setup_firewall()
        summary()
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Installation interrupted by user.")
        sys.exit(1)
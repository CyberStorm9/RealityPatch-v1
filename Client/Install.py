import os
import sys
import subprocess
import platform
from time import sleep

REQUIREMENTS = [
    'PyQt6>=6.4.0',
    'colorama>=0.4.6'
]

def run_command(command):
    """Run system command and handle errors."""
    try:
        result = subprocess.run(command, check=True, shell=True)
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False

def check_python():
    """Ensure Python version is sufficient."""
    if sys.version_info < (3, 7):
        print("[!] Python 3.7 or higher is required.")
        sys.exit(1)

def install_packages():
    """Install all required Python packages."""
    print("[*] Installing dependencies...\n")
    for pkg in REQUIREMENTS:
        print(f" -> Installing {pkg}...")
        success = run_command(f"{sys.executable} -m pip install --upgrade {pkg}")
        if success:
            print(f"    [+] {pkg} installed successfully.\n")
        else:
            print(f"    [!] Failed to install {pkg}. Check your internet or pip setup.\n")

def pip_check():
    """Check if pip exists."""
    print("[*] Checking pip...")
    if not run_command(f"{sys.executable} -m pip --version"):
        print("[!] Pip not found. Trying to install pip...")
        get_pip = "https://bootstrap.pypa.io/get-pip.py"
        run_command(f"curl {get_pip} -o get-pip.py")
        run_command(f"{sys.executable} get-pip.py")
        os.remove("get-pip.py")
        if not run_command(f"{sys.executable} -m pip --version"):
            print("[!] Pip installation failed. Install pip manually and rerun this.")
            sys.exit(1)
        else:
            print("[+] Pip installed successfully.\n")
    else:
        print("[+] Pip is working.\n")

def summary():
    print("\n[+] Setup complete.")
    print("[*] Run with: python client.py")
    print("[*] RealityPatch V1 CyberChat is ready to launch.\n")

if __name__ == "__main__":
    try:
        check_python()
        pip_check()
        install_packages()
        summary()
    except KeyboardInterrupt:
        print("\n[!] Install cancelled by user.")
        sys.exit(0)
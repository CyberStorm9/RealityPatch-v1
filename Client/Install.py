import os
import sys
import subprocess
import platform
from time import sleep


# ========================
# 📦 REQUIRED PACKAGES
# ========================
REQUIREMENTS = [
    'PyQt6>=6.4.0',         # GUI Primary
    'tk',                   # GUI Fallback (Usually comes with Python)
    'textual>=0.43.0',      # Text-based GUI fallback
    'rich>=13.0.0',         # Terminal GUI fallback
    'colorama>=0.4.6',      # Colored outputs
    

# ========================
# ✅ FUNCTIONS
# ========================

def run_command(command):
    """Run system command and handle errors."""
    try:
        result = subprocess.run(command, check=True, shell=True)
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False


def check_python():
    """Ensure Python version is 3.7+."""
    print("[*] Checking Python version...")
    if sys.version_info < (3, 7):
        print("[!] Python 3.7 or higher is required.")
        sys.exit(1)
    print("[+] Python version OK.\n")


def pip_check():
    """Ensure pip is installed."""
    print("[*] Checking pip...")
    if not run_command(f"{sys.executable} -m pip --version"):
        print("[!] Pip not found. Trying to install pip...")
        get_pip = "https://bootstrap.pypa.io/get-pip.py"
        run_command(f"curl {get_pip} -o get-pip.py" if platform.system() != "Windows"
                    else f"powershell -Command Invoke-WebRequest -Uri {get_pip} -OutFile get-pip.py")
        run_command(f"{sys.executable} get-pip.py")
        os.remove("get-pip.py")
        if not run_command(f"{sys.executable} -m pip --version"):
            print("[!] Pip installation failed. Install pip manually.")
            sys.exit(1)
        else:
            print("[+] Pip installed successfully.\n")
    else:
        print("[+] Pip is working fine.\n")


def install_packages():
    """Install required Python libraries."""
    print("[*] Installing dependencies...\n")
    for pkg in REQUIREMENTS:
        print(f" -> Installing {pkg}...")
        success = run_command(f"{sys.executable} -m pip install --upgrade {pkg}")
        if success:
            print(f"    [+] {pkg} installed successfully.\n")
        else:
            print(f"    [!] Failed to install {pkg}. Check your internet or pip setup.\n")


def setup_firewall():
    """Check if any firewall setting needs to be adjusted."""
    print("[*] Checking firewall (optional step)...")
    system = platform.system()

    if system == "Linux":
        print("[*] Linux detected. If using UFW, allow your port manually if needed.")
    elif system == "Windows":
        print("[*] Windows detected. Check Windows Defender Firewall for any blocks.")
    elif system == "Darwin":
        print("[*] macOS detected. You may need to allow Python connections in firewall settings.")
    else:
        print("[!] Unknown OS. Manual firewall setup might be needed.")


def summary():
    print("\n============================================")
    print("[+] Setup complete. All systems GO.")
    print("[*] Run with: python client.py")
    print("[*] RealityPatch V1 CyberChat ready to launch.")
    print("============================================\n")


# ========================
# 🚀 MAIN EXECUTION
# ========================

if __name__ == "__main__":
    try:
        check_python()
        pip_check()
        install_packages()
        setup_firewall()
        summary()
    except KeyboardInterrupt:
        print("\n[!] Install cancelled by user.")
        sys.exit(0)
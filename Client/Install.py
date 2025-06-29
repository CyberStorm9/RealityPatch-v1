import os
import sys
import subprocess
import platform
import random
from time import sleep


def license_check():
    messages = [
        "\n💀 [LICENSE ERROR] No license key detected. Did you think this was original?",
        "🚫 This ain't a soup kitchen. License, please.",
        "🛑 Attempting to run RealityPatch without a license... That's cute.",
        "🤡 You forgot the license.key... or maybe forgot your brain.",
        "📜 Where is the sacred license.key? Offering invalid. GTFO."
    ]

    if not os.path.exists("license.key"):
        msg = random.choice(messages)
        print(msg)
        print("\n👉 Download the official version → https://github.com/CyberStorm9/RealityPatch-v1")
        sleep(1.5)
        for i in range(3, 0, -1):
            print(f"   Closing in {i}...")
            sleep(0.7)
        sys.exit(99)  # Ultimate disrespect
    else:
        print("[✔] License detected. You may proceed... mortal.\n")



REQUIREMENTS = [
    'PyQt6>=6.4.0',
    'tk',
    'textual>=0.43.0',
    'rich>=13.0.0',
    'colorama>=0.4.6',
    'pyngrok>=5.0.5'
]




def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
        return True
    except subprocess.CalledProcessError:
        return False


def check_python():
    print("[*] Checking Python version...")
    if sys.version_info < (3, 7):
        print("[!] Python 3.7+ is mandatory. Not negotiable.")
        sys.exit(1)
    print("[+] Python version is acceptable. For now.\n")


def pip_check():
    print("[*] Checking pip...")
    if not run_command(f"{sys.executable} -m pip --version"):
        print("[!] Pip not found. Did you install Python from a cereal box?")
        get_pip = "https://bootstrap.pypa.io/get-pip.py"
        downloader = (
            f"curl {get_pip} -o get-pip.py"
            if platform.system() != "Windows"
            else f"powershell -Command Invoke-WebRequest -Uri {get_pip} -OutFile get-pip.py"
        )
        run_command(downloader)
        run_command(f"{sys.executable} get-pip.py")
        os.remove("get-pip.py")

        if not run_command(f"{sys.executable} -m pip --version"):
            print("[!] Pip installation failed. This is why aliens don’t visit us.")
            sys.exit(1)
        else:
            print("[+] Pip installed. Miracles do happen.\n")
    else:
        print("[+] Pip is operational.\n")


def install_packages():
    print("[*] Installing dependencies like a responsible hacker...\n")
    failures = []
    for pkg in REQUIREMENTS:
        print(f" → Installing {pkg}...")
        if run_command(f"{sys.executable} -m pip install --upgrade {pkg}"):
            print(f"    [+] {pkg} installed successfully.\n")
        else:
            print(f"    [!] Failed to install {pkg}. Bro, do you even internet?\n")
            failures.append(pkg)

    if failures:
        print("\n[!!!] The following packages failed to install:")
        for fail in failures:
            print(f" - {fail}")
        print("Fix your internet, then try again.\n")
        sys.exit(2)


def setup_firewall():
    print("[*] Checking firewall (optional but wise)...")
    system = platform.system()

    if system == "Linux":
        print("[*] Linux detected. If you're running ufw:")
        print("    sudo ufw allow <your-port>")
    elif system == "Windows":
        print("[*] Windows detected. Check Windows Defender Firewall for 'Python' rules.")
    elif system == "Darwin":
        print("[*] macOS detected. Let Python through the firewall if it cries.")
    else:
        print("[!] Unknown OS. You're probably cursed. Manual firewall setup might be needed.\n")


def summary():
    print("\n==============================================")
    print("[+] Setup complete. Apocalypse postponed.")
    print("[*] Run the client with: python client.py")
    print("[*] Run the server with: python server.py")
    print("[*] RealityPatch V1 CyberChat is now live.")
    print("==============================================\n")



if __name__ == "__main__":
    try:
        print("=======================================")
        print("   ⚡ RealityPatch Installer ⚡")
        print("      Version: CHAOS Protocol")
        print("=======================================\n")

        license_check()
        check_python()
        pip_check()
        install_packages()
        setup_firewall()
        summary()

    except KeyboardInterrupt:
        print("\n[!] Install cancelled by user. Coward.")
        sys.exit(0)
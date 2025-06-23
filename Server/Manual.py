import os
import platform
import sys
from time import sleep

# Color codes for cross-platform compatibility
if platform.system() == "Windows":
    import colorama
    colorama.init()
    COLOR_RED = colorama.Fore.RED
    COLOR_GREEN = colorama.Fore.GREEN
    COLOR_YELLOW = colorama.Fore.YELLOW
    COLOR_BLUE = colorama.Fore.BLUE
    COLOR_RESET = colorama.Style.RESET_ALL
else:
    COLOR_RED = '\033[91m'
    COLOR_GREEN = '\033[92m'
    COLOR_YELLOW = '\033[93m'
    COLOR_BLUE = '\033[94m'
    COLOR_RESET = '\033[0m'

def print_section(title, content):
    """Print a section with formatted title and content"""
    print(f"\n{COLOR_YELLOW}=== {title} ===")
    print(COLOR_RESET + content)

def print_step(number, text):
    """Print a numbered step"""
    print(f"\n{COLOR_BLUE}Step {number}:{COLOR_RESET} {text}")

def print_command(cmd):
    """Print a command in a special format"""
    print(f"\n{COLOR_GREEN}┌───[{COLOR_YELLOW}COMMAND{COLOR_GREEN}]───")
    print(f"{COLOR_GREEN}│{COLOR_RESET} {cmd}")
    print(f"{COLOR_GREEN}└──────────────────{COLOR_RESET}")

def print_warning(text):
    """Print a warning message"""
    print(f"\n{COLOR_RED}⚠️ WARNING: {text}{COLOR_RESET}")

def print_info(text):
    """Print informational text"""
    print(f"\n{COLOR_BLUE}ℹ️ {text}{COLOR_RESET}")

def clear_screen():
    """Clear the terminal screen"""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def display_manual():
    """Display the comprehensive manual"""
    clear_screen()
    
    # Header
    print(f"{COLOR_GREEN}==========================================")
    print(f" TERMINAL CHAT SERVER - INTERACTIVE MANUAL ")
    print(f"=========================================={COLOR_RESET}")
    
    # Table of Contents
    print(f"\n{COLOR_YELLOW}TABLE OF CONTENTS:{COLOR_RESET}")
    print("1. Installation")
    print("2. Getting ngrok Auth Token")
    print("3. Starting the Server")
    print("4. Admin Privileges")
    print("5. Connecting Clients")
    print("6. Security Features")
    print("7. Troubleshooting")
    print("8. Manual ngrok Setup")
    print("9. Notes")
    print(f"\n{COLOR_YELLOW}Type 'exit' at any time to quit the manual{COLOR_RESET}")
    
    # Wait for user to continue
    input("\nPress Enter to continue...")
    
    # Installation
    clear_screen()
    print_section("1. INSTALLATION", "How to set up the chat server")
    print_step(1, "Run the install script:")
    print_command("python install.py")
    print("\nThis will:")
    print("- Install required Python packages (pyngrok, colorama)")
    print("- Attempt to download and configure ngrok")
    print("- Add ngrok to your system PATH")
    print_step(2, "Manual ngrok Installation (if automated fails):")
    print("- Download ngrok from https://ngrok.com/download")
    print("- Choose the correct version for your OS")
    print("- Unzip the file")
    print("- Move ngrok to a directory in your PATH:")
    print("  Windows: C:\\Windows or add to system PATH")
    print("  Mac/Linux: /usr/local/bin or ~/bin")
    
    if input("\nContinue? (y/n): ").lower() != 'y':
        return
    
    # Getting ngrok Auth Token
    clear_screen()
    print_section("2. GETTING NGROK AUTH TOKEN", "Essential for secure tunneling")
    print_step(1, "Create a free account at https://ngrok.com/signup")
    print_step(2, "Login to dashboard: https://dashboard.ngrok.com")
    print_step(3, "Get your authtoken: https://dashboard.ngrok.com/get-started/your-authtoken")
    print("\nYour token will look like:")
    print_command("2AbCdeFGHijklmnOpQRSTuvwxYZ12345678Abcd")
    print_warning("Keep this token secure - it gives access to your ngrok account")
    
    if input("\nContinue? (y/n): ").lower() != 'y':
        return
    
    # Starting the Server
    clear_screen()
    print_section("3. STARTING THE SERVER", "Launching your chat server")
    print_step(1, "Run the server script:")
    print_command("python server.py")
    print_step(2, "Enter port number (e.g., 12345)")
    print_step(3, "When asked, enter your ngrok auth token")
    print("\nThe server will display:")
    print("- Local connection info (127.0.0.1:PORT)")
    print("- Ngrok public URL (if enabled)")
    print("- Admin authentication token")
    print_info("Save the admin token - first user to enter it becomes admin")
    
    if input("\nContinue? (y/n): ").lower() != 'y':
        return
    
    # Admin Privileges
    clear_screen()
    print_section("4. ADMIN PRIVILEGES", "Managing your chat server")
    print("The first client to connect with the admin token becomes the server admin.")
    print("\nAdmin commands:")
    print_command("::ban <IP>          - Ban an IP address")
    print_command("::warn <IP> <msg>   - Send warning to specific user")
    print_command("::kick <IP>         - Kick user from server")
    print_command("::clear             - Clear chat for all users")
    print("\nExample usage:")
    print_command("::warn 192.168.1.5 Stop spamming!")
    print_warning("IP addresses must match exactly")
    
    if input("\nContinue? (y/n): ").lower() != 'y':
        return
    
    # Connecting Clients
    clear_screen()
    print_section("5. CONNECTING CLIENTS", "Joining the chat")
    print_step(1, "Share the connection details:")
    print("- Ngrok URL (recommended for remote connections)")
    print("- Local IP:PORT (for LAN connections)")
    print_step(2, "Clients run the client script:")
    print_command("python client.py")
    print("\nClient workflow:")
    print("- Enter server address and port")
    print("- If prompted, enter admin token (first user only)")
    print("- Start chatting!")
    print_info("For remote connections, use the ngrok URL in format: HOST:PORT")
    
    if input("\nContinue? (y/n): ").lower() != 'y':
        return
    
    # Security Features
    clear_screen()
    print_section("6. SECURITY FEATURES", "Protecting your server")
    print("- Server self-destructs when stopped")
    print("- All connections terminated immediately")
    print("- Admin token randomly generated on each start")
    print("- Banned IPs stored in memory only")
    print("- Ngrok tunnels automatically closed")
    print("- Ephemeral data storage (nothing saved to disk)")
    print_warning("Always use ngrok with auth token for secure tunneling")
    
    if input("\nContinue? (y/n): ").lower() != 'y':
        return
    
    # Troubleshooting
    clear_screen()
    print_section("7. TROUBLESHOOTING", "Solving common problems")
    
    print(f"\n{COLOR_YELLOW}Q: Ngrok tunnel fails to create{COLOR_RESET}")
    print("A: 1. Verify your auth token")
    print("   2. Check firewall settings:")
    print("      Windows: Allow ngrok through firewall")
    print("      Mac/Linux: Ensure port is accessible")
    print("   3. Test ngrok manually:")
    print_command("ngrok tcp <port>")
    
    print(f"\n{COLOR_YELLOW}Q: 'ngrok command not found'{COLOR_RESET}")
    print("A: 1. Ensure ngrok is installed correctly")
    print("   2. Verify ngrok is in your PATH")
    print("   3. Restart your terminal after installation")
    
    print(f"\n{COLOR_YELLOW}Q: Clients can't connect{COLOR_RESET}")
    print("A: 1. Verify server is running")
    print("   2. Check port forwarding (for local connections)")
    print("   3. Use ngrok for easier remote access")
    
    print(f"\n{COLOR_YELLOW}Q: Admin commands not working{COLOR_RESET}")
    print("A: 1. Verify you entered the admin token first")
    print("   2. Commands must start with ::")
    print("   3. IP addresses must match exactly")
    
    if input("\nContinue? (y/n): ").lower() != 'y':
        return
    
    # Manual ngrok Setup
    clear_screen()
    print_section("8. MANUAL NGROK SETUP", "For when automated install fails")
    print("Download links:")
    print_command("Windows: https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip")
    print_command("Mac (Intel): https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-darwin-amd64.zip")
    print_command("Mac (Apple Silicon): https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-darwin-arm64.zip")
    print_command("Linux (x86_64): https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip")
    print_command("Linux (ARM64): https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.zip")
    
    print("\nInstallation commands:")
    print_command("# Windows:")
    print_command("unzip ngrok-stable-windows-amd64.zip")
    print_command("move ngrok.exe C:\\Windows\\")
    
    print_command("\n# Mac/Linux:")
    print_command("unzip /path/to/ngrok.zip")
    print_command("sudo mv ngrok /usr/local/bin/")
    print_command("sudo chmod +x /usr/local/bin/ngrok")
    
    print("\nConnect your account:")
    print_command("ngrok authtoken YOUR_AUTH_TOKEN")
    
    if input("\nContinue? (y/n): ").lower() != 'y':
        return
    
    # Notes
    clear_screen()
    print_section("9. NOTES", "Important information")
    print("- The server owner is automatically admin")
    print("- All data is ephemeral (lost when server stops)")
    print("- For best security, use ngrok with auth token")
    print("- Server port changes each time for added security")
    print("- First user to enter admin token gets privileges")
    print("- Consider using a firewall for local connections")
    print("\nFor additional help: https://github.com/your-repo")
    
    print(f"\n{COLOR_GREEN}==========================================")
    print(f" MANUAL COMPLETE - HAPPY CHATTING! ")
    print(f"=========================================={COLOR_RESET}")

if __name__ == "__main__":
    try:
        display_manual()
    except KeyboardInterrupt:
        print("\n\nManual closed")
        sys.exit(0)

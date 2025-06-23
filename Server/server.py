import socket
import threading
import random
import string
import sys
import signal
import atexit
from pyngrok import ngrok
from network import create_tunnel

# ========================
# Global Variables
# ========================
clients = []  # (socket, address, is_admin, username)
banned_ips = set()
CMD_PREFIX = "::"
server_running = True
ADMIN_TOKEN = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
admin_ip = None
ngrok_url = None

# ========================
# Cleanup and Signal Handling
# ========================
def handle_shutdown(signum=None, frame=None):
    print("\n[!] Shutdown signal received. Cleaning up...")
    shutdown_server()
    sys.exit(0)

def shutdown_server():
    global server_running
    server_running = False
    try:
        if ngrok_url:
            ngrok.disconnect(ngrok_url)
    except:
        pass
    for client, _, _, _ in clients:
        try:
            client.send("[Server] Server shutting down. Goodbye!\n".encode())
            client.close()
        except:
            pass
    print("[+] All connections closed. Server clean.")

atexit.register(shutdown_server)
signal.signal(signal.SIGINT, handle_shutdown)
signal.signal(signal.SIGTERM, handle_shutdown)

# ========================
# Broadcast Helper
# ========================
def broadcast(msg, sender_socket=None):
    for client, _, _, _ in clients:
        if client != sender_socket:
            try:
                client.send(msg.encode())
            except:
                remove_client(client)

# ========================
# Remove client helper
# ========================
def remove_client(sock):
    global clients
    clients = [c for c in clients if c[0] != sock]
    print(f"[STATUS] Active connections: {len(clients)}")

# ========================
# Handle admin commands
# ========================
def handle_admin_command(command, client_socket, addr):
    is_admin = any(sock == client_socket and admin_status for sock, _, admin_status, _ in clients)

    if not is_admin:
        client_socket.send("[Server] Admin privileges required.\n".encode())
        return

    cmd = command.strip().split()
    if not cmd:
        return

    if cmd[0] == "::ban" and len(cmd) == 2:
        banned_ips.add(cmd[1])
        broadcast(f"[Server] IP {cmd[1]} banned by admin.")
    elif cmd[0] == "::warn" and len(cmd) >= 3:
        warning = " ".join(cmd[2:])
        for sock, ip, _, _ in clients:
            if ip[0] == cmd[1]:
                sock.send(f"[Admin Warning] {warning}\n".encode())
    elif cmd[0] == "::kick" and len(cmd) == 2:
        for sock, ip, _, name in clients:
            if ip[0] == cmd[1]:
                sock.send("[Server] You were kicked by admin.\n".encode())
                sock.close()
                remove_client(sock)
                broadcast(f"[Server] {name} was kicked.")
    elif cmd[0] == "::clear":
        broadcast("[Server] Chat cleared by admin.\n")
    elif cmd[0] == "::users":
        users = "\n".join([f"- {name} ({ip[0]})" for _, ip, _, name in clients])
        client_socket.send(f"[Server] Users:\n{users}\n".encode())
    elif cmd[0] == "::help":
        help_text = """
[Server] Admin Commands:
  ::ban <ip>     - Ban a user's IP
  ::kick <ip>    - Kick a user
  ::warn <ip> <msg> - Send a warning message
  ::clear        - Clear chat for all
  ::users        - List connected users
"""
        client_socket.send(help_text.encode())
    else:
        client_socket.send("[Server] Unknown admin command. Use ::help\n".encode())

# ========================
# Handle Client
# ========================
def handle_client(sock, addr):
    global admin_ip
    is_admin = False
    username = f"User-{addr[1]}"

    # Token Authentication
    if admin_ip is None:
        try:
            sock.send("[Server] Enter admin token: ".encode())
            attempt = sock.recv(1024).decode().strip()
            if attempt == ADMIN_TOKEN:
                admin_ip = addr[0]
                is_admin = True
                username = f"Admin-{addr[1]}"
                sock.send("[Server] Admin access granted.\n".encode())
            else:
                sock.send("[Server] Invalid token. Continuing as normal user.\n".encode())
        except:
            sock.send("[Server] Error with token input. Proceeding as user.\n".encode())
    else:
        sock.send("[Server] Admin already authenticated.\n".encode())

    clients.append((sock, addr, is_admin, username))
    sock.send(f"[Server] Welcome {username}. Type '{CMD_PREFIX}help' for commands.\n".encode())

    while server_running:
        try:
            msg = sock.recv(1024).decode()
            if not msg:
                break
            if msg.startswith(CMD_PREFIX):
                handle_admin_command(msg, sock, addr)
            else:
                broadcast(f"[{username}] {msg}", sock)
        except:
            break

    print(f"[-] {username} disconnected.")
    sock.close()
    remove_client(sock)

# ========================
# Start Server
# ========================
def start_server(port):
    global ngrok_url
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))
    server.listen()
    print(f"[+] Server listening on port {port}")
    print(f"[TOKEN] Admin Token: {ADMIN_TOKEN} (Save this!)")

    if input("Use ngrok? (y/n): ").lower() == 'y':
        token = input("Enter your ngrok authtoken: ").strip()
        ngrok.set_auth_token(token)
        tunnel = ngrok.connect(port, "tcp")
        ngrok_url = tunnel.public_url
        print(f"[NGROK] Public URL: {ngrok_url.replace('tcp://', '')}")

    print("[*] Waiting for clients...")
    while server_running:
        try:
            client_sock, addr = server.accept()
            if addr[0] in banned_ips:
                client_sock.send("[Server] You're banned.\n".encode())
                client_sock.close()
                continue
            threading.Thread(target=handle_client, args=(client_sock, addr), daemon=True).start()
        except:
            break

    server.close()

# ========================
# Entry Point
# ========================
if __name__ == '__main__':
    print("\n====== RealityPatch Server V1 ======")
    try:
        port = int(input("Enter port to run server on: "))
        start_server(port)
    except KeyboardInterrupt:
        handle_shutdown()
    except Exception as e:
        print(f"[ERROR] {e}")
        handle_shutdown()

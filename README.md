# RealityPatch-v1
Terminal based communication tool 
# ⚡ RealityPatch V1 – CyberChat  

 **RealityPatch V1 – CyberChat**, a privacy-focused, terminal-based chat app for hackers, web devs, enthusiasts, and anyone who doesn't want Big Brother breathing down their neck.  

This is a fully self-destructing chat server and client. When the server dies, it nukes the logs. No footprints. No evidence. No compromises.  

---

## 🧠 Features  

- ✅ Fully terminal-based with optional GUI  
- ✅ GUI fallback chain: **PyQt6 → Tkinter → CLI (default)**  
- ✅ Supports LAN and global connections via **ngrok TCP tunnels**  
- ✅ No data saved. EVER. No usernames, no logs, no history.  
- ✅ Dynamic Admin system — First to input admin token owns the server.  
- ✅ Admin tools:  
  - `/ban <IP>` – Block shady IPs  
  - `/kick <IP>` – Kick misbehaving users  
  - `/warn <IP> <msg>` – Send private warnings  
  - `/clear` – Wipe chat screen for everyone  
- ✅ Secure auto-server kill. Stops ngrok, closes all sockets.  
- ✅ Hacker-themed GUI with green-on-black cyberpunk vibes.  
- ✅ Works on Android (Termux), Linux, Windows, Mac.  
- ✅ Lightweight. No databases. No bloated frameworks.  

---

## 🚀 Installation  

### 🔥 Server Side  

```bash
git clone https://github.com/CyberStorm9/RealityPatch-v1.git
#### 🔥 Server Side  

cd RealityPatch-v1/Server
python install.py


### 🔥 Client Side  

```bash
git clone https://github.com/CyberStorm9/RealityPatch-v1.git
#### 🔥 Client Side  

cd RealityPatch-v1/Client 
python install.py
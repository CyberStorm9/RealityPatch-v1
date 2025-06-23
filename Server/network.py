# network.py
from pyngrok import ngrok, conf, exception

# Store the created tunnel so we can clean it up later
_active_tunnel = None

def create_tunnel(port: int, auth_token: str) -> str or None:
    """
    Creates an ngrok TCP tunnel to the given port using the provided auth token.
    Returns the public URL or None on failure.
    """
    global _active_tunnel
    try:
        # Set ngrok configuration
        config = conf.get_default()
        config.auth_token = auth_token
        config.region = "us"

        # Create the TCP tunnel
        _active_tunnel = ngrok.connect(port, "tcp")
        public_url = _active_tunnel.public_url

        print(f"[NGROK] Tunnel created: {public_url}")
        return public_url

    except exception.PyngrokNgrokError as e:
        print(f"[ERROR] Failed to create ngrok tunnel: {e}")
        return None

def close_tunnel():
    """
    Cleanly disconnect the active ngrok tunnel.
    Should be called during shutdown.
    """
    global _active_tunnel
    try:
        if _active_tunnel:
            ngrok.disconnect(_active_tunnel.public_url)
            print("[NGROK] Tunnel closed.")
    except Exception as e:
        print(f"[WARNING] Error closing ngrok tunnel: {e}")
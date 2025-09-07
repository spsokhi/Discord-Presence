from pypresence import Presence, exceptions as rpc_exc
import sys
import time
from datetime import datetime

client_id = "YOUR_APP_ID"

activity = {
    "details": "Playing CS2",
    "state": "Competitive – Mirage",
    "large_image": "cs2",
    "large_text": "Counter-Strike 2",
    "start": int(time.time())
}

rpc = Presence(client_id)

def connect():
    rpc.connect()
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Connected to Discord RPC.")

backoff = 2
while True:
    try:
        connect()
        break
    except (rpc_exc.DiscordNotFound, ConnectionRefusedError) as e:
        print(f"Discord not found / refused: {e}", file=sys.stderr)
        time.sleep(backoff)
        backoff = min(backoff * 1.5, 30)
    except Exception as e:
        print(f"Unexpected error while connecting: {e}", file=sys.stderr)
        time.sleep(backoff)
        backoff = min(backoff * 1.5, 30)

def set_presence():
    rpc.update(**activity)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Presence updated.")

try:
    set_presence()
    while True:
        time.sleep(60)
        try:
            set_presence()
        except (BrokenPipeError, rpc_exc.InvalidID, rpc_exc.ServerError, ConnectionResetError):
            print("Lost connection. Reconnecting...")
            connected = False
            backoff = 2
            while not connected:
                try:
                    connect()
                    set_presence()
                    connected = True
                except Exception as e:
                    print(f"Reconnect failed: {e}", file=sys.stderr)
                    time.sleep(backoff)
                    backoff = min(backoff * 1.5, 30)
finally:
    try:
        rpc.clear()
        rpc.close()
    except Exception:
        pass

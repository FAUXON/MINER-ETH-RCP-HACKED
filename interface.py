import time
import random
import threading
import tkinter as tk
from tkinter import ttk


def fake_rpc_error():
    errors = [
        "RPC Error: Failed to fetch gas price.",
        "RPC Error: Unexpected response from node.",
        "RPC Error: eth_getWork failed.",
        "RPC Error: Connection timeout to https://mainnet.infura.io",
    ]
    return random.choice(errors)


def simulate_mining_live():
    total_earned = 0.0
    mining_log = []
    for i in range(1, 101):
        base_reward = round(random.uniform(0.0005, 0.0015), 6)
        multiplied_reward = base_reward * 3
        total_earned += multiplied_reward
        block_text = f"[Block {i}] Reward: {base_reward:.6f} ETH x3 ➜ +{multiplied_reward:.6f} ETH"

        mining_log.append(block_text)
        if random.random() < 0.25:
            mining_log.append(f" ⚠️  {fake_rpc_error()}")
        mining_log.append("-" * 40)
        
        yield "\n".join(mining_log[-3:]), i, total_earned  # Renvoie les 3 dernières lignes, l’index et total


def run_mining():
    start_button.config(state=tk.DISABLED)  # Empêche clics multiples
    text_box.config(state=tk.NORMAL)
    text_box.delete(1.0, tk.END)
    progress_var.set(0)
    log_output = ""
    
    for log_entry, block_index, total_earned in simulate_mining_live():
        text_box.insert(tk.END, log_entry + "\n")
        text_box.see(tk.END)
        progress_var.set(block_index)
        time.sleep(1)  # 1 sec par bloc
        log_output += log_entry + "\n"

    summary = f"\n⛏️  Mining completed! Total earned: {total_earned:.6f} ETH"
    text_box.insert(tk.END, summary)
    text_box.config(state=tk.DISABLED)
    
    with open("mining_report.txt", "w") as f:
        f.write(log_output + "\n" + summary)
    
    start_button.config(state=tk.NORMAL)

# Démarrer dans un thread séparé
def start_mining():
    threading.Thread(target=run_mining).start()

# --- INTERFACE ---
window = tk.Tk()
window.title("ETH Mining RCP Leak")
window.geometry("650x600")
window.config(bg="#2c3e50")

frame = tk.Frame(window, bg="#34495e")
frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

title_label = tk.Label(frame, text="ETH Mining RCP Hacked", font=("Helvetica", 16, "bold"), fg="white", bg="#34495e")
title_label.pack(pady=10)

blockchain_info = """🔗 Blockchain Information:
Ethereum uses proof-of-work (PoW) to validate transactions and add new blocks.
Miners compete to solve complex puzzles, securing the network and earning rewards.
Each block mined provides a reward, which can fluctuate depending on network conditions."""
info_label = tk.Label(frame, text=blockchain_info, font=("Helvetica", 10), fg="white", bg="#34495e", justify=tk.LEFT)
info_label.pack(pady=10)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(frame, variable=progress_var, maximum=100, length=500)
progress_bar.pack(pady=20)

text_box = tk.Text(frame, height=15, width=70, wrap=tk.WORD, state=tk.DISABLED, bg="#ecf0f1", fg="#2c3e50", font=("Courier", 10))
text_box.pack(pady=10)

start_button = tk.Button(frame, text="Start Mining", command=start_mining, height=2, width=20, bg="#27ae60", fg="white", font=("Helvetica", 12))
start_button.pack(pady=10)

window.mainloop()

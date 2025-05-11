
import time
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def fake_rpc_error():
    errors = [
        "RPC Error: Failed to fetch gas price.",
        "RPC Error: Unexpected response from node.",
        "RPC Error: eth_getWork failed.",
        "RPC Error: Connection timeout to https://mainnet.infura.io",
    ]
    return random.choice(errors)

def simulate_mining():
    clear()
    print("╔══════════════════════════════════════╗")
    print("║       ETH Mining Simulator v1.0     ║")
    print("╚══════════════════════════════════════╝\n")
    total_earned = 0.0

    for i in range(1, 21):
        time.sleep(random.uniform(0.3, 0.7))
        base_reward = round(random.uniform(0.005, 0.02), 6)
        multiplied_reward = base_reward * 3
        total_earned += multiplied_reward
        print(f"[Block {i}] Reward: {base_reward:.6f} ETH x3 ➜ +{multiplied_reward:.6f} ETH")

        if random.random() < 0.25:
            print(f" ⚠️  {fake_rpc_error()}")
        print("-" * 40)

    print("\n⛏️  Mining completed! Total earned: {:.6f} ETH (simulated)".format(total_earned))
    input("\nAppuyez sur Entrée pour quitter...")

if __name__ == "__main__":
    simulate_mining()

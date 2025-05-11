import os

# Liste des types de fichiers à créer
file_types = ['py', 'txt', 'md', 'json', 'html', 'css', 'js', 'csv', 'log']

# Dossiers à créer
directories = ['Blockchain', 'Web3', 'SmartContracts']

# Noms de fichiers basés sur des concepts blockchain
file_names = [
    'backRCP', 'Multipl', 'Mining', 'SmartContract', 'Tokenization', 'GasFee', 
    'NodeSync', 'RPCRequest', 'DeFiProtocol', 'Validator', 'BlockchainExplorer', 
    'HashRate', 'BlockReward', 'CryptoWallet', 'Staking', 'Airdrop', 'DApp', 
    'BlockchainAPI', 'EthereumNode', 'Web3Integration'
]

# Fonction pour créer des fichiers
def create_files():
    # Créer les 20 fichiers avec des noms personnalisés
    for i in range(20):
        file_name = f"{file_names[i % len(file_names)]}.{file_types[i % len(file_types)]}"
        with open(file_name, 'w') as f:
            f.write(f"# {file_name} - Example file related to blockchain/Web3")
        print(f"{file_name} created!")

    # Créer les dossiers et les fichiers à l'intérieur
    for directory in directories:
        os.makedirs(directory, exist_ok=True)  # Créer le dossier s'il n'existe pas
        for j in range(1, 5):  # Créer 4 fichiers dans chaque dossier
            file_name = f"{directory}/{file_names[(j-1) % len(file_names)]}_{directory}_{j}.txt"
            with open(file_name, 'w') as f:
                f.write(f"# {file_name} - Example file related to {directory}")
            print(f"{file_name} created!")

# Exécution de la fonction
create_files()

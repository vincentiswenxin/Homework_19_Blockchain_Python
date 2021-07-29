# Import dependencies
import subprocess
import json
from dotenv import load_dotenv
# Import constants.py and necessary functions from bit and web3
from constants import *
import os
from web3 import Web3
from eth_account import Account
from bit import PrivateKeyTestnet
from bit.network import NetworkAPI
from web3.auto.gethdev import w3

 # Load and set environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic")

command = './derive -g --mnemonic="orphan prosper again evolve flavor assist moment review climb shove warrior valve" --cols=path,address,privkey,pubkey --format=json'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p_status = p.wait()

keys = json.loads(output)
print(keys)











# Create a function called `derive_wallets`
# def derive_wallets(coin):
#     import subprocess
#     import json
#     command = 'php ./hd-wallet-derive/hd-wallet-derive.php -g --mnemonic="orphan prosper again evolve flavor assist moment review climb shove warrior valve" --cols=path,address,privkey,pubkey --format=json -- numderive=3' 
#     #print(command)
#     p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
#     #print(p)
#     output, err = p.communicate()
#     p_status = p.wait()
#     return json.loads(output)
# derive_wallets(ETH)
# # Create a dictionary object called coins to store the output from `derive_wallets`.
# coins = {ETH: derive_wallets(ETH), BTCTEST: derive_wallets(BTCTEST)}
# print(coins)

# # Create a function called `priv_key_to_account` that converts privkey strings to account objects.
# def priv_key_to_account(# YOUR CODE HERE):
#     # YOUR CODE HERE

# # Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
# def create_tx(# YOUR CODE HERE):
#     # YOUR CODE HERE

# # Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
# def send_tx(# YOUR CODE HERE):
#     # YOUR CODE HERE


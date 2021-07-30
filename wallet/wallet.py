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
from web3.middleware import geth_poa_middleware
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic")

#Create a function called `derive_wallets`
def derive_wallets(coin):
    command = f'php ./derive -g --mnemonic="{mnemonic}" --cols=path,address,privkey,pubkey --coin={coin} --format=json -- numderive=3' 
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = {ETH: derive_wallets(ETH), BTCTEST: derive_wallets(BTCTEST)}
print(coins)

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    elif coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(coin, account, to, amount):
    if coin == ETH:
        gasEstimate = w3.eth.estimateGas(
            {"from": account.address, "to": to, "value": amount})
        return {
            "from": account.address,
            "to": to,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address)}
    elif coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(coin, account, to, amount):
    tx = create_tx(coin, account, to, amount)
    signed_tx = account.sign_transaction(tx)
    if coin == ETH: 
        return w3.eth.sendRawTransaction(signed.rawTransaction)
    elif coin == BTCTEST: 
        return NetworkAPI.broadcast_tx_testnet(signed_tx) 

# the following is the test account info
#test_acc = priv_key_to_account(BTCTEST, "L3tgVp9rtaXHJD9FirXSG4aCr2iLvstefKsJHyapHtkkGzrmUuuj")
#PrivateKeyTestnet: mvWMmMJ3QojPFjed3K9Q5iZd2yHJtYCZE9
#test_acc_eth = priv_key_to_account(ETH, "Kyy42gkJPveSesLJajtrnZAmypUxDiZ6rF8yZZBTNUv83VkSmb6d")

#return bit test to the Faucet(mkHS9ne12qx9pS9VojpwU5xtRd4T7X7ZUt)
#send_tx(BTCTEST, test_acc, "mkHS9ne12qx9pS9VojpwU5xtRd4T7X7ZUt",0.00001)






from web3 import Web3
from termcolor import cprint
import config


gasLimit = 3000000
def usdc_arb_approve(private_key, gasLimit):
    rpc = config.ARB_RPC
    web3 = Web3(Web3.HTTPProvider(rpc))
    usdc_contract_address = config.arv_usdc_contract_address
    ucdc_contract = web3.eth.contract(usdc_contract_address, abi=config.ERC20_ABI)
    try:

        account = web3.eth.account.privateKeyToAccount(private_key)
        address_wallet = account.address

        approve_amount = 2 ** 256 - 1

        #Адрес контракта при апруве
        contractSwap = Web3.toChecksumAddress(config.arb_contract)

        gasPrice = Web3.toWei(0.0000000001, 'ether')
        nonce = web3.eth.get_transaction_count(address_wallet)

        approve_transaction = ucdc_contract.functions.approve(
            contractSwap, approve_amount
        ).buildTransaction({
            'chainId': web3.eth.chain_id,
            'gas': gasLimit,
            'gasPrice': gasPrice,
            'nonce': nonce,
        })

        signed_txn = web3.eth.account.sign_transaction(approve_transaction, private_key=private_key)
        tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        cprint(f'\n>>> Approve USDC | https://arbiscan.io/tx/{web3.toHex(tx_token)} ', 'green')
    except Exception as error:
        cprint(f'\n>>> Approve USDC | {address_wallet} | {error}', 'red')

def usdc_aave_arb_approve(private_key, gasLimit):
    rpc = config.ARB_RPC
    web3 = Web3(Web3.HTTPProvider(rpc))
    usdc_aave_contract_address = config.arb_usdc_aave_contract_address
    usdc_aave_contract = web3.eth.contract(usdc_aave_contract_address, abi=config.ERC20_ABI)
    try:

        account = web3.eth.account.privateKeyToAccount(private_key)
        address_wallet = account.address

        approve_amount = 2 ** 256 - 1

        #Адрес контракта при апруве
        contractSwap = Web3.toChecksumAddress(config.arb_contract)

        gasPrice = Web3.toWei(0.0000000001, 'ether')
        nonce = web3.eth.get_transaction_count(address_wallet)

        approve_transaction = usdc_aave_contract.functions.approve(
            contractSwap, approve_amount
        ).buildTransaction({
            'chainId': web3.eth.chain_id,
            'gas': gasLimit,
            'gasPrice': gasPrice,
            'nonce': nonce,
        })

        signed_txn = web3.eth.account.sign_transaction(approve_transaction, private_key=private_key)
        tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        cprint(f'\n>>> Approve AUSDC | https://arbiscan.io/tx/{web3.toHex(tx_token)} ', 'green')
    except Exception as error:
        cprint(f'\n>>> Approve AUSDC | {address_wallet} | {error}', 'red')

def usdc_opt_approve(private_key, gasLimit):
    rpc = config.OPT_RPC
    web3 = Web3(Web3.HTTPProvider(rpc))
    usdc_contract_address = config.opt_usdc_contract_address
    usdc_contract = web3.eth.contract(usdc_contract_address, abi=config.ERC20_ABI)
    try:

        account = web3.eth.account.privateKeyToAccount(private_key)
        address_wallet = account.address

        approve_amount = 2 ** 256 - 1

        # Адрес контракта при апруве
        contractSwap = Web3.toChecksumAddress(config.opt_contract)

        gasPrice = Web3.toWei(0.0000000001, 'ether')
        nonce = web3.eth.get_transaction_count(address_wallet)

        approve_transaction = usdc_contract.functions.approve(
            contractSwap, approve_amount
        ).buildTransaction({
            'chainId': web3.eth.chain_id,
            'gas': gasLimit,
            'gasPrice': gasPrice,
            'nonce': nonce,
        })

        signed_txn = web3.eth.account.sign_transaction(approve_transaction, private_key=private_key)
        tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        cprint(f'\n>>> Approve USDC | https://optimistic.etherscan.io/tx/{web3.toHex(tx_token)} ', 'green')
    except Exception as error:
        cprint(f'\n>>> Approve USDC | {address_wallet} | {error}', 'red')


def usdc_aave_opt_approve(private_key, gasLimit):
    rpc = config.OPT_RPC
    web3 = Web3(Web3.HTTPProvider(rpc))
    usdc_aave_contract_address = config.opt_usdc_aave_contract_address
    usdc_aave_contract = web3.eth.contract(usdc_aave_contract_address, abi=config.ERC20_ABI)
    try:

        account = web3.eth.account.privateKeyToAccount(private_key)
        address_wallet = account.address

        approve_amount = 2 ** 256 - 1

        #Адрес контракта при апруве
        contractSwap = Web3.toChecksumAddress(config.opt_contract)

        gasPrice = Web3.toWei(0.0000000001, 'ether')
        nonce = web3.eth.get_transaction_count(address_wallet)

        approve_transaction = usdc_aave_contract.functions.approve(
            contractSwap, approve_amount
        ).buildTransaction({
            'chainId': web3.eth.chain_id,
            'gas': gasLimit,
            'gasPrice': gasPrice,
            'nonce': nonce,
        })

        signed_txn = web3.eth.account.sign_transaction(approve_transaction, private_key=private_key)
        tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        cprint(f'\n>>> Approve AUSDC | https://optimistic.etherscan.io/tx/{web3.toHex(tx_token)} ', 'green')
    except Exception as error:
        cprint(f'\n>>> Approve AUSDC | {address_wallet} | {error}', 'red')

def usdc_pol_approve(private_key, gasLimit):
    gasLimit = 250000
    rpc = config.POL_RPC
    web3 = Web3(Web3.HTTPProvider(rpc))
    usdc_contract_address = config.pol_usdc_contract_address
    usdc_contract = web3.eth.contract(usdc_contract_address, abi=config.ERC20_ABI)
    try:

        account = web3.eth.account.privateKeyToAccount(private_key)
        address_wallet = account.address

        approve_amount = 2 ** 256 - 1

        # Адрес контракта при апруве
        contractSwap = Web3.toChecksumAddress(config.pol_contract)

        nonce = web3.eth.get_transaction_count(address_wallet)

        approve_transaction = usdc_contract.functions.approve(
            contractSwap, approve_amount
        ).buildTransaction({
            'chainId': web3.eth.chain_id,
            'gas': gasLimit,
            'gasPrice': web3.toWei('1000', 'gwei'),
            'nonce': nonce,
        })

        signed_txn = web3.eth.account.sign_transaction(approve_transaction, private_key=private_key)
        tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        cprint(f'\n>>> Approve USDC | https://polygonscan.com/tx/{web3.toHex(tx_token)} ', 'green')
    except Exception as error:
        cprint(f'\n>>> Approve USDC | {address_wallet} | {error}', 'red')

def usdc_aave_pol_approve(private_key, gasLimit):
    rpc = config.POL_RPC
    web3 = Web3(Web3.HTTPProvider(rpc))
    usdc_aave_contract_address = config.pol_usdc_aave_contract_address
    usdc_aave_contract = web3.eth.contract(usdc_aave_contract_address, abi=config.ERC20_ABI)
    try:

        account = web3.eth.account.privateKeyToAccount(private_key)
        address_wallet = account.address

        approve_amount = 2 ** 256 - 1

        #Адрес контракта при апруве
        contractSwap = Web3.toChecksumAddress(config.pol_contract)

        nonce = web3.eth.get_transaction_count(address_wallet)

        approve_transaction = usdc_aave_contract.functions.approve(
            contractSwap, approve_amount
        ).buildTransaction({
            'chainId': web3.eth.chain_id,
            'gas': gasLimit,
            'gasPrice': web3.toWei('1000', 'gwei'),
            'nonce': nonce,
        })

        signed_txn = web3.eth.account.sign_transaction(approve_transaction, private_key=private_key)
        tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        cprint(f'\n>>> Approve AUSDC | https://polygonscan.com/tx/{web3.toHex(tx_token)} ', 'green')
    except Exception as error:
        cprint(f'\n>>> Approve AUSDC | {address_wallet} | {error}', 'red')
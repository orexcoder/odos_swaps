import random
import time
import config
import approve

from web3 import Web3
from termcolor import cprint

def swap(swap_amount, chain_selected, odos_swap_contract, path_USDC_AUSDC, path_AUSDC_USDC, private_key, gasLimit, gasPrice):

    account = web3.eth.account.privateKeyToAccount(private_key)
    address_wallet = Web3.toChecksumAddress(account.address)
    contractToken = Web3.toChecksumAddress(odos_swap_contract)

    contract = web3.eth.contract(address=contractToken, abi=abi)

    byte_inputs_permit = '0x'

    for i in range(swap_amount):
        nonce = web3.eth.get_transaction_count(address_wallet)
        usdc_balance = ucdc_contract.functions.balanceOf(address_wallet).call()
        ausdc_balance = usdc_aave_contract.functions.balanceOf(address_wallet).call()
        if round(usdc_balance / 1000000, 2) > 0:
            try:
                swap_staff_input = [str(usdc_contract_address), usdc_balance,
                                    executor, byte_inputs_permit]
                swap_staff_output = [str(usdc_aave_contract_address), 1, str(address_wallet)]
                contract_txn = contract.functions.swap(
                    [swap_staff_input],
                    [swap_staff_output],
                    usdc_balance,
                    int(round(usdc_balance * 0.996)),
                    executor,
                    path_USDC_AUSDC
                ).buildTransaction({
                    'from': address_wallet,
                    'gas': gasLimit,
                    'gasPrice': gasPrice,
                    'nonce': nonce,
                })

                signed_txn = web3.eth.account.sign_transaction(contract_txn, private_key=private_key)
                tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
                if chain_selected == 'Arbitrum':
                    cprint(f'\n>>> Swapping {i + 1}| https://arbiscan.io/tx/{web3.toHex(tx_token)} ', 'green')
                    time.sleep(random.randint(5, 10))
                elif chain_selected == 'Optimism':
                    cprint(f'\n>>> Swapping {i + 1}| https://optimistic.etherscan.io/tx/{web3.toHex(tx_token)} ', 'green')
                    time.sleep(random.randint(5, 10))
                elif chain_selected == 'Polygon':
                    cprint(f'\n>>> Swapping {i + 1}| https://polygonscan.com/tx/{web3.toHex(tx_token)} ',
                           'green')
                    time.sleep(random.randint(10, 20))
                else:
                    cprint('\n>>> Укажите корректную сеть ', 'red')
            except Exception as error:
                cprint(f'\n>>> Error with address | {address_wallet} | {error}', 'red')

        else:
            try:
                swap_staff_input = [str(usdc_aave_contract_address), ausdc_balance,
                                    executor, byte_inputs_permit]
                swap_staff_output = [str(usdc_contract_address), 1, str(address_wallet)]
                contract_txn = contract.functions.swap(
                    [swap_staff_input],
                    [swap_staff_output],
                    ausdc_balance,
                    int(round(ausdc_balance * 0.996)),
                    executor,
                    path_AUSDC_USDC
                ).buildTransaction({
                    'from': address_wallet,
                    'gas': gasLimit,
                    'gasPrice': gasPrice,
                    'nonce': nonce,
                })

                signed_txn = web3.eth.account.sign_transaction(contract_txn, private_key=private_key)
                tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
                if chain_selected == 'Arbitrum':
                    cprint(f'\n>>> Swapping {i + 1}| https://arbiscan.io/tx/{web3.toHex(tx_token)} ', 'green')
                    time.sleep(random.randint(5, 10))
                elif chain_selected == 'Optimism':
                    cprint(f'\n>>> Swapping {i + 1}| https://optimistic.etherscan.io/tx/{web3.toHex(tx_token)} ',
                           'green')
                    time.sleep(random.randint(5, 10))
                elif chain_selected == 'Polygon':
                    cprint(f'\n>>> Swapping {i + 1}| https://polygonscan.com/tx/{web3.toHex(tx_token)} ',
                           'green')
                    time.sleep(random.randint(10, 20))
                else:
                    cprint('\n>>> Укажите корректную сеть ', 'red')
            except Exception as error:
                cprint(f'\n>>> Error with address | {address_wallet} | {error}', 'red')


if __name__ == '__main__':
    cprint(f'\n============================================= 0rex =============================================',
           'cyan')
    cprint(f'\ndonate: 0x5086028342e11b4ea1c405ca9923c4f3ffa0056f',
           'cyan')
    cprint(f'\nsubscribe to me : https://t.me/orex_code', 'magenta')
    print()
    chain_selected = str(input('Укажите сеть для свапов: Arbitrum, Optimism, Polygon \n'))
    next_trans = 1
    if chain_selected == 'Arbitrum':
        rpc = config.ARB_RPC
        web3 = Web3(Web3.HTTPProvider(rpc))
        gasLimit = 3000000
        gasPrice = Web3.toWei(0.0000000001, 'ether')
        usdc_contract_address = config.arv_usdc_contract_address
        ucdc_contract = web3.eth.contract(usdc_contract_address, abi=config.ERC20_ABI)
        usdc_aave_contract_address = config.arb_usdc_aave_contract_address
        usdc_aave_contract = web3.eth.contract(usdc_aave_contract_address, abi=config.ERC20_ABI)
        executor = Web3.toChecksumAddress(config.arb_executor)
        abi = config.ABI_ARB
        odos_swap_contract = config.arb_contract
        path_USDC_AUSDC = config.ARB_PATH_USDC_TO_AUSDC
        path_AUSDC_USDC = config.ARB_PATH_AUSDC_TO_USDC

    elif chain_selected == 'Optimism':
        rpc = config.OPT_RPC
        web3 = Web3(Web3.HTTPProvider(rpc))
        gasLimit = 3000000
        gasPrice = Web3.toWei(0.0000000001, 'ether')
        usdc_contract_address = config.opt_usdc_contract_address
        ucdc_contract = web3.eth.contract(usdc_contract_address, abi=config.ERC20_ABI)
        usdc_aave_contract_address = config.opt_usdc_aave_contract_address
        usdc_aave_contract = web3.eth.contract(usdc_aave_contract_address, abi=config.ERC20_ABI)
        executor = Web3.toChecksumAddress(config.opt_executor)
        abi = config.ABI_OPT
        odos_swap_contract = config.opt_contract
        path_USDC_AUSDC = config.OPT_PATH_USDC_TO_AUSDC
        path_AUSDC_USDC = config.OPT_PATH_AUSDC_TO_USDC

    elif chain_selected == 'Polygon':
        rpc = config.POL_RPC
        web3 = Web3(Web3.HTTPProvider(rpc))
        gasLimit = 300000
        gasPrice = web3.toWei('1000', 'gwei')
        usdc_contract_address = config.pol_usdc_contract_address
        ucdc_contract = web3.eth.contract(usdc_contract_address, abi=config.ERC20_ABI)
        usdc_aave_contract_address = config.pol_usdc_aave_contract_address
        usdc_aave_contract = web3.eth.contract(usdc_aave_contract_address, abi=config.ERC20_ABI)
        executor = Web3.toChecksumAddress(config.pol_executor)
        abi = config.ABI_POL
        odos_swap_contract = config.pol_contract
        path_USDC_AUSDC = config.POL_PATH_USDC_TO_AUSDC
        path_AUSDC_USDC = config.POL_PATH_AUSDC_TO_USDC

    else:
        cprint('\n>>> Укажите корректную сеть ', 'red')
        next_trans = 0

    if next_trans == 1:
        swap_amount = int(input('Укажите количество свапов на каждом кошельке: '))


    with open('private_keys.txt', 'r') as key:
        keys_list = [row.strip() for row in key]

        for private_key in keys_list:
            cprint(f'\n=============== start : {private_key} ===============', 'white')
            if chain_selected == 'Arbitrum':
                pass
                approve.usdc_arb_approve(private_key, gasLimit)
                time.sleep(random.randint(5, 15))
                approve.usdc_aave_arb_approve(private_key, gasLimit)
                time.sleep(random.randint(5, 15))
            elif chain_selected == 'Optimism':
                pass
                approve.usdc_opt_approve(private_key, gasLimit)
                time.sleep(random.randint(5, 15))
                approve.usdc_aave_opt_approve(private_key, gasLimit)
                time.sleep(random.randint(5, 15))
            elif chain_selected == 'Polygon':
                pass
                approve.usdc_pol_approve(private_key, gasLimit)
                time.sleep(random.randint(5, 15))
                approve.usdc_aave_pol_approve(private_key, gasLimit)
                time.sleep(random.randint(20, 30))
            else:
                cprint('\n>>> Укажите корректную сеть ', 'red')

            swap(swap_amount, chain_selected, odos_swap_contract, path_USDC_AUSDC, path_AUSDC_USDC, private_key, gasLimit, gasPrice)
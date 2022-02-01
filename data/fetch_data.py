import os
import json
import time
import schedule
from web3 import Web3

from apiclient import discovery
from google.oauth2 import service_account
from pycoingecko import CoinGeckoAPI


# Initialize web3
INFURA_TOKEN = os.environ['WEB3_INFURA_TOKEN_4']
infuraURL = f'https://mainnet.infura.io/v3/{INFURA_TOKEN}'
web3 = Web3(Web3.HTTPProvider(infuraURL))

# Price APIs
cg = CoinGeckoAPI()

def check_refresh(spreadsheet_id, sheet, range_name):
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    return result.get('values',[])[0][0], result.get('values',[])[1][0]


def lp_v2_info(lp_address):
    try:
        lp_address = Web3.toChecksumAddress(lp_address)
        lp_abi = json.loads('[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
        lp = web3.eth.contract(address=lp_address, abi=lp_abi)
        token_zero = lp.functions.token0().call()
        token_one = lp.functions.token1().call()
        reserves = lp.functions.getReserves().call()
        supply = lp.functions.totalSupply().call()
        return token_zero, token_one, reserves[0], reserves[1], supply      
    except Exception as e:
        print('lp error')
        print(e)


def lp_v3_info(lp_address):
    try:
        lp_address = Web3.toChecksumAddress(lp_address)
        lp_abi = json.loads('[{"inputs":[{"internalType":"address payable","name":"_gelato","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"receiver","type":"address"},{"indexed":false,"internalType":"uint256","name":"burnAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":false,"internalType":"uint128","name":"liquidityBurned","type":"uint128"}],"name":"Burned","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"feesEarned0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"feesEarned1","type":"uint256"}],"name":"FeesEarned","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"receiver","type":"address"},{"indexed":false,"internalType":"uint256","name":"mintAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint128","name":"liquidityMinted","type":"uint128"}],"name":"Minted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousManager","type":"address"},{"indexed":true,"internalType":"address","name":"newManager","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"int24","name":"lowerTick_","type":"int24"},{"indexed":false,"internalType":"int24","name":"upperTick_","type":"int24"},{"indexed":false,"internalType":"uint128","name":"liquidityBefore","type":"uint128"},{"indexed":false,"internalType":"uint128","name":"liquidityAfter","type":"uint128"}],"name":"Rebalance","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"managerFee","type":"uint16"}],"name":"SetManagerFee","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"oldAdminTreasury","type":"address"},{"indexed":false,"internalType":"address","name":"newAdminTreasury","type":"address"}],"name":"UpdateAdminTreasury","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"gelatoRebalanceBPS","type":"uint16"},{"indexed":false,"internalType":"uint16","name":"gelatoWithdrawBPS","type":"uint16"},{"indexed":false,"internalType":"uint16","name":"gelatoSlippageBPS","type":"uint16"},{"indexed":false,"internalType":"uint32","name":"gelatoSlippageInterval","type":"uint32"}],"name":"UpdateGelatoParams","type":"event"},{"inputs":[],"name":"GELATO","outputs":[{"internalType":"address payable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"burnAmount","type":"uint256"},{"internalType":"address","name":"receiver","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"},{"internalType":"uint128","name":"liquidityBurned","type":"uint128"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int24","name":"newLowerTick","type":"int24"},{"internalType":"int24","name":"newUpperTick","type":"int24"},{"internalType":"uint160","name":"swapThresholdPrice","type":"uint160"},{"internalType":"uint256","name":"swapAmountBPS","type":"uint256"},{"internalType":"bool","name":"zeroForOne","type":"bool"}],"name":"executiveRebalance","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"gelatoBalance0","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"gelatoBalance1","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"gelatoFeeBPS","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"gelatoRebalanceBPS","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"gelatoSlippageBPS","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"gelatoSlippageInterval","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"gelatoWithdrawBPS","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount0Max","type":"uint256"},{"internalType":"uint256","name":"amount1Max","type":"uint256"}],"name":"getMintAmounts","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"},{"internalType":"uint256","name":"mintAmount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getPositionID","outputs":[{"internalType":"bytes32","name":"positionID","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getUnderlyingBalances","outputs":[{"internalType":"uint256","name":"amount0Current","type":"uint256"},{"internalType":"uint256","name":"amount1Current","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint160","name":"sqrtRatioX96","type":"uint160"}],"name":"getUnderlyingBalancesAtPrice","outputs":[{"internalType":"uint256","name":"amount0Current","type":"uint256"},{"internalType":"uint256","name":"amount1Current","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"address","name":"_pool","type":"address"},{"internalType":"uint16","name":"_managerFeeBPS","type":"uint16"},{"internalType":"int24","name":"_lowerTick","type":"int24"},{"internalType":"int24","name":"_upperTick","type":"int24"},{"internalType":"address","name":"_manager_","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_managerFeeBPS","type":"uint16"}],"name":"initializeManagerFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"lowerTick","outputs":[{"internalType":"int24","name":"","type":"int24"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"manager","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"managerBalance0","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"managerBalance1","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"managerFeeBPS","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"managerTreasury","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"mintAmount","type":"uint256"},{"internalType":"address","name":"receiver","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"},{"internalType":"uint128","name":"liquidityMinted","type":"uint128"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pool","outputs":[{"internalType":"contract IUniswapV3Pool","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint160","name":"swapThresholdPrice","type":"uint160"},{"internalType":"uint256","name":"swapAmountBPS","type":"uint256"},{"internalType":"bool","name":"zeroForOne","type":"bool"},{"internalType":"uint256","name":"feeAmount","type":"uint256"},{"internalType":"address","name":"paymentToken","type":"address"}],"name":"rebalance","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"token0","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"token1","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount0Owed","type":"uint256"},{"internalType":"uint256","name":"amount1Owed","type":"uint256"},{"internalType":"bytes","name":"","type":"bytes"}],"name":"uniswapV3MintCallback","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"amount0Delta","type":"int256"},{"internalType":"int256","name":"amount1Delta","type":"int256"},{"internalType":"bytes","name":"","type":"bytes"}],"name":"uniswapV3SwapCallback","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"newRebalanceBPS","type":"uint16"},{"internalType":"uint16","name":"newWithdrawBPS","type":"uint16"},{"internalType":"uint16","name":"newSlippageBPS","type":"uint16"},{"internalType":"uint32","name":"newSlippageInterval","type":"uint32"},{"internalType":"address","name":"newTreasury","type":"address"}],"name":"updateGelatoParams","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"upperTick","outputs":[{"internalType":"int24","name":"","type":"int24"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"feeAmount","type":"uint256"},{"internalType":"address","name":"feeToken","type":"address"}],"name":"withdrawGelatoBalance","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"feeAmount","type":"uint256"},{"internalType":"address","name":"feeToken","type":"address"}],"name":"withdrawManagerBalance","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
        lp = web3.eth.contract(address=lp_address, abi=lp_abi)
        token_zero = lp.functions.token0().call()
        token_one = lp.functions.token1().call()
        return token_zero, token_one   
    except Exception as e:
        print('lp error')
        print(e)


def token_info(token_address, token_dict):
    try:
        token_address = Web3.toChecksumAddress(token_address)
        token_abi = json.loads('[{"inputs":[{"internalType":"uint256","name":"chainId_","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"src","type":"address"},{"indexed":true,"internalType":"address","name":"guy","type":"address"},{"indexed":false,"internalType":"uint256","name":"wad","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":true,"inputs":[{"indexed":true,"internalType":"bytes4","name":"sig","type":"bytes4"},{"indexed":true,"internalType":"address","name":"usr","type":"address"},{"indexed":true,"internalType":"bytes32","name":"arg1","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"arg2","type":"bytes32"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"}],"name":"LogNote","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"src","type":"address"},{"indexed":true,"internalType":"address","name":"dst","type":"address"},{"indexed":false,"internalType":"uint256","name":"wad","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"burn","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"guy","type":"address"}],"name":"deny","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"mint","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"src","type":"address"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"move","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"holder","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"bool","name":"allowed","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"pull","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"push","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"guy","type":"address"}],"name":"rely","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"src","type":"address"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"version","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"wards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]')
        token = web3.eth.contract(address=token_address, abi=token_abi)
        symbol = token.functions.symbol().call()
        decimals = token.functions.decimals().call()
        return symbol, decimals
    except Exception as e:
        print('token error')
        print(e)


def cg_price(token_api_id):
    return cg.get_price(ids=token_api_id, vs_currencies='usd')[token_api_id]['usd']

def main():
    print('checking')
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    secret_file = os.path.join(os.getcwd(), 'client_secret.json')
    spreadsheet_id = = os.environ['LIQUIDITY_SPREADSHEET_ID']

    try:    
        credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scopes)
        service = discovery.build('sheets', 'v4', credentials=credentials)
        sheet = service.spreadsheets()

        token_dict = {'0x64aa3364F17a4D01c6f1751Fd97C2BD3D7e7f1D5':'olympus', '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2':'ethereum', '0x853d955aCEf822Db058eb8505911ED77F175b99e':'frax', '0x6B175474E89094C44Da98b954EedeAC495271d0F':'dai'}



        #addLiquidity
        check_add, pool_address_add = check_refresh(spreadsheet_id, sheet, range_name='addLiquidity!D18:D19')

        if check_add == 'TRUE':
            #inform that the program is running
            data = {'values' : [['fetching info...']]}
            sheet.values().update(spreadsheetId=spreadsheet_id, body=data, range='addLiquidity!F18', valueInputOption='USER_ENTERED').execute()

            #fetch on-chain info
            contract_zero, contract_one = lp_v3_info(pool_address_add)
            symbol_zero, decimals_zero = token_info(contract_zero, token_dict)
            symbol_one, decimals_one = token_info(contract_one, token_dict)
            price_zero, price_one = cg_price(token_dict[contract_zero]), cg_price(token_dict[contract_one])
            
            #update gsheets
            values_zero = [
                [symbol_zero], [decimals_zero], [contract_zero], [price_zero]         
            ]
            values_one = [
                [symbol_one], [decimals_one], [contract_one], [price_one]            
            ]
            
            data_zero = {'values' : values_zero}
            sheet.values().update(spreadsheetId=spreadsheet_id, body=data_zero, range='addLiquidity!D20:D23', valueInputOption='USER_ENTERED').execute()
            
            data_one = {'values' : values_one}
            sheet.values().update(spreadsheetId=spreadsheet_id, body=data_one, range='addLiquidity!D25:D28', valueInputOption='USER_ENTERED').execute()
            
            data = {'values' : [['FALSE']]}
            sheet.values().update(spreadsheetId=spreadsheet_id, body=data, range='addLiquidity!D18', valueInputOption='USER_ENTERED').execute()
            
            #inform that the program has finished
            data = {'values' : [['']]}
            sheet.values().update(spreadsheetId=spreadsheet_id, body=data, range='addLiquidity!F18', valueInputOption='USER_ENTERED').execute()
            print('updated')

        #removeLiquidity
        check_remove, pool_address_remove = check_refresh(spreadsheet_id, sheet, range_name='removeLiquidity!D12:D13')

        if check_remove == 'TRUE':
            #inform that the program is running
            data = {'values' : [['fetching info...']]}
            sheet.values().update(spreadsheetId=spreadsheet_id, body=data, range='removeLiquidity!F12', valueInputOption='USER_ENTERED').execute()

            #fetch on-chain info
            contract_zero, contract_one, amount_zero, amount_one, supply = lp_v2_info(pool_address_remove)
            symbol_zero, decimals_zero = token_info(contract_zero, token_dict)
            symbol_one, decimals_one = token_info(contract_one, token_dict)
            price_zero, price_one = cg_price(token_dict[contract_zero]), cg_price(token_dict[contract_one])

            #update gsheets
            values = [
                [symbol_zero], [decimals_zero], [contract_zero], [amount_zero], [price_zero],
                [symbol_one], [decimals_one], [contract_one], [amount_one], [price_one],
                [supply]
            ]
            
            data = {'values' : values}
            sheet.values().update(spreadsheetId=spreadsheet_id, body=data, range='removeLiquidity!D14:D24', valueInputOption='USER_ENTERED').execute()
            
            data = {'values' : [['FALSE']]}
            sheet.values().update(spreadsheetId=spreadsheet_id, body=data, range='removeLiquidity!D12', valueInputOption='USER_ENTERED').execute()
            
            #inform that the program has finished
            data = {'values' : [['']]}
            sheet.values().update(spreadsheetId=spreadsheet_id, body=data, range='removeLiquidity!F12', valueInputOption='USER_ENTERED').execute()
            print('updated')

    except OSError as e:
        print (e)


schedule.every(5).seconds.do(main)
while True:
    schedule.run_pending()
    time.sleep(1)
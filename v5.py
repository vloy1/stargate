from web3 import Web3
import time
import random
from web3.middleware import geth_poa_middleware
import transfer

w3 = Web3(Web3.HTTPProvider('https://arb1.arbitrum.io/rpc'))
t = 10

abi_stargate = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"chainId","type":"uint16"},{"indexed":false,"internalType":"bytes","name":"srcAddress","type":"bytes"},{"indexed":false,"internalType":"uint256","name":"nonce","type":"uint256"},{"indexed":false,"internalType":"address","name":"token","type":"address"},{"indexed":false,"internalType":"uint256","name":"amountLD","type":"uint256"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"bytes","name":"payload","type":"bytes"},{"indexed":false,"internalType":"bytes","name":"reason","type":"bytes"}],"name":"CachedSwapSaved","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"srcChainId","type":"uint16"},{"indexed":true,"internalType":"bytes","name":"srcAddress","type":"bytes"},{"indexed":true,"internalType":"uint256","name":"nonce","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"srcPoolId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"dstPoolId","type":"uint256"},{"indexed":false,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amountSD","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"mintAmountSD","type":"uint256"}],"name":"RedeemLocalCallback","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"bridgeFunctionType","type":"uint8"},{"indexed":false,"internalType":"uint16","name":"chainId","type":"uint16"},{"indexed":false,"internalType":"bytes","name":"srcAddress","type":"bytes"},{"indexed":false,"internalType":"uint256","name":"nonce","type":"uint256"}],"name":"Revert","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"srcChainId","type":"uint16"},{"indexed":false,"internalType":"uint256","name":"_srcPoolId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_dstPoolId","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"to","type":"bytes"},{"indexed":false,"internalType":"uint256","name":"redeemAmountSD","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"mintAmountSD","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"nonce","type":"uint256"},{"indexed":true,"internalType":"bytes","name":"srcAddress","type":"bytes"}],"name":"RevertRedeemLocal","type":"event"},{"inputs":[{"internalType":"uint256","name":"_poolId","type":"uint256"},{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"uint256","name":"_dstPoolId","type":"uint256"}],"name":"activateChainPath","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_poolId","type":"uint256"},{"internalType":"uint256","name":"_amountLD","type":"uint256"},{"internalType":"address","name":"_to","type":"address"}],"name":"addLiquidity","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"bridge","outputs":[{"internalType":"contract Bridge","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"bytes","name":"","type":"bytes"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"cachedSwapLookup","outputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountLD","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"payload","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_poolId","type":"uint256"},{"internalType":"bool","name":"_fullMode","type":"bool"}],"name":"callDelta","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"internalType":"uint256","name":"_nonce","type":"uint256"}],"name":"clearCachedSwap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_poolId","type":"uint256"},{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"uint256","name":"_dstPoolId","type":"uint256"},{"internalType":"uint256","name":"_weight","type":"uint256"}],"name":"createChainPath","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_poolId","type":"uint256"},{"internalType":"address","name":"_token","type":"address"},{"internalType":"uint8","name":"_sharedDecimals","type":"uint8"},{"internalType":"uint8","name":"_localDecimals","type":"uint8"},{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"}],"name":"createPool","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"uint256","name":"_dstPoolId","type":"uint256"},{"internalType":"uint256","name":"_srcPoolId","type":"uint256"},{"components":[{"internalType":"uint256","name":"credits","type":"uint256"},{"internalType":"uint256","name":"idealBalance","type":"uint256"}],"internalType":"struct Pool.CreditObj","name":"_c","type":"tuple"}],"name":"creditChainPath","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"contract Factory","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcPoolId","type":"uint16"},{"internalType":"uint256","name":"_amountLP","type":"uint256"},{"internalType":"address","name":"_to","type":"address"}],"name":"instantRedeemLocal","outputs":[{"internalType":"uint256","name":"amountSD","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"mintFeeOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"protocolFeeOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"uint8","name":"_functionType","type":"uint8"},{"internalType":"bytes","name":"_toAddress","type":"bytes"},{"internalType":"bytes","name":"_transferAndCallPayload","type":"bytes"},{"components":[{"internalType":"uint256","name":"dstGasForCall","type":"uint256"},{"internalType":"uint256","name":"dstNativeAmount","type":"uint256"},{"internalType":"bytes","name":"dstNativeAddr","type":"bytes"}],"internalType":"struct IStargateRouter.lzTxObj","name":"_lzTxParams","type":"tuple"}],"name":"quoteLayerZeroFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"uint256","name":"_srcPoolId","type":"uint256"},{"internalType":"uint256","name":"_dstPoolId","type":"uint256"},{"internalType":"address payable","name":"_refundAddress","type":"address"},{"internalType":"uint256","name":"_amountLP","type":"uint256"},{"internalType":"bytes","name":"_to","type":"bytes"},{"components":[{"internalType":"uint256","name":"dstGasForCall","type":"uint256"},{"internalType":"uint256","name":"dstNativeAmount","type":"uint256"},{"internalType":"bytes","name":"dstNativeAddr","type":"bytes"}],"internalType":"struct IStargateRouter.lzTxObj","name":"_lzTxParams","type":"tuple"}],"name":"redeemLocal","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"internalType":"uint256","name":"_nonce","type":"uint256"},{"internalType":"uint256","name":"_srcPoolId","type":"uint256"},{"internalType":"uint256","name":"_dstPoolId","type":"uint256"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amountSD","type":"uint256"},{"internalType":"uint256","name":"_mintAmountSD","type":"uint256"}],"name":"redeemLocalCallback","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"internalType":"uint256","name":"_nonce","type":"uint256"},{"internalType":"uint256","name":"_srcPoolId","type":"uint256"},{"internalType":"uint256","name":"_dstPoolId","type":"uint256"},{"internalType":"uint256","name":"_amountSD","type":"uint256"},{"internalType":"bytes","name":"_to","type":"bytes"}],"name":"redeemLocalCheckOnRemote","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"uint256","name":"_srcPoolId","type":"uint256"},{"internalType":"uint256","name":"_dstPoolId","type":"uint256"},{"internalType":"address payable","name":"_refundAddress","type":"address"},{"internalType":"uint256","name":"_amountLP","type":"uint256"},{"internalType":"uint256","name":"_minAmountLD","type":"uint256"},{"internalType":"bytes","name":"_to","type":"bytes"},{"components":[{"internalType":"uint256","name":"dstGasForCall","type":"uint256"},{"internalType":"uint256","name":"dstNativeAmount","type":"uint256"},{"internalType":"bytes","name":"dstNativeAddr","type":"bytes"}],"internalType":"struct IStargateRouter.lzTxObj","name":"_lzTxParams","type":"tuple"}],"name":"redeemRemote","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"internalType":"uint256","name":"_nonce","type":"uint256"}],"name":"retryRevert","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"},{"internalType":"bytes","name":"","type":"bytes"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"revertLookup","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"internalType":"uint256","name":"_nonce","type":"uint256"},{"internalType":"address payable","name":"_refundAddress","type":"address"},{"components":[{"internalType":"uint256","name":"dstGasForCall","type":"uint256"},{"internalType":"uint256","name":"dstNativeAmount","type":"uint256"},{"internalType":"bytes","name":"dstNativeAddr","type":"bytes"}],"internalType":"struct IStargateRouter.lzTxObj","name":"_lzTxParams","type":"tuple"}],"name":"revertRedeemLocal","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"uint256","name":"_srcPoolId","type":"uint256"},{"internalType":"uint256","name":"_dstPoolId","type":"uint256"},{"internalType":"address payable","name":"_refundAddress","type":"address"}],"name":"sendCredits","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"contract Bridge","name":"_bridge","type":"address"},{"internalType":"contract Factory","name":"_factory","type":"address"}],"name":"setBridgeAndFactory","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_poolId","type":"uint256"},{"internalType":"bool","name":"_batched","type":"bool"},{"internalType":"uint256","name":"_swapDeltaBP","type":"uint256"},{"internalType":"uint256","name":"_lpDeltaBP","type":"uint256"},{"internalType":"bool","name":"_defaultSwapMode","type":"bool"},{"internalType":"bool","name":"_defaultLPMode","type":"bool"}],"name":"setDeltaParam","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_poolId","type":"uint256"},{"internalType":"address","name":"_feeLibraryAddr","type":"address"}],"name":"setFeeLibrary","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_poolId","type":"uint256"},{"internalType":"uint256","name":"_mintFeeBP","type":"uint256"}],"name":"setFees","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"}],"name":"setMintFeeOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"}],"name":"setProtocolFeeOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_poolId","type":"uint256"},{"internalType":"bool","name":"_swapStop","type":"bool"}],"name":"setSwapStop","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_poolId","type":"uint256"},{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"uint256","name":"_dstPoolId","type":"uint256"},{"internalType":"uint16","name":"_weight","type":"uint16"}],"name":"setWeightForChainPath","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"uint256","name":"_srcPoolId","type":"uint256"},{"internalType":"uint256","name":"_dstPoolId","type":"uint256"},{"internalType":"address payable","name":"_refundAddress","type":"address"},{"internalType":"uint256","name":"_amountLD","type":"uint256"},{"internalType":"uint256","name":"_minAmountLD","type":"uint256"},{"components":[{"internalType":"uint256","name":"dstGasForCall","type":"uint256"},{"internalType":"uint256","name":"dstNativeAmount","type":"uint256"},{"internalType":"bytes","name":"dstNativeAddr","type":"bytes"}],"internalType":"struct IStargateRouter.lzTxObj","name":"_lzTxParams","type":"tuple"},{"internalType":"bytes","name":"_to","type":"bytes"},{"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"swap","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"internalType":"uint256","name":"_nonce","type":"uint256"},{"internalType":"uint256","name":"_srcPoolId","type":"uint256"},{"internalType":"uint256","name":"_dstPoolId","type":"uint256"},{"internalType":"uint256","name":"_dstGasForCall","type":"uint256"},{"internalType":"address","name":"_to","type":"address"},{"components":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"eqFee","type":"uint256"},{"internalType":"uint256","name":"eqReward","type":"uint256"},{"internalType":"uint256","name":"lpFee","type":"uint256"},{"internalType":"uint256","name":"protocolFee","type":"uint256"},{"internalType":"uint256","name":"lkbRemove","type":"uint256"}],"internalType":"struct Pool.SwapObj","name":"_s","type":"tuple"},{"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"swapRemote","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_poolId","type":"uint256"},{"internalType":"address","name":"_to","type":"address"}],"name":"withdrawMintFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_poolId","type":"uint256"},{"internalType":"address","name":"_to","type":"address"}],"name":"withdrawProtocolFee","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
abi_usdt = '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_user","type":"address"}],"name":"BlockPlaced","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_user","type":"address"}],"name":"BlockReleased","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_blockedUser","type":"address"},{"indexed":false,"internalType":"uint256","name":"_balance","type":"uint256"}],"name":"DestroyedBlockedFunds","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_destination","type":"address"},{"indexed":false,"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_contract","type":"address"}],"name":"NewPrivilegedContract","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"Redeem","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_contract","type":"address"}],"name":"RemovedPrivilegedContract","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_trustedDeFiContract","type":"address"}],"name":"addPrivilegedContract","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"addToBlockedList","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"},{"internalType":"address","name":"_spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"bridgeBurn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"bridgeMint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_blockedUser","type":"address"}],"name":"destroyBlockedFunds","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"uint8","name":"_decimals","type":"uint8"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"uint8","name":"_decimals","type":"uint8"},{"internalType":"address","name":"_l2Gateway","type":"address"},{"internalType":"address","name":"_l1Counterpart","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"isBlocked","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"isTrusted","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"l1Address","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"l2Gateway","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_destination","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"_recipients","type":"address[]"},{"internalType":"uint256[]","name":"_values","type":"uint256[]"}],"name":"multiTransfer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"redeem","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"removeFromBlockedList","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_trustedDeFiContract","type":"address"}],"name":"removePrivilegedContract","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_recipient","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_sender","type":"address"},{"internalType":"address","name":"_recipient","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}]'

arb = {
    'name':'Arbitrum',
    'RPC':'https://arb1.arbitrum.io/rpc',
    'USDT': {'adress' : '0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9',
            'abi' : abi_usdt,
            'decimal': 6,},
    'nomer': 110,
    'stargate': '0x53bf833a5d6c4dda888f69c22c88c9f356a41614',
    'token': 1000000,
    '1':2,
    '2':2,
    'gas': 2500000
}

avax = {
    'name':'Avax',
    'RPC':'https://avalanche-c-chain.publicnode.com/',
    'USDT': {'adress':'0x9702230A8Ea53601f5cD2dc00fDBc13d4dF4A8c7',
            'abi' : abi_usdt,
            'decimal': 6,},
    'nomer': 106,
    'stargate': '0x45a01e4e04f14f7a4a6702c74187c5f6222033cd',
    'token': 1000000,
    '1':2,
    '2':2,
    'gas': 410000
}

bsc = {
    'name':'Bep20',
    'RPC':'https://bsc-dataseed1.defibit.io/',
    'USDT': { 'adress': '0x55d398326f99059fF775485246999027B3197955',
            'abi' : abi_usdt,
            'decimal': 18,},
    'nomer': 102,
    'stargate': '0x4a364f8c717cAAD9A442737Eb7b8A55cc6cf18D8',
    'token': 1000000000000000000,
    '1':2,
    '2':2,
    'gas': 450000
}

poligon = {
    'name':'poligon',
    'RPC':'https://polygon-rpc.com',
    'USDT': {'adress' : '0xc2132D05D31c914a87C6611C10748AEb04B58e8F',
            'abi' : abi_usdt,
            'decimal': 6,},
    'nomer': 109,
    'stargate': '0x45A01E4e04F14f7A4a6702c74187c5F6222033cd',
    'token': 1000000,
    '1':2,
    '2':2,
    'gas': 450000
}

def s(ti):
    time.sleep(ti)

def adress_birgh():
    try:
        ish = open('adres_birgh.txt','r').readlines()
        private = open('adres_birgh.txt','r').read().splitlines()
        wallet = private[00]
        del ish[00]
        with open("adres_birgh.txt", "w") as file:
            file.writelines(ish)
        return wallet
    except:
        print('Кошельки для вывода кончились')

def wallett():
    try:
        private = open('wal.txt','r').read().splitlines()
        wallet = private[00]
        return wallet
    except:
        print('Кошельки кончились')

def wallett_del():
    ish = open('wal.txt','r').readlines()
    del ish[00]
    with open("wal.txt", "w") as file:
        file.writelines(ish)

def res_balance(set,adres):
    w3 = Web3(Web3.HTTPProvider(set['RPC'])) 
    eth_balance = w3.eth.get_balance(adres)
    if eth_balance > 0:
        return 1
    else:
        return 0

def aka(privat):
    w3 = Web3(Web3.HTTPProvider('https://arb1.arbitrum.io/rpc'))
    account = w3.eth.account.from_key(privat)
    adress = account.address
    nativ = res_balance(arb,adress) +res_balance(avax,adress)+res_balance(bsc,adress)
    if nativ == 3:
        return adress,privat
    else:
        return 0,0

def status(tx_hash,set1):
    time.sleep(15)
    w3 = Web3(Web3.HTTPProvider(set1['RPC'])) 
    try:
        status_ = w3.eth.get_transaction_receipt(tx_hash)
        status  = status_["status"]
        return status
    except:
        print("ошибка")
        return 0 

def apruve(set,token,contract,ak): #работает 
    try:
        w3 = Web3(Web3.HTTPProvider(set['RPC'])) 
        apruv_adres_token = Web3.to_checksum_address(token['adress']) 
        apruv_adres_most = Web3.to_checksum_address(contract) 
        apruv_contrakt = w3.eth.contract(address=apruv_adres_token,abi=token['abi']) 
        amount_in = apruv_contrakt.functions.balanceOf(ak[0]).call()
        if amount_in == 0 :
            while True:
                time.sleep(10)
                amount_in = apruv_contrakt.functions.balanceOf(ak[0]).call()
                if amount_in != 0:
                    nonce = w3.eth.get_transaction_count(ak[0])
                    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
                    gas_price = w3.eth.gas_price
                    tx1 = apruv_contrakt.functions.approve(
                        apruv_adres_most,
                        amount_in
                    ).build_transaction({
                        'from': ak[0],
                        'gas': set['gas'],
                        'gasPrice': gas_price,
                        'nonce': nonce,
                    })
                    signed_txn = w3.eth.account.sign_transaction(tx1, private_key=ak[1])
                    x_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
                    #status(x_hash)
                    time.sleep(5)
                    break
        else:
            nonce = w3.eth.get_transaction_count(ak[0])
            w3.middleware_onion.inject(geth_poa_middleware, layer=0)
            gas_price = w3.eth.gas_price
            tx1 = apruv_contrakt.functions.approve(
                apruv_adres_most,
                amount_in
            ).build_transaction({
                'from': ak[0],
                'gas': set['gas'],
                'gasPrice': gas_price,
                'nonce': nonce,
            })
            signed_txn = w3.eth.account.sign_transaction(tx1, private_key=ak[1])
            x_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            #status(x_hash)
            time.sleep(5)
    except: 
        print('Ошибка апрува')
        

def stargate(ak): ##### gotov, no проверка баланса
    rand = [bsc,avax,poligon]
    r1 = random.choice(rand)
    rand.remove(r1)
    r2 = random.choice(rand)
    rand.remove(r2)
    r3 = random.choice(rand)
    while True:
        tx1 = st(arb,r1,ak)
        if tx1 != 1:
            s(600)
            tx1 = st(arb,r1,ak)
            if tx1 != 1:
                return arb
        s(t)
        tx2 = st(r1,r2,ak)
        if tx2 != 1:
            s(600)
            tx2 = st(r1,r2,ak)
            if tx2 != 1:
                return r1
        s(t)
        tx3 = st(r2,r3,ak)
        if tx3 != 1:
            s(600)
            tx3 = st(r2,r3,ak)
            if tx3 != 1:
                return r2
        s(t)
        tx4 = st(r3,arb,ak)
        if tx4 != 1:
            s(600)
            tx4 = st(r3,arb,ak) 
            if tx4 != 1:
                return r3 
        return arb
    

    # система рандомизации  
def st(set1,set2,ak):
    apruve(set1,set1['USDT'],set1['stargate'],ak)
    time.sleep(20)
    w3 = Web3(Web3.HTTPProvider(set1['RPC'])) 
    adres_token = Web3.to_checksum_address(set1['USDT']['adress']) 
    contrakt = w3.eth.contract(address=adres_token,abi=set1['USDT']['abi']) 
    balanse = contrakt.functions.balanceOf(ak[0]).call()
    balanse = balanse / (10**set1['USDT']['decimal'])
    if balanse == 0:
        time.sleep(15)
        balanse = contrakt.functions.balanceOf(ak[0]).call()
        balanse = balanse / (10**set1['USDT']['decimal'])
        if balanse == 0:
            time.sleep(20)
            balanse = contrakt.functions.balanceOf(ak[0]).call()
            balanse = balanse / (10**set1['USDT']['decimal'])
    w3 = Web3(Web3.HTTPProvider(set1['RPC']))
    contractToken = Web3.to_checksum_address(set1['stargate'])
    contract = w3.eth.contract(address=contractToken, abi=abi_stargate)
    nonce = w3.eth.get_transaction_count(ak[0])
    gas_price = w3.eth.gas_price
    monet = int(set1['token']*balanse)
    monet_min = int(monet *0.95)
    fees = contract.functions.quoteLayerZeroFee(
        set2['nomer'],
        1,
        "0x0000000000000000000000000000000000001010",
        "0x",
        [0, 0,
        "0x0000000000000000000000000000000000000001"]
    ).call()
    fee = fees[0]

    tx = contract.functions.swap(
        set2['nomer'],
        set1['1'],
        set1['2'],
        ak[0],
        monet,
        monet_min,
        [0,
        0,
        '0x0000000000000000000000000000000000000001'],
        ak[0],
        '0x'
    ).build_transaction(
        {
        'from': ak[0],
        'value': fee, 
        'gas': set1['gas'],
        'gasPrice': gas_price,
        'nonce': nonce,
        })

    signed_txn = w3.eth.account.sign_transaction(tx, private_key=ak[1])
    try:
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        time.sleep(5)
        f = status(tx_hash,set1)
        a1 = set1['name']
        if f != 0 :
            a2 = set2['name']
            print(f'выполнен перевод {balanse} USDT из {a1} в {a2} , {f}')
            return f
        else:
            return f 
    except:
        print(f'{set1} нехватка газа')
        print(f'выполнен перевод {balanse} USDT из {a1} в {a2}')
        return 0 

#вывод на биржу 
def ww(ak,seti=arb,apuve=True):
    if apuve == True:
        apruve(seti,seti['USDT'],seti['USDT']['adress'],ak)
        time.sleep(20)
    w3 = Web3(Web3.HTTPProvider(seti['RPC'])) 
    apruv_adres_token = Web3.to_checksum_address(seti['USDT']['adress']) 
    apruv_contrakt = w3.eth.contract(address=apruv_adres_token,abi=seti['USDT']['abi']) 
    amount_in = apruv_contrakt.functions.balanceOf(ak[0]).call()
    if amount_in != 0 :
        nonce = w3.eth.get_transaction_count(ak[0])
        adress_br = adress_birgh()
        apruv_br = Web3.to_checksum_address(adress_br) 
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        gas_price = w3.eth.gas_price
        tx1 = apruv_contrakt.functions.transfer(
            apruv_br,
            amount_in
        ).build_transaction({
            'from': ak[0],
            'gas': 400000,
            'gasPrice': gas_price,
            'nonce': nonce,
        })
        try:
            signed_txn = w3.eth.account.sign_transaction(tx1, private_key=ak[1])
            x_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f'Отправил на биржу {amount_in/10**6}')
            return True
        except:
            print(f'{ak[0]} , не хватило газа')
            return False
    else:
        s = seti['name']
        print(f'{ak[0]} в сети {s}  пустой')
        return False
    
def time_m(ad):
    while True:
        w3 = Web3(Web3.HTTPProvider(arb['RPC'])) 
        apruv_adres_token = Web3.to_checksum_address(arb['USDT']['adress']) 
        apruv_contrakt = w3.eth.contract(address=apruv_adres_token,abi=arb['USDT']['abi']) 
        balanse = apruv_contrakt.functions.balanceOf(ad[0]).call()
        if balanse > 0:
            break
        else:
            time.sleep(2)
#work
def ran(wal):
    sp = [stargate]
    ad = aka(wal)
    if ad[0] != 0:
        print('------------------------------------------')
        print(ad[0])
        #отправка с биржи и ожидание денег
        transfer.okx_withdraw(ad[0],10,12)
        #ожидаение денег
        time_m(ad)
        #начала старгейта
        while len(sp) != 0:
            l = random.choice(sp)
            TorF = l(ad)
            sp.remove(l)
        #вывод на биржу 
        ww(ad,TorF)
        print('------------------------------------------')
    else:
        print(f'{ad[0]} нет нативного токена')
    
def main():
    while True:
        #try:
            a = wallett()
            ran(a)
            wallett_del()
        #except:
            #break

main()
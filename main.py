import json
import math
import time

from web3 import Web3

from config import *

# w3 = Web3(Web3.HTTPProvider(INFURA_MAINNET))
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

pool_abi = json.loads(
    '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,'
    '"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"int24",'
    '"name":"tickLower","type":"int24"},{"indexed":true,"internalType":"int24","name":"tickUpper","type":"int24"},'
    '{"indexed":false,"internalType":"uint128","name":"amount","type":"uint128"},{"indexed":false,'
    '"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256",'
    '"name":"amount1","type":"uint256"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,'
    '"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"address",'
    '"name":"recipient","type":"address"},{"indexed":true,"internalType":"int24","name":"tickLower","type":"int24"},'
    '{"indexed":true,"internalType":"int24","name":"tickUpper","type":"int24"},{"indexed":false,'
    '"internalType":"uint128","name":"amount0","type":"uint128"},{"indexed":false,"internalType":"uint128",'
    '"name":"amount1","type":"uint128"}],"name":"Collect","type":"event"},{"anonymous":false,"inputs":[{'
    '"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":true,'
    '"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"uint128",'
    '"name":"amount0","type":"uint128"},{"indexed":false,"internalType":"uint128","name":"amount1",'
    '"type":"uint128"}],"name":"CollectProtocol","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,'
    '"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address",'
    '"name":"recipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0",'
    '"type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":false,'
    '"internalType":"uint256","name":"paid0","type":"uint256"},{"indexed":false,"internalType":"uint256",'
    '"name":"paid1","type":"uint256"}],"name":"Flash","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,'
    '"internalType":"uint16","name":"observationCardinalityNextOld","type":"uint16"},{"indexed":false,'
    '"internalType":"uint16","name":"observationCardinalityNextNew","type":"uint16"}],'
    '"name":"IncreaseObservationCardinalityNext","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,'
    '"internalType":"uint160","name":"sqrtPriceX96","type":"uint160"},{"indexed":false,"internalType":"int24",'
    '"name":"tick","type":"int24"}],"name":"Initialize","type":"event"},{"anonymous":false,"inputs":[{'
    '"indexed":false,"internalType":"address","name":"sender","type":"address"},{"indexed":true,'
    '"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"int24",'
    '"name":"tickLower","type":"int24"},{"indexed":true,"internalType":"int24","name":"tickUpper","type":"int24"},'
    '{"indexed":false,"internalType":"uint128","name":"amount","type":"uint128"},{"indexed":false,'
    '"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256",'
    '"name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,'
    '"internalType":"uint8","name":"feeProtocol0Old","type":"uint8"},{"indexed":false,"internalType":"uint8",'
    '"name":"feeProtocol1Old","type":"uint8"},{"indexed":false,"internalType":"uint8","name":"feeProtocol0New",'
    '"type":"uint8"},{"indexed":false,"internalType":"uint8","name":"feeProtocol1New","type":"uint8"}],'
    '"name":"SetFeeProtocol","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address",'
    '"name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"recipient","type":"address"},'
    '{"indexed":false,"internalType":"int256","name":"amount0","type":"int256"},{"indexed":false,'
    '"internalType":"int256","name":"amount1","type":"int256"},{"indexed":false,"internalType":"uint160",'
    '"name":"sqrtPriceX96","type":"uint160"},{"indexed":false,"internalType":"uint128","name":"liquidity",'
    '"type":"uint128"},{"indexed":false,"internalType":"int24","name":"tick","type":"int24"}],"name":"Swap",'
    '"type":"event"},{"inputs":[{"internalType":"int24","name":"tickLower","type":"int24"},{"internalType":"int24",'
    '"name":"tickUpper","type":"int24"},{"internalType":"uint128","name":"amount","type":"uint128"}],"name":"burn",'
    '"outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256",'
    '"name":"amount1","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{'
    '"internalType":"address","name":"recipient","type":"address"},{"internalType":"int24","name":"tickLower",'
    '"type":"int24"},{"internalType":"int24","name":"tickUpper","type":"int24"},{"internalType":"uint128",'
    '"name":"amount0Requested","type":"uint128"},{"internalType":"uint128","name":"amount1Requested",'
    '"type":"uint128"}],"name":"collect","outputs":[{"internalType":"uint128","name":"amount0","type":"uint128"},'
    '{"internalType":"uint128","name":"amount1","type":"uint128"}],"stateMutability":"nonpayable","type":"function"},'
    '{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint128",'
    '"name":"amount0Requested","type":"uint128"},{"internalType":"uint128","name":"amount1Requested",'
    '"type":"uint128"}],"name":"collectProtocol","outputs":[{"internalType":"uint128","name":"amount0",'
    '"type":"uint128"},{"internalType":"uint128","name":"amount1","type":"uint128"}],"stateMutability":"nonpayable",'
    '"type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"",'
    '"type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"fee","outputs":[{'
    '"internalType":"uint24","name":"","type":"uint24"}],"stateMutability":"view","type":"function"},{"inputs":[],'
    '"name":"feeGrowthGlobal0X128","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],'
    '"stateMutability":"view","type":"function"},{"inputs":[],"name":"feeGrowthGlobal1X128","outputs":[{'
    '"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{'
    '"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount0",'
    '"type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"},{"internalType":"bytes",'
    '"name":"data","type":"bytes"}],"name":"flash","outputs":[],"stateMutability":"nonpayable","type":"function"},'
    '{"inputs":[{"internalType":"uint16","name":"observationCardinalityNext","type":"uint16"}],'
    '"name":"increaseObservationCardinalityNext","outputs":[],"stateMutability":"nonpayable","type":"function"},'
    '{"inputs":[{"internalType":"uint160","name":"sqrtPriceX96","type":"uint160"}],"name":"initialize","outputs":[],'
    '"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"liquidity","outputs":[{'
    '"internalType":"uint128","name":"","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[],'
    '"name":"maxLiquidityPerTick","outputs":[{"internalType":"uint128","name":"","type":"uint128"}],'
    '"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient",'
    '"type":"address"},{"internalType":"int24","name":"tickLower","type":"int24"},{"internalType":"int24",'
    '"name":"tickUpper","type":"int24"},{"internalType":"uint128","name":"amount","type":"uint128"},'
    '{"internalType":"bytes","name":"data","type":"bytes"}],"name":"mint","outputs":[{"internalType":"uint256",'
    '"name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],'
    '"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"",'
    '"type":"uint256"}],"name":"observations","outputs":[{"internalType":"uint32","name":"blockTimestamp",'
    '"type":"uint32"},{"internalType":"int56","name":"tickCumulative","type":"int56"},{"internalType":"uint160",'
    '"name":"secondsPerLiquidityCumulativeX128","type":"uint160"},{"internalType":"bool","name":"initialized",'
    '"type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint32[]",'
    '"name":"secondsAgos","type":"uint32[]"}],"name":"observe","outputs":[{"internalType":"int56[]",'
    '"name":"tickCumulatives","type":"int56[]"},{"internalType":"uint160[]",'
    '"name":"secondsPerLiquidityCumulativeX128s","type":"uint160[]"}],"stateMutability":"view","type":"function"},'
    '{"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"positions","outputs":[{'
    '"internalType":"uint128","name":"liquidity","type":"uint128"},{"internalType":"uint256",'
    '"name":"feeGrowthInside0LastX128","type":"uint256"},{"internalType":"uint256","name":"feeGrowthInside1LastX128",'
    '"type":"uint256"},{"internalType":"uint128","name":"tokensOwed0","type":"uint128"},{"internalType":"uint128",'
    '"name":"tokensOwed1","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[],'
    '"name":"protocolFees","outputs":[{"internalType":"uint128","name":"token0","type":"uint128"},'
    '{"internalType":"uint128","name":"token1","type":"uint128"}],"stateMutability":"view","type":"function"},'
    '{"inputs":[{"internalType":"uint8","name":"feeProtocol0","type":"uint8"},{"internalType":"uint8",'
    '"name":"feeProtocol1","type":"uint8"}],"name":"setFeeProtocol","outputs":[],"stateMutability":"nonpayable",'
    '"type":"function"},{"inputs":[],"name":"slot0","outputs":[{"internalType":"uint160","name":"sqrtPriceX96",'
    '"type":"uint160"},{"internalType":"int24","name":"tick","type":"int24"},{"internalType":"uint16",'
    '"name":"observationIndex","type":"uint16"},{"internalType":"uint16","name":"observationCardinality",'
    '"type":"uint16"},{"internalType":"uint16","name":"observationCardinalityNext","type":"uint16"},'
    '{"internalType":"uint8","name":"feeProtocol","type":"uint8"},{"internalType":"bool","name":"unlocked",'
    '"type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int24",'
    '"name":"tickLower","type":"int24"},{"internalType":"int24","name":"tickUpper","type":"int24"}],'
    '"name":"snapshotCumulativesInside","outputs":[{"internalType":"int56","name":"tickCumulativeInside",'
    '"type":"int56"},{"internalType":"uint160","name":"secondsPerLiquidityInsideX128","type":"uint160"},'
    '{"internalType":"uint32","name":"secondsInside","type":"uint32"}],"stateMutability":"view","type":"function"},'
    '{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"bool",'
    '"name":"zeroForOne","type":"bool"},{"internalType":"int256","name":"amountSpecified","type":"int256"},'
    '{"internalType":"uint160","name":"sqrtPriceLimitX96","type":"uint160"},{"internalType":"bytes","name":"data",'
    '"type":"bytes"}],"name":"swap","outputs":[{"internalType":"int256","name":"amount0","type":"int256"},'
    '{"internalType":"int256","name":"amount1","type":"int256"}],"stateMutability":"nonpayable","type":"function"},'
    '{"inputs":[{"internalType":"int16","name":"","type":"int16"}],"name":"tickBitmap","outputs":[{'
    '"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],'
    '"name":"tickSpacing","outputs":[{"internalType":"int24","name":"","type":"int24"}],"stateMutability":"view",'
    '"type":"function"},{"inputs":[{"internalType":"int24","name":"","type":"int24"}],"name":"ticks","outputs":[{'
    '"internalType":"uint128","name":"liquidityGross","type":"uint128"},{"internalType":"int128",'
    '"name":"liquidityNet","type":"int128"},{"internalType":"uint256","name":"feeGrowthOutside0X128",'
    '"type":"uint256"},{"internalType":"uint256","name":"feeGrowthOutside1X128","type":"uint256"},'
    '{"internalType":"int56","name":"tickCumulativeOutside","type":"int56"},{"internalType":"uint160",'
    '"name":"secondsPerLiquidityOutsideX128","type":"uint160"},{"internalType":"uint32","name":"secondsOutside",'
    '"type":"uint32"},{"internalType":"bool","name":"initialized","type":"bool"}],"stateMutability":"view",'
    '"type":"function"},{"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"",'
    '"type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"token1","outputs":[{'
    '"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"}]')
pool_address = Web3.toChecksumAddress('0x4e68Ccd3E89f51C3074ca5072bbAC773960dFa36')
decimals_token_0 = 18
decimals_token_1 = 6
token0_abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],'
                        '"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{'
                        '"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":['
                        '{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable",'
                        '"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"",'
                        '"type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},'
                        '{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},'
                        '{"name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"",'
                        '"type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},'
                        '{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"withdraw","outputs":[],'
                        '"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,'
                        '"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,'
                        '"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"",'
                        '"type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],'
                        '"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],'
                        '"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,'
                        '"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"dst",'
                        '"type":"address"},{"name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"name":"",'
                        '"type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},'
                        '{"constant":false,"inputs":[],"name":"deposit","outputs":[],"payable":true,'
                        '"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"name":"",'
                        '"type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"",'
                        '"type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},'
                        '{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,'
                        '"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"guy",'
                        '"type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Approval",'
                        '"type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},'
                        '{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad",'
                        '"type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{'
                        '"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad",'
                        '"type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{'
                        '"indexed":true,"name":"src","type":"address"},{"indexed":false,"name":"wad",'
                        '"type":"uint256"}],"name":"Withdrawal","type":"event"}]')
token0_address = Web3.toChecksumAddress('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2')
token1_abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],'
                        '"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{'
                        '"name":"_upgradedAddress","type":"address"}],"name":"deprecate","outputs":[],'
                        '"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,'
                        '"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],'
                        '"name":"approve","outputs":[],"payable":false,"stateMutability":"nonpayable",'
                        '"type":"function"},{"constant":true,"inputs":[],"name":"deprecated","outputs":[{"name":"",'
                        '"type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},'
                        '{"constant":false,"inputs":[{"name":"_evilUser","type":"address"}],"name":"addBlackList",'
                        '"outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},'
                        '{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],'
                        '"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{'
                        '"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value",'
                        '"type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,'
                        '"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],'
                        '"name":"upgradedAddress","outputs":[{"name":"","type":"address"}],"payable":false,'
                        '"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"",'
                        '"type":"address"}],"name":"balances","outputs":[{"name":"","type":"uint256"}],'
                        '"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],'
                        '"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,'
                        '"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],'
                        '"name":"maximumFee","outputs":[{"name":"","type":"uint256"}],"payable":false,'
                        '"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],'
                        '"name":"_totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,'
                        '"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"unpause",'
                        '"outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},'
                        '{"constant":true,"inputs":[{"name":"_maker","type":"address"}],"name":"getBlackListStatus",'
                        '"outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view",'
                        '"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"",'
                        '"type":"address"}],"name":"allowed","outputs":[{"name":"","type":"uint256"}],'
                        '"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],'
                        '"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,'
                        '"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"who",'
                        '"type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],'
                        '"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],'
                        '"name":"pause","outputs":[],"payable":false,"stateMutability":"nonpayable",'
                        '"type":"function"},{"constant":true,"inputs":[],"name":"getOwner","outputs":[{"name":"",'
                        '"type":"address"}],"payable":false,"stateMutability":"view","type":"function"},'
                        '{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],'
                        '"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],'
                        '"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,'
                        '"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to",'
                        '"type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],'
                        '"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,'
                        '"inputs":[{"name":"newBasisPoints","type":"uint256"},{"name":"newMaxFee","type":"uint256"}],'
                        '"name":"setParams","outputs":[],"payable":false,"stateMutability":"nonpayable",'
                        '"type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],'
                        '"name":"issue","outputs":[],"payable":false,"stateMutability":"nonpayable",'
                        '"type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],'
                        '"name":"redeem","outputs":[],"payable":false,"stateMutability":"nonpayable",'
                        '"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},'
                        '{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining",'
                        '"type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},'
                        '{"constant":true,"inputs":[],"name":"basisPointsRate","outputs":[{"name":"",'
                        '"type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},'
                        '{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"isBlackListed","outputs":[{'
                        '"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},'
                        '{"constant":false,"inputs":[{"name":"_clearedUser","type":"address"}],'
                        '"name":"removeBlackList","outputs":[],"payable":false,"stateMutability":"nonpayable",'
                        '"type":"function"},{"constant":true,"inputs":[],"name":"MAX_UINT","outputs":[{"name":"",'
                        '"type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},'
                        '{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],'
                        '"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable",'
                        '"type":"function"},{"constant":false,"inputs":[{"name":"_blackListedUser",'
                        '"type":"address"}],"name":"destroyBlackFunds","outputs":[],"payable":false,'
                        '"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"_initialSupply",'
                        '"type":"uint256"},{"name":"_name","type":"string"},{"name":"_symbol","type":"string"},'
                        '{"name":"_decimals","type":"uint256"}],"payable":false,"stateMutability":"nonpayable",'
                        '"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"amount",'
                        '"type":"uint256"}],"name":"Issue","type":"event"},{"anonymous":false,"inputs":[{'
                        '"indexed":false,"name":"amount","type":"uint256"}],"name":"Redeem","type":"event"},'
                        '{"anonymous":false,"inputs":[{"indexed":false,"name":"newAddress","type":"address"}],'
                        '"name":"Deprecate","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,'
                        '"name":"feeBasisPoints","type":"uint256"},{"indexed":false,"name":"maxFee",'
                        '"type":"uint256"}],"name":"Params","type":"event"},{"anonymous":false,"inputs":[{'
                        '"indexed":false,"name":"_blackListedUser","type":"address"},{"indexed":false,'
                        '"name":"_balance","type":"uint256"}],"name":"DestroyedBlackFunds","type":"event"},'
                        '{"anonymous":false,"inputs":[{"indexed":false,"name":"_user","type":"address"}],'
                        '"name":"AddedBlackList","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,'
                        '"name":"_user","type":"address"}],"name":"RemovedBlackList","type":"event"},'
                        '{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},'
                        '{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value",'
                        '"type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{'
                        '"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to",'
                        '"type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer",'
                        '"type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},'
                        '{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"}]')
token1_address = Web3.toChecksumAddress('0xdAC17F958D2ee523a2206206994597C13D831ec7')
wallet_address = Web3.toChecksumAddress('0x5AB5bab28d1EA8c812B013B7fFF05112F298a25F')

swap_router_abi = json.loads(
    '[{"inputs":[{"internalType":"address","name":"_factoryV2","type":"address"},{"internalType":"address",'
    '"name":"factoryV3","type":"address"},{"internalType":"address","name":"_positionManager","type":"address"},'
    '{"internalType":"address","name":"_WETH9","type":"address"}],"stateMutability":"nonpayable",'
    '"type":"constructor"},{"inputs":[],"name":"WETH9","outputs":[{"internalType":"address","name":"",'
    '"type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address",'
    '"name":"token","type":"address"}],"name":"approveMax","outputs":[],"stateMutability":"payable",'
    '"type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"}],'
    '"name":"approveMaxMinusOne","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{'
    '"internalType":"address","name":"token","type":"address"}],"name":"approveZeroThenMax","outputs":[],'
    '"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token",'
    '"type":"address"}],"name":"approveZeroThenMaxMinusOne","outputs":[],"stateMutability":"payable",'
    '"type":"function"},{"inputs":[{"internalType":"bytes","name":"data","type":"bytes"}],'
    '"name":"callPositionManager","outputs":[{"internalType":"bytes","name":"result","type":"bytes"}],'
    '"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"bytes[]","name":"paths",'
    '"type":"bytes[]"},{"internalType":"uint128[]","name":"amounts","type":"uint128[]"},{"internalType":"uint24",'
    '"name":"maximumTickDivergence","type":"uint24"},{"internalType":"uint32","name":"secondsAgo","type":"uint32"}],'
    '"name":"checkOracleSlippage","outputs":[],"stateMutability":"view","type":"function"},{"inputs":[{'
    '"internalType":"bytes","name":"path","type":"bytes"},{"internalType":"uint24","name":"maximumTickDivergence",'
    '"type":"uint24"},{"internalType":"uint32","name":"secondsAgo","type":"uint32"}],"name":"checkOracleSlippage",'
    '"outputs":[],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"bytes",'
    '"name":"path","type":"bytes"},{"internalType":"address","name":"recipient","type":"address"},'
    '{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256",'
    '"name":"amountOutMinimum","type":"uint256"}],"internalType":"struct IV3SwapRouter.ExactInputParams",'
    '"name":"params","type":"tuple"}],"name":"exactInput","outputs":[{"internalType":"uint256","name":"amountOut",'
    '"type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{'
    '"internalType":"address","name":"tokenIn","type":"address"},{"internalType":"address","name":"tokenOut",'
    '"type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"address",'
    '"name":"recipient","type":"address"},{"internalType":"uint256","name":"amountIn","type":"uint256"},'
    '{"internalType":"uint256","name":"amountOutMinimum","type":"uint256"},{"internalType":"uint160",'
    '"name":"sqrtPriceLimitX96","type":"uint160"}],"internalType":"struct IV3SwapRouter.ExactInputSingleParams",'
    '"name":"params","type":"tuple"}],"name":"exactInputSingle","outputs":[{"internalType":"uint256",'
    '"name":"amountOut","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{'
    '"internalType":"bytes","name":"path","type":"bytes"},{"internalType":"address","name":"recipient",'
    '"type":"address"},{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256",'
    '"name":"amountInMaximum","type":"uint256"}],"internalType":"struct IV3SwapRouter.ExactOutputParams",'
    '"name":"params","type":"tuple"}],"name":"exactOutput","outputs":[{"internalType":"uint256","name":"amountIn",'
    '"type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{'
    '"internalType":"address","name":"tokenIn","type":"address"},{"internalType":"address","name":"tokenOut",'
    '"type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"address",'
    '"name":"recipient","type":"address"},{"internalType":"uint256","name":"amountOut","type":"uint256"},'
    '{"internalType":"uint256","name":"amountInMaximum","type":"uint256"},{"internalType":"uint160",'
    '"name":"sqrtPriceLimitX96","type":"uint160"}],"internalType":"struct IV3SwapRouter.ExactOutputSingleParams",'
    '"name":"params","type":"tuple"}],"name":"exactOutputSingle","outputs":[{"internalType":"uint256",'
    '"name":"amountIn","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],'
    '"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view",'
    '"type":"function"},{"inputs":[],"name":"factoryV2","outputs":[{"internalType":"address","name":"",'
    '"type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address",'
    '"name":"token","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],'
    '"name":"getApprovalType","outputs":[{"internalType":"enum IApproveAndCall.ApprovalType","name":"",'
    '"type":"uint8"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{'
    '"internalType":"address","name":"token0","type":"address"},{"internalType":"address","name":"token1",'
    '"type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256",'
    '"name":"amount0Min","type":"uint256"},{"internalType":"uint256","name":"amount1Min","type":"uint256"}],'
    '"internalType":"struct IApproveAndCall.IncreaseLiquidityParams","name":"params","type":"tuple"}],'
    '"name":"increaseLiquidity","outputs":[{"internalType":"bytes","name":"result","type":"bytes"}],'
    '"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"internalType":"address",'
    '"name":"token0","type":"address"},{"internalType":"address","name":"token1","type":"address"},'
    '{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"int24","name":"tickLower",'
    '"type":"int24"},{"internalType":"int24","name":"tickUpper","type":"int24"},{"internalType":"uint256",'
    '"name":"amount0Min","type":"uint256"},{"internalType":"uint256","name":"amount1Min","type":"uint256"},'
    '{"internalType":"address","name":"recipient","type":"address"}],"internalType":"struct '
    'IApproveAndCall.MintParams","name":"params","type":"tuple"}],"name":"mint","outputs":[{"internalType":"bytes",'
    '"name":"result","type":"bytes"}],"stateMutability":"payable","type":"function"},{"inputs":[{'
    '"internalType":"bytes32","name":"previousBlockhash","type":"bytes32"},{"internalType":"bytes[]","name":"data",'
    '"type":"bytes[]"}],"name":"multicall","outputs":[{"internalType":"bytes[]","name":"","type":"bytes[]"}],'
    '"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"deadline",'
    '"type":"uint256"},{"internalType":"bytes[]","name":"data","type":"bytes[]"}],"name":"multicall","outputs":[{'
    '"internalType":"bytes[]","name":"","type":"bytes[]"}],"stateMutability":"payable","type":"function"},{"inputs":['
    '{"internalType":"bytes[]","name":"data","type":"bytes[]"}],"name":"multicall","outputs":[{"internalType":"bytes['
    ']","name":"results","type":"bytes[]"}],"stateMutability":"payable","type":"function"},{"inputs":[],'
    '"name":"positionManager","outputs":[{"internalType":"address","name":"","type":"address"}],'
    '"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"token",'
    '"type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"pull","outputs":[],'
    '"stateMutability":"payable","type":"function"},{"inputs":[],"name":"refundETH","outputs":[],'
    '"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token",'
    '"type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256",'
    '"name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},'
    '{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],'
    '"name":"selfPermit","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{'
    '"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"nonce",'
    '"type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint8",'
    '"name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32",'
    '"name":"s","type":"bytes32"}],"name":"selfPermitAllowed","outputs":[],"stateMutability":"payable",'
    '"type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},'
    '{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint256","name":"expiry",'
    '"type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r",'
    '"type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"selfPermitAllowedIfNecessary",'
    '"outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token",'
    '"type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256",'
    '"name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},'
    '{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],'
    '"name":"selfPermitIfNecessary","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{'
    '"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin",'
    '"type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address",'
    '"name":"to","type":"address"}],"name":"swapExactTokensForTokens","outputs":[{"internalType":"uint256",'
    '"name":"amountOut","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{'
    '"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax",'
    '"type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address",'
    '"name":"to","type":"address"}],"name":"swapTokensForExactTokens","outputs":[{"internalType":"uint256",'
    '"name":"amountIn","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{'
    '"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountMinimum",'
    '"type":"uint256"},{"internalType":"address","name":"recipient","type":"address"}],"name":"sweepToken",'
    '"outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token",'
    '"type":"address"},{"internalType":"uint256","name":"amountMinimum","type":"uint256"}],"name":"sweepToken",'
    '"outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token",'
    '"type":"address"},{"internalType":"uint256","name":"amountMinimum","type":"uint256"},{"internalType":"uint256",'
    '"name":"feeBips","type":"uint256"},{"internalType":"address","name":"feeRecipient","type":"address"}],'
    '"name":"sweepTokenWithFee","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{'
    '"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountMinimum",'
    '"type":"uint256"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256",'
    '"name":"feeBips","type":"uint256"},{"internalType":"address","name":"feeRecipient","type":"address"}],'
    '"name":"sweepTokenWithFee","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{'
    '"internalType":"int256","name":"amount0Delta","type":"int256"},{"internalType":"int256","name":"amount1Delta",'
    '"type":"int256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"uniswapV3SwapCallback",'
    '"outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256",'
    '"name":"amountMinimum","type":"uint256"},{"internalType":"address","name":"recipient","type":"address"}],'
    '"name":"unwrapWETH9","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{'
    '"internalType":"uint256","name":"amountMinimum","type":"uint256"}],"name":"unwrapWETH9","outputs":[],'
    '"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountMinimum",'
    '"type":"uint256"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256",'
    '"name":"feeBips","type":"uint256"},{"internalType":"address","name":"feeRecipient","type":"address"}],'
    '"name":"unwrapWETH9WithFee","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{'
    '"internalType":"uint256","name":"amountMinimum","type":"uint256"},{"internalType":"uint256","name":"feeBips",'
    '"type":"uint256"},{"internalType":"address","name":"feeRecipient","type":"address"}],'
    '"name":"unwrapWETH9WithFee","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{'
    '"internalType":"uint256","name":"value","type":"uint256"}],"name":"wrapETH","outputs":[],'
    '"stateMutability":"payable","type":"function"},{"stateMutability":"payable","type":"receive"}]')
swap_router_address = Web3.toChecksumAddress('0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45')
swap_router = w3.eth.contract(address=swap_router_address, abi=swap_router_abi)
nonfungible_position_manager_abi = json.loads(
    '[{"inputs":[{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address",'
    '"name":"_WETH9","type":"address"},{"internalType":"address","name":"_tokenDescriptor_","type":"address"}],'
    '"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,'
    '"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address",'
    '"name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId",'
    '"type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,'
    '"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address",'
    '"name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],'
    '"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256",'
    '"name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"address","name":"recipient",'
    '"type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,'
    '"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Collect","type":"event"},'
    '{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},'
    '{"indexed":false,"internalType":"uint128","name":"liquidity","type":"uint128"},{"indexed":false,'
    '"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256",'
    '"name":"amount1","type":"uint256"}],"name":"DecreaseLiquidity","type":"event"},{"anonymous":false,"inputs":[{'
    '"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,'
    '"internalType":"uint128","name":"liquidity","type":"uint128"},{"indexed":false,"internalType":"uint256",'
    '"name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1",'
    '"type":"uint256"}],"name":"IncreaseLiquidity","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,'
    '"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to",'
    '"type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],'
    '"name":"Transfer","type":"event"},{"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32",'
    '"name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PERMIT_TYPEHASH",'
    '"outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},'
    '{"inputs":[],"name":"WETH9","outputs":[{"internalType":"address","name":"","type":"address"}],'
    '"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},'
    '{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],'
    '"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner",'
    '"type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],'
    '"stateMutability":"view","type":"function"},{"inputs":[],"name":"baseURI","outputs":[{"internalType":"string",'
    '"name":"","type":"string"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256",'
    '"name":"tokenId","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"payable","type":"function"},'
    '{"inputs":[{"components":[{"internalType":"uint256","name":"tokenId","type":"uint256"},'
    '{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint128","name":"amount0Max",'
    '"type":"uint128"},{"internalType":"uint128","name":"amount1Max","type":"uint128"}],"internalType":"struct '
    'INonfungiblePositionManager.CollectParams","name":"params","type":"tuple"}],"name":"collect","outputs":[{'
    '"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1",'
    '"type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address",'
    '"name":"token0","type":"address"},{"internalType":"address","name":"token1","type":"address"},'
    '{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"uint160","name":"sqrtPriceX96",'
    '"type":"uint160"}],"name":"createAndInitializePoolIfNecessary","outputs":[{"internalType":"address",'
    '"name":"pool","type":"address"}],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{'
    '"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint128","name":"liquidity",'
    '"type":"uint128"},{"internalType":"uint256","name":"amount0Min","type":"uint256"},{"internalType":"uint256",'
    '"name":"amount1Min","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"}],'
    '"internalType":"struct INonfungiblePositionManager.DecreaseLiquidityParams","name":"params","type":"tuple"}],'
    '"name":"decreaseLiquidity","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},'
    '{"internalType":"uint256","name":"amount1","type":"uint256"}],"stateMutability":"payable","type":"function"},'
    '{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],'
    '"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId",'
    '"type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],'
    '"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"uint256",'
    '"name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"amount0Desired","type":"uint256"},'
    '{"internalType":"uint256","name":"amount1Desired","type":"uint256"},{"internalType":"uint256",'
    '"name":"amount0Min","type":"uint256"},{"internalType":"uint256","name":"amount1Min","type":"uint256"},'
    '{"internalType":"uint256","name":"deadline","type":"uint256"}],"internalType":"struct '
    'INonfungiblePositionManager.IncreaseLiquidityParams","name":"params","type":"tuple"}],'
    '"name":"increaseLiquidity","outputs":[{"internalType":"uint128","name":"liquidity","type":"uint128"},'
    '{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1",'
    '"type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address",'
    '"name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],'
    '"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view",'
    '"type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"token0","type":"address"},'
    '{"internalType":"address","name":"token1","type":"address"},{"internalType":"uint24","name":"fee",'
    '"type":"uint24"},{"internalType":"int24","name":"tickLower","type":"int24"},{"internalType":"int24",'
    '"name":"tickUpper","type":"int24"},{"internalType":"uint256","name":"amount0Desired","type":"uint256"},'
    '{"internalType":"uint256","name":"amount1Desired","type":"uint256"},{"internalType":"uint256",'
    '"name":"amount0Min","type":"uint256"},{"internalType":"uint256","name":"amount1Min","type":"uint256"},'
    '{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"deadline",'
    '"type":"uint256"}],"internalType":"struct INonfungiblePositionManager.MintParams","name":"params",'
    '"type":"tuple"}],"name":"mint","outputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},'
    '{"internalType":"uint128","name":"liquidity","type":"uint128"},{"internalType":"uint256","name":"amount0",'
    '"type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"stateMutability":"payable",'
    '"type":"function"},{"inputs":[{"internalType":"bytes[]","name":"data","type":"bytes[]"}],"name":"multicall",'
    '"outputs":[{"internalType":"bytes[]","name":"results","type":"bytes[]"}],"stateMutability":"payable",'
    '"type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],'
    '"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId",'
    '"type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],'
    '"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender",'
    '"type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256",'
    '"name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},'
    '{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],'
    '"name":"permit","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{'
    '"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"positions","outputs":[{'
    '"internalType":"uint96","name":"nonce","type":"uint96"},{"internalType":"address","name":"operator",'
    '"type":"address"},{"internalType":"address","name":"token0","type":"address"},{"internalType":"address",'
    '"name":"token1","type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"},'
    '{"internalType":"int24","name":"tickLower","type":"int24"},{"internalType":"int24","name":"tickUpper",'
    '"type":"int24"},{"internalType":"uint128","name":"liquidity","type":"uint128"},{"internalType":"uint256",'
    '"name":"feeGrowthInside0LastX128","type":"uint256"},{"internalType":"uint256","name":"feeGrowthInside1LastX128",'
    '"type":"uint256"},{"internalType":"uint128","name":"tokensOwed0","type":"uint128"},{"internalType":"uint128",'
    '"name":"tokensOwed1","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[],'
    '"name":"refundETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{'
    '"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to",'
    '"type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom",'
    '"outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address",'
    '"name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},'
    '{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data",'
    '"type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},'
    '{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"value",'
    '"type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8",'
    '"name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32",'
    '"name":"s","type":"bytes32"}],"name":"selfPermit","outputs":[],"stateMutability":"payable","type":"function"},'
    '{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"nonce",'
    '"type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint8",'
    '"name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32",'
    '"name":"s","type":"bytes32"}],"name":"selfPermitAllowed","outputs":[],"stateMutability":"payable",'
    '"type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},'
    '{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint256","name":"expiry",'
    '"type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r",'
    '"type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"selfPermitAllowedIfNecessary",'
    '"outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token",'
    '"type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256",'
    '"name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},'
    '{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],'
    '"name":"selfPermitIfNecessary","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{'
    '"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved",'
    '"type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},'
    '{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface",'
    '"outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},'
    '{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256",'
    '"name":"amountMinimum","type":"uint256"},{"internalType":"address","name":"recipient","type":"address"}],'
    '"name":"sweepToken","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"symbol",'
    '"outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},'
    '{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{'
    '"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{'
    '"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index",'
    '"type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"",'
    '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256",'
    '"name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"",'
    '"type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{'
    '"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{'
    '"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to",'
    '"type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom",'
    '"outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256",'
    '"name":"amount0Owed","type":"uint256"},{"internalType":"uint256","name":"amount1Owed","type":"uint256"},'
    '{"internalType":"bytes","name":"data","type":"bytes"}],"name":"uniswapV3MintCallback","outputs":[],'
    '"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountMinimum",'
    '"type":"uint256"},{"internalType":"address","name":"recipient","type":"address"}],"name":"unwrapWETH9",'
    '"outputs":[],"stateMutability":"payable","type":"function"},{"stateMutability":"payable","type":"receive"}]')
nonfungible_position_manager_address = Web3.toChecksumAddress('0xC36442b4a4522E871399CD717aBDD847Ab11FE88')
nonfungible_position_manager = w3.eth.contract(address=nonfungible_position_manager_address,
                                               abi=nonfungible_position_manager_abi)
pool = w3.eth.contract(address=pool_address, abi=pool_abi)
token0 = w3.eth.contract(address=token0_address, abi=token0_abi)
token1 = w3.eth.contract(address=token1_address, abi=token1_abi)
tick_spacing = pool.functions.tickSpacing().call()
pair_fee = pool.functions.fee().call()
chain_id = 5777


def get_current_price():
    slot0 = pool.functions.slot0().call()
    sqrt_price_x96 = slot0[0]
    return sqrt_price_x96 * sqrt_price_x96 * (10 ** decimals_token_0) / (10 ** decimals_token_1) / 2 ** 192


def log_with_base(y, x):
    return math.log(y) / math.log(x)


def price_to_tick(price):
    # val_to_log = float(price) * pow(10, (decimals_token_0 - decimals_token_1))
    val_to_log = float(price) * pow(10, (decimals_token_1 - decimals_token_0))
    tick_id = math.log(val_to_log) / math.log(1.0001)
    return round(tick_id, 0)


def tokens_for_strategy(min_range, max_range, investment, price):
    decimal = decimals_token_1 - decimals_token_0
    sqrt_price = math.sqrt(price * (pow(10, decimal)))
    sqrt_low = math.sqrt(min_range * (pow(10, decimal)))
    sqrt_high = math.sqrt(max_range * (pow(10, decimal)))

    if sqrt_low < sqrt_price < sqrt_high:

        delta = investment / (
                (sqrt_price - sqrt_low) + (((1 / sqrt_price) - (1 / sqrt_high)) * (price * pow(10, decimal))))
        amount1 = delta * (sqrt_price - sqrt_low)
        amount0 = delta * ((1 / sqrt_price) - (1 / sqrt_high)) * pow(10, decimal)

    elif sqrt_price <= sqrt_low:
        delta = investment / (((1 / sqrt_low) - (1 / sqrt_high)) * price)
        amount1 = 0
        amount0 = delta * ((1 / sqrt_low) - (1 / sqrt_high))

    elif sqrt_price >= sqrt_high:
        delta = investment / (sqrt_high - sqrt_low)
        amount1 = delta * (sqrt_high - sqrt_low)
        amount0 = 0

    return [amount0, amount1]


def remove_liquidity():
    position_id = nonfungible_position_manager.functions.balanceOf(wallet_address).call()
    position = nonfungible_position_manager.functions.positions(position_id).call()
    tx = nonfungible_position_manager.functions.approve(pool, position_id).buildTransaction(
        {
            "gasPrice": w3.eth.gas_price,
            "chainId": chain_id,
            'from': wallet_address,
            'gas': 300000,
            'nonce': w3.eth.getTransactionCount(wallet_address),
        }
    )
    sign_and_send(tx)
    tx = pool.functions.burn(position[5], position[6], (1 << 128) - 1).buildTransaction()
    return sign_and_send(tx)


def sign_and_send(tx):
    signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return w3.toHex(tx_hash)


def swap(zero_for_one, amount, fee, amount_out_minimum, sqrt_price_limit_x96):
    if zero_for_one:
        token_in = token0
        token_out = token1
        decimal = decimals_token_0
    else:
        token_in = token1
        token_out = token0
        decimal = decimals_token_1
    approve(token_in, swap_router_address)
    params = {
        'tokenIn': token_in.address,
        'tokenOut': token_out.address,
        'fee': fee,
        'recipient': wallet_address,
        'deadline': round(time.time()) + 60 * 20,
        'amountIn': int(amount * (10 ** decimal)),
        'amountOutMinimum': amount_out_minimum,
        'sqrtPriceLimitX96': sqrt_price_limit_x96
    }
    tx = swap_router.functions.exactInputSingle(params).buildTransaction(
        {
            "gasPrice": w3.eth.gas_price,
            "chainId": chain_id,
            'from': wallet_address,
            'gas': 300000,
            'nonce': w3.eth.getTransactionCount(wallet_address),
            'value': amount * (10 ** decimal),
        }
    )
    return sign_and_send(tx)


def approve(token, spender_address):
    max_amount = w3.toWei(2 ** 64 - 1, 'ether')
    tx = token.functions.approve(spender_address, max_amount).buildTransaction({
        "gasPrice": w3.eth.gas_price,
        "chainId": chain_id,
        'from': wallet_address,
        'gas': 200000,
        'nonce': w3.eth.getTransactionCount(wallet_address)
    })
    return sign_and_send(tx)


def add_liquidity(token0_amount, token1_amount, tick_lower, tick_upper):
    params = {
        'token0': token0_address,
        'token1': token1_address,
        'fee': pair_fee,
        'tickLower': tick_lower,
        'tickUpper': tick_upper,
        'amount0Desired': int(token0_amount * (10 ** decimals_token_0)),
        'amount1Desired': int(token1_amount * (10 ** decimals_token_1)),
        'amount0Min': 0,
        'amount1Min': 0,
        'recipient': wallet_address,
        'deadline': round(time.time()) + 60 * 20
    }
    approve(token0, nonfungible_position_manager_address)
    approve(token1, nonfungible_position_manager_address)
    tx = nonfungible_position_manager.functions.mint(params).buildTransaction({
        "gasPrice": w3.eth.gas_price,
        "chainId": chain_id,
        'from': wallet_address,
        'gas': 300000,
        'nonce': w3.eth.getTransactionCount(wallet_address)
    })
    return sign_and_send(tx)


# swap
# print('before')
# print(token0.functions.balanceOf(wallet_address).call() / (10 ** decimals_token_0))
# print(token1.functions.balanceOf(wallet_address).call() / (10 ** decimals_token_1))
# print(swap(True, 20, pair_fee, 0, 0))
# print('after')
# print(token0.functions.balanceOf(wallet_address).call() / (10 ** decimals_token_0))
# print(token1.functions.balanceOf(wallet_address).call() / (10 ** decimals_token_1))

# add liquidity
print('before')
print(token0.functions.balanceOf(wallet_address).call() / (10 ** decimals_token_0))
print(token1.functions.balanceOf(wallet_address).call() / (10 ** decimals_token_1))
slot0 = pool.functions.slot0().call()
price = get_current_price()
print(add_liquidity(5, 5 * price, slot0[1] - 5 * tick_spacing, slot0[1] + 5 * tick_spacing))
print('after')
print(token0.functions.balanceOf(wallet_address).call() / (10 ** decimals_token_0))
print(token1.functions.balanceOf(wallet_address).call() / (10 ** decimals_token_1))

from typing import List

from . import construction_material_trade_symbol, market_transaction, market_trade_good

class MarketExport:
    symbol: construction_material_trade_symbol
    name: str
    description: str

class Market:
    symbol: str
    exports: List[MarketExport]
    imports: List[MarketExport]
    exchange: List[MarketExport]
    transactions: List[market_transaction]
    tradeGoods: List[market_trade_good]

market = Market
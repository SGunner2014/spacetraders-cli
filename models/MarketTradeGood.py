from typing import Literal

from . import construction_material_trade_symbol

class MarketTradeGood:
    symbol: construction_material_trade_symbol
    type_: Literal["EXPORT", "IMPORT", "EXCHANGE"]
    tradeVolume: int
    supply: Literal["SCARCE", "LIMITED", "MODERATE", "HIGH", "ABUNDANT"]
    activity: Literal["WEAK", "GROWING", "STRONG", "RESTRICTED"]
    purchasePrice: int
    sellPrice: int

market_trade_good = MarketTradeGood

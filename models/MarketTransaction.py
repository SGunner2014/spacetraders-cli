from typing import Literal

class MarketTransaction:
    waypointSymbol: str
    shipSymbol: str
    tradeSymbol: str
    type_: Literal["PURCHASE", "SELL"]
    units: int
    pricePerUnit: int
    totalPrice: int
    timestamp: str

market_transaction = MarketTransaction
from . import construction_material_trade_symbol

class ShipCargoItem:
    symbol: construction_material_trade_symbol
    name: str
    description: str
    units: int

ship_cargo_item = ShipCargoItem
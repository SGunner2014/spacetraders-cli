from . import system_type

class ScannedSystem:
    symbol: str
    sectorSymbol: str
    type_: system_type
    x: int
    y: int
    distance: int

scanned_system = ScannedSystem
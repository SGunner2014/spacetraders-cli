from . import ship_registration, ship_nav

class ScannedShipFrame:
    symbol: str

class ScannedShipReactor:
    symbol: str

class ScannedShipEngine:
    symbol: str

class ScannedShipMounts:
    symbol: str

class ScannedShip:
    symbol: str
    registration: ship_registration
    nav: ship_nav
    frame: ScannedShipFrame
    reactor: ScannedShipReactor
    engine: ScannedShipEngine
    mounts: ScannedShipMounts

scanned_ship = ScannedShip
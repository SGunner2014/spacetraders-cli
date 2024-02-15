from . import waypoint_type

class ShipNavDestination:
    symbol: str
    type: waypoint_type
    systemSymbol: str
    x: int
    y: int

class ShipNavRoute:
    destination: ShipNavDestination
    origin: ShipNavDestination
    departureTime: str
    arrival: str

ship_nav_route = ShipNavRoute
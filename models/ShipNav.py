from . import ship_nav_route, ship_nav_status, ship_nav_flight_mode

class ShipNav:
    systemSymbol: str
    waypointSymbol: str
    route: ship_nav_route
    status: ship_nav_status
    flightMode: ship_nav_flight_mode

ship_nav = ShipNav
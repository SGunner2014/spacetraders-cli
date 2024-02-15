from typing import Literal
from enum import Enum

class ShipNavFlightMode(Enum):
    DRIFT = "DRIFT"
    STEALTH = "STEALTH"
    CRUISE = "CRUISE"
    BURN = "BURN"

ship_nav_flight_mode = Literal[ShipNavFlightMode]
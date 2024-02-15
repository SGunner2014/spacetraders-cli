from typing import Literal
from enum import Enum

class ShipNavStatus(Enum):
    IN_TRANSIT = "IN_TRANSIT"
    IN_ORBIT = "IN_ORBIT"
    DOCKED = "DOCKED"

ship_nav_status = Literal[ShipNavStatus]
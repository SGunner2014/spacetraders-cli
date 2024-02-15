from enum import Enum
from typing import Literal

class ShipRole(Enum):
    FABRICATOR = "FABRICATOR"
    HARVESTER = "HARVESTER"
    HAULER = "HAULER"
    INTERCEPTOR = "INTERCEPTOR"
    EXCAVATOR = "EXCAVATOR"
    TRANSPORT = "TRANSPORT"
    REPAIR = "REPAIR"
    SURVEYOR = "SURVEYOR"
    COMMAND = "COMMAND"
    CARRIER = "CARRIER"
    PATROL = "PATROL"
    SATELLITE = "SATELLITE"
    EXPLORER = "EXPLORER"
    REFINERY = "REFINERY"

ship_role = Literal[ShipRole]

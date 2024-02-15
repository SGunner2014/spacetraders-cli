from enum import Enum
from typing import Literal, List

from . import ship_requirements

class ShipFrameSymbol(Enum):
    FRAME_PROBE = "FRAME_PROBE"
    FRAME_DRONE = "FRAME_DRONE"
    FRAME_INTERCEPTOR = "FRAME_INTERCEPTOR"
    FRAME_RACER = "FRAME_RACER"
    FRAME_FIGHTER = "FRAME_FIGHTER"
    FRAME_FRIGATE = "FRAME_FRIGATE"
    FRAME_SHUTTLE = "FRAME_SHUTTLE"
    FRAME_EXPLORER = "FRAME_EXPLORER"
    FRAME_MINER = "FRAME_MINER"
    FRAME_LIGHT_FREIGHTER = "FRAME_LIGHT_FREIGHTER"
    FRAME_HEAVY_FREIGHTER = "FRAME_HEAVY_FREIGHTER"
    FRAME_TRANSPORT = "FRAME_TRANSPORT"
    FRAME_DESTROYER = "FRAME_DESTROYER"
    FRAME_CRUISER = "FRAME_CRUISER"
    FRAME_CARRIER = "FRAME_CARRIER"

class ShipFrame:
    symbol: Literal[ShipFrameSymbol]
    name: str
    description: str
    condition: int
    moduleSlots: int
    mountingPoints: int
    fuelCapacity: int
    requirements: List[ship_requirements]

ship_frame = ShipFrame

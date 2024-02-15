from typing import Literal

from . import ship_requirements

class ShipEngine:
    symbol: Literal["ENGINE_IMPULSE_DRIVE_I", "ENGINE_ION_DRIVE_I", "ENGINE_ION_DRIVE_II", "ENGINE_HYPER_DRIVE_I"]
    name: str
    description: str
    condition: int
    speed: int
    requirements: ship_requirements

ship_engine = ShipEngine

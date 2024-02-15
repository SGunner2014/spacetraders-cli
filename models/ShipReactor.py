from typing import Literal

from . import ship_requirements

class ShipReactor:
    symbol: Literal["REACTOR_SOLAR_I", "REACTOR_FUSION_I", "REACTOR_FISSION_I", "REACTOR_CHEMICAL_I", "REACTOR_ANTIMATTER_I"]
    name: str
    description: str
    condition: int
    powerOutput: int
    requirements: ship_requirements

ship_reactor = ShipReactor
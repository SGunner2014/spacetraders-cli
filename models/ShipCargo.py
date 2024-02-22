from typing import List

from . import ship_cargo_item

class ShipCargo:
    capacity: int
    units: int
    inventory: List[ship_cargo_item]

ship_cargo = ShipCargo
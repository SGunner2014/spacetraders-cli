from typing import Literal

class ShipCrew:
    current: int
    required: int
    capacity: int
    rotation: Literal["STRICT", "RELAXED"]
    morale: int
    wages: int

ship_crew = ShipCrew
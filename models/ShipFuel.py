from typing import Optional

class ShipFuelItem:
  amount: int
  timestamp: str

class ShipFuel:
  current: int
  capacity: int
  consumed: Optional[ShipFuelItem]

ship_fuel = ShipFuel
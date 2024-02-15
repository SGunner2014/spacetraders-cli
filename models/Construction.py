from enum import Enum
from typing import List, Literal

from . import construction_material

class Construction:
    symbol: str
    materials: List[construction_material]
    isComplete: bool

construction = Construction
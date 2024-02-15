from enum import Enum
from typing import Literal

class SystemType(Enum):
    NEUTRON_STAR = "NEUTRON_STAR"
    RED_STAR = "RED_STAR"
    ORANGE_STAR = "ORANGE_STAR"
    BLUE_STAR = "BLUE_STAR"
    YOUNG_STAR = "YOUNG_STAR"
    WHITE_DWARF = "WHITE_DWARF"
    BLACK_HOLE = "BLACK_HOLE"
    HYPERGIANT = "HYPERGIANT"
    NEBULA = "NEBULA"
    UNSTABLE = "UNSTABLE"

class ConnectedSystem:
    symbol: str
    sectorSymbol: str
    type: Literal[SystemType]
    factionSymbol: str
    x: int
    y: int
    distance: int

connected_system = ConnectedSystem
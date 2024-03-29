from typing import Literal
from enum import Enum

class FactionSymbol(Enum):
    COSMIC = "COSMIC"
    VOID = "VOID"
    GALACTIC = "GALACTIC"
    QUANTUM = "QUANTUM"
    DOMINION = "DOMINION"
    ASTRO = "ASTRO"
    CORSAIRS = "CORSAIRS"
    OBSIDIAN = "OBSIDIAN"
    AEGIS = "AEGIS"
    UNITED = "UNITED"
    SOLITARY = "SOLITARY"
    COBALT = "COBALT"
    OMEGA = "OMEGA"
    ECHO = "ECHO"
    LORDS = "LORDS"
    CULT = "CULT"
    ANCIENTS = "ANCIENTS"
    SHADOW = "SHADOW"
    ETHEREAL = "ETHEREAL"

faction_symbol = Literal[FactionSymbol]

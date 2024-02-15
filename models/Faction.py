from typing import List

from . import faction_symbol, faction_trait

class Faction:
    symbol: faction_symbol
    name: str
    description: str
    headquarters: str
    traits: List[faction_trait]
    isRecruiting: bool

faction = Faction
from typing import List

from . import waypoint_type, faction_symbol, waypoint_trait, chart

class ScannedWaypointOrbital:
    symbol: str

class ScannedWaypointFaction:
    symbol: faction_symbol

class ScannedWaypoint:
    synmbol: str
    type_: waypoint_type
    systemSymbol: str
    x: int
    y: int
    orbitals: List[ScannedWaypointOrbital]
    faction: ScannedWaypointFaction
    traits: List[waypoint_trait]
    chart: chart

scanned_waypoint = ScannedWaypoint
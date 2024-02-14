from enum import Enum

class ship_role(Enum):
    FABRICATOR = "FABRICATOR"
    HARVESTER = "HARVESTER"
    HAULER = "HAULER"
    INTERCEPTOR = "INTERCEPTOR"
    EXCAVATOR = "EXCAVATOR"
    TRANSPORT = "TRANSPORT"
    REPAIR = "REPAIR"
    SURVEYOR = "SURVEYOR"
    COMMAND = "COMMAND"
    CARRIER = "CARRIER"
    PATROL = "PATROL"
    SATELLITE = "SATELLITE"
    EXPLORER = "EXPLORER"
    REFINERY = "REFINERY"

class location_type(Enum):
    PLANET = "PLANET"
    GAS_GIANT = "GAS_GIANT"
    MOON = "MOON"
    ORBITAL_STATION = "ORBITAL_STATION"
    JUMP_GATE = "JUMP_GATE"
    ASTEROID_FIELD = "ASTEROID_FIELD"
    ASTEROID = "ASTEROID"
    ENGINEERED_ASTEROID = "ENGINEERED_ASTEROID"
    ASTEROID_BASE = "ASTEROID_BASE"
    NEBULA = "NEBULA"
    DEBRIS_FIELD = "DEBRIS_FIELD"
    GRAVITY_WELL = "GRAVITY_WELL"
    ARTIFICIAL_GRAVITY_WELL = "ARTIFICIAL_GRAVITY_WELL"
    FUEL_STATION = "FUEL_STATION"

class ship_registration:
    name: str
    factionSymbol: str
    role: ship_role

class nav_location:
    symbol: str
    type: location_type
    systemSymbol: str
    x: int
    y: int

class flight_mode(Enum):
    DRIFT = "DRIFT"
    STEALTH = "STEALTH"
    CRUISE = "CRUISE"
    BURN = "BURN"

class nav_route:
    destination: nav_location
    origin: nav_location
    departureTime: str
    arrival: str

class nav_status(Enum):
    IN_TRANSIT = "IN_TRANSIT"
    IN_ORBIT = "IN_ORBIT"
    DOCKED = "DOCKED"

class ship_nav:
    systemSymbol: str
    waypointSymbol: str
    route: nav_route
    status: nav_status
    flightMode: flight_mode

class crew_rotation(Enum):
    STRICT = "STRICT"
    RELAXED = "RELAXED"

class ship_crew:
    current: int
    required: int
    capacity: int
    rotation: crew_rotation
    morale: int
    wages: int

class ship_frame_symbol(Enum):
    FRAME_PROBE = "FRAME_PROBE"
    FRAME_DRONE = "FRAME_DRONE"
    FRAME_INTERCEPTOR = "FRAME_INTERCEPTOR"
    FRAME_RACER = "FRAME_RACER"
    FRAME_FIGHTER = "FRAME_FIGHTER"
    FRAME_FRIGATE = "FRAME_FRIGATE"
    FRAME_SHUTTLE = "FRAME_SHUTTLE"
    FRAME_EXPLORER = "FRAME_EXPLORER"
    FRAME_MINER = "FRAME_MINER"
    FRAME_LIGHT_FREIGHTER = "FRAME_LIGHT_FREIGHTER"
    FRAME_HEAVY_FREIGHTER = "FRAME_HEAVY_FREIGHTER"
    FRAME_TRANSPORT = "FRAME_TRANSPORT"
    FRAME_DESTROYER = "FRAME_DESTROYER"
    FRAME_CRUISER = "FRAME_CRUISER"
    FRAME_CARRIER = "FRAME_CARRIER"

class ship_frame:
    symbol: ship_frame_symbol

class ship:
    symbol: str
    registration: ship_registration
    nav: ship_nav
    crew: ship_crew
    frame: ship_frame
from typing import List

from . import (
    ship_registration,
    ship_nav,
    ship_crew,
    ship_frame,
    ship_reactor,
    ship_engine,
    cooldown,
    ship_module,
    ship_mount,
    ship_cargo,
    ship_fuel,
)


class Ship:
    symbol: str
    registration: ship_registration
    nav: ship_nav
    crew: ship_crew
    frame: ship_frame
    reactor: ship_reactor
    engine: ship_engine
    cooldown: cooldown
    modules: List[ship_module]
    mounts: List[ship_mount]
    cargo: ship_cargo
    fuel: ship_fuel


ship = Ship

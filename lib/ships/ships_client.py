from datetime import datetime
from typing import List

from lib.generic_client import __GenericClient
from models.ships.ship import ship

class ShipsClient(__GenericClient):
    ships_list: List[ship] = []
    last_fetched = None

    def get_ships(self) -> List[ship]:
        ships = self.make_request("/my/ships", "GET")

        self.ships_list = ships.data
        self.last_fetched = datetime.now()

        return ships.data

    def get_ship(self, symbol: str) -> ship:
        ship = self.make_request(f"/my/ships/{symbol}", "GET")

        return ship.data

    def purchase_ship(self, ship_type: ship_type, waypoint_symbol: str):
        pass

from datetime import datetime
from typing import List

from clients.generic_client import __GenericClient
from models import ship
from exceptions.ShipNotFoundException import ShipNotFoundException

class ShipsClient(__GenericClient):
    selected_ship: str = None
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

    # def purchase_ship(self, ship_type: ship_type, waypoint_symbol: str):
    #     pass

    def select_ship(self, ship_symbol: str):
        if self.ships_list and ship_symbol in self.ships_list:
            self.selected_ship = ship_symbol
        else:
            raise ShipNotFoundException()

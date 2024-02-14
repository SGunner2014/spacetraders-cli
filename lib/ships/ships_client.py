from datetime import datetime
from typing import List

from lib.generic_client import __GenericClient
from models.ships.ship import ship

class ShipsClient(__GenericClient):
    ships_list: List[ship] = []
    last_fetched = None

    def get_ships(self) -> List[ship]:
        ships = self.make_request("/my/ships", "GET", expected=List[ship])

        self.ships_list = ships.data
        self.last_fetched = datetime.now()

        return ships.data
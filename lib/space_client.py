from lib.ships.ships_client import ShipsClient

class SpaceClient:
    def __init__(self, token):
        self.token = token
        self.ships = ShipsClient(token)
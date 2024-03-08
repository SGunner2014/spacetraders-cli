from clients.ships.ships_client import ShipsClient
from clients.contracts.contracts_client import ContractsClient

class SpaceClient:
    def __init__(self, token):
        self.token = token
        self.ships = ShipsClient(token)
        self.contracts = ContractsClient(token)
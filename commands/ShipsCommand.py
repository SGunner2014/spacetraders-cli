from typing import List
from prettytable import PrettyTable

from .BaseCommand import BaseCommand

class ShipsCommand(BaseCommand):
    name: str = "ships"

    def on_invoke(self, parts: List[str]) -> None:
        if parts[1] == "list":
            self.list_ships(parts)

    def list_ships(self, parts: List[str]) -> None:
        ships = self.space_client.ships.get_ships()
        table = PrettyTable(["Name", "Role", "Faction", "Status"])
        data = []
        for ship in ships:
            table.add_row([
                ship.registration.name,
                ship.registration.role,
                ship.registration.factionSymbol,
                ship.nav.status,
            ])
        print(table)
        

ships_command = ShipsCommand
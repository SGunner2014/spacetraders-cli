from typing import List
from prettytable import PrettyTable

from .BaseCommand import BaseCommand
from exceptions.ShipNotFoundException import ShipNotFoundException

class ShipsCommand(BaseCommand):
    name: str = "ships"

    def get_command_handlers(self) -> dict:
        return {
            "list": self.list_ships,
            "select": self.select_ship,
        }

    def list_ships(self, parts: List[str]) -> None:
        ships = self.space_client.ships.get_ships()
        table = PrettyTable(["Name", "Role", "Faction", "Status", "Selected"])
        for ship in ships:
            table.add_row([
                ship.registration.name,
                ship.registration.role,
                ship.registration.factionSymbol,
                ship.nav.status,
                "SELECTED" if ship.registration.name == self.space_client.ships.selected_ship else "",
            ])
        print(table)

    def select_ship(self, parts: List[str]) -> None:
        if len(parts) <= 2:
            return

        ship_symbol = parts[2]
        
        try:
            self.space_client.ships.select_ship(ship_symbol)
            print("Ship selected: " + str(ship_symbol))
        except ShipNotFoundException:
            print("Ship not found: " + str(ship_symbol))
        

ships_command = ShipsCommand
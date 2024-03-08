from typing import List
from prettytable import PrettyTable

from exceptions.ContractNotFoundException import ContractNotFoundException
from exceptions.ShipNotFoundException import ShipNotFoundException

from .BaseCommand import BaseCommand

class ContractsCommand(BaseCommand):
    name: str = "contracts"

    def get_command_handlers(self) -> dict:
        return {
            "list": self.get_contracts,
            "accept": self.accept_contract,
            "show": self.show_contract,
            "select": self.select_contract,
            "deliver": self.deliver_contract,
        }

    def get_contracts(self, parts: List[str]) -> None:
        contracts = self.space_client.contracts.get_contracts()
        table = PrettyTable([
            "ID",
            "Type",
            "Accepted",
            "Fulfilled",
            "Accept Deadline",
            "Selected",
        ])
        for contract in contracts:
            table.add_row([
                contract.id,
                contract.type,
                contract.accepted,
                contract.fulfilled,
                contract.deadlineToAccept,
                "SELECTED" if self.space_client.contracts.selected_contract == contract.id else ""
            ])
        print(table)

    def accept_contract(self, parts: List[str]) -> None:
        if len(parts) < 3:
            return

        contract_id = parts[2]
        self.space_client.contracts.accept_contract(contract_id)
        print(f"Contract Accepted: {contract_id}")

    def show_contract(self, parts: List[str]) -> None:
        if len(parts) < 3:
            return

        contract = self.space_client.contracts.show_contract(parts[2])

        table = PrettyTable([
            "ID",
            "Accepted",
            "Fulfilled",
            "Deadline",
            "Payment",
        ])
        table.add_row([
            contract.id,
            contract.accepted,
            contract.fulfilled,
            contract.terms.deadline,
            f"{contract.terms.payment.onAccepted} -> {contract.terms.payment.onFulfilled}",
        ])
        print(table)
        print("\nDelivery:")

        table = PrettyTable([
            "Destination",
            "Trade Symbol",
            "Fulfilled/Required",
        ])
        for deliver in contract.terms.deliver:
            table.add_row([
                deliver.destinationSymbol,
                deliver.tradeSymbol,
                f"{deliver.unitsFulfilled}/{deliver.unitsRequired}",
            ])

        print(table)

    def select_contract(self, parts: List[str]) -> None:
        if len(parts) <= 2:
            return

        contract_symbol = parts[2]

        try:
            self.space_client.contracts.select_contract(contract_symbol)
            print("Contract selected: " + str(contract_symbol))
        except ContractNotFoundException:
            print("Contract not found: " + str(contract_symbol))

    def deliver_contract(self, parts: List[str]) -> None:
        selected_ship = self.space_client.ships.selected_ship
        if not selected_ship:
            print("You must select a ship before running this command")
        selected_contract = self.space_client.contracts.selected_contract
        if not selected_contract:
            print("You must select a contract before running this command")

        if len(parts) <= 3:
            print("You must specify a trade symbol and the number of units to deliver")
            return

        tradeSymbol = parts[2]
        units = int(parts[3])

        self.space_client.contracts.deliver(selected_ship, selected_contract, tradeSymbol, units)

contracts_command = ContractsCommand

from datetime import datetime
from typing import List

from clients.generic_client import __GenericClient
from exceptions.ContractNotFoundException import ContractNotFoundException
from models import contract

class ContractsClient(__GenericClient):
    selected_contract: str = None
    contracts_list: List[contract] = []
    last_fetched = None

    def get_contracts(self) -> List[contract]:
        contracts = self.make_request("/my/contracts", "GET")

        self.contracts_list = contracts.data
        self.last_fetched = datetime.now()

        return contracts.data

    def accept_contract(self, contract_id: str) -> None:
        contract = self.make_request(f"/my/contracts/{contract_id}/accept", "POST")

    def show_contract(self, contract_id: str) -> contract:
        contract = self.make_request(f"/my/contracts/{contract_id}", "GET")

        return contract.data

    def select_contract(self, contract_symbol: str):
        if self.contracts_list:
            for contract in self.contracts_list:
                if contract.id == contract_symbol:
                    self.selected_contract = contract_symbol
                    return
            raise ContractNotFoundException()
        else:
            raise ContractNotFoundException()

    def deliver(self, ship, contractId, tradeSymbol, units):
        response = self.make_request(f"/my/contracts/{contractId}/deliver", "POST", data={
            "shipSymbol": ship,
            "tradeSymbol": tradeSymbol,
            "units": units,
        })

        return response.data

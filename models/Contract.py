from . import contract_terms

class Contract:
    id: str
    factionSymbol: str
    type: str
    terms: contract_terms
    accepted: bool
    fulfilled: bool
    expiration: str
    deadlineToAccept: str

contract = Contract
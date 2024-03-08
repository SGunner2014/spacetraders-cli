from typing import List

from . import contract_payment, contract_deliver_good

class ContractTerms:
    deadline: str
    payment: contract_payment
    deliver: List[contract_deliver_good]

contract_terms = ContractTerms
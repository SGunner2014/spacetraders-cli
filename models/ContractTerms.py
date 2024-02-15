from . import contract_payment, contract_deliver_good

class ContractTerms:
    deadline: str
    payment: contract_payment
    deliver: contract_deliver_good

contract_terms = ContractTerms
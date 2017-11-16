def split_bills(contribution, involvement, balance):
    per_person = sum(contribution.values()) / ( len(balance) - len( [ i for i in involvement if not i ] ) )
    required_payments = {person: per_person if involvement.get(person, True) else 0.0 for person in balance}
    new_balance = {person: required_payments.get(person, 0.0 ) + balance[person] - contribution.get(person, 0.0) for person in balance}
    return new_balance


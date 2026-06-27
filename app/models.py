transaction_history = []

def add_transaction(txn: dict):
    transaction_history.append(txn)

def get_history():
    return transaction_history

def clear_history():
    transaction_history.clear()
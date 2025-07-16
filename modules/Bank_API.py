# ---------- Module 3: Simulated + M-PESA Bank API ----------

def fetch_bank_transactions(user_id):
    """
    Simulates fetching bank transactions for a given user ID.
    In a real-world application, this function would connect to a bank's API
    or a service like M-PESA to retrieve actual transaction data.

    Args:
        user_id (str): The ID of the user whose transactions are to be fetched.

    Returns:
        list: A list of dictionaries, where each dictionary represents a transaction.
    """
    # This is a mock implementation that returns a static list of transactions.
    # In a real application, you would make an API call to a financial institution.
    transactions = [
        {"date": "2025-07-01", "amount": -1200, "desc": "Rent"},
        {"date": "2025-07-02", "amount": -150, "desc": "Groceries"},
        {"date": "2025-07-03", "amount": -50, "desc": "Transport"},
        {"date": "2025-07-05", "amount": 5000, "desc": "Salary"},
        {"date": "2025-07-06", "amount": -500, "desc": "Investments"},
    ]
    for t in transactions:
        t['category'] = categorize_transaction(t['desc'])
    return transactions

def categorize_transaction(description):
    """
    Categorizes a transaction based on its description.

    Args:
        description (str): The description of the transaction.

    Returns:
        str: The category of the transaction.
    """
    description = description.lower()
    if 'rent' in description:
        return 'Rent'
    elif 'groceries' in description or 'food' in description:
        return 'Groceries'
    elif 'transport' in description or 'uber' in description or 'lyft' in description:
        return 'Transport'
    elif 'salary' in description or 'income' in description:
        return 'Income'
    elif 'investments' in description or 'stocks' in description:
        return 'Investments'
    else:
        return 'Other'

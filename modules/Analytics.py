# ---------- Module 5: Analytics ----------

import pandas as pd

def calculate_spending_by_category(transactions):
    """
    Calculates total spending for each category from a list of transactions.

    Args:
        transactions (list): A list of dictionaries, where each dictionary represents a transaction.

    Returns:
        pandas.Series: A pandas Series where the index is the category and the values are the total spending.
    """
    df = pd.DataFrame(transactions)
    # Filter for expenses (amount < 0) and take the absolute value
    expenses = df[df['amount'] < 0].copy()
    expenses['amount'] = expenses['amount'].abs()
    # Group by category and sum the amounts
    spending_by_category = expenses.groupby('category')['amount'].sum()
    return spending_by_category

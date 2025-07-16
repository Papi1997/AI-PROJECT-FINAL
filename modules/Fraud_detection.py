# ---------- Module 4: Anomaly Detection for Fraud ----------

import numpy as np
from sklearn.ensemble import IsolationForest

def detect_fraud(transactions):
    """
    Detects potential fraudulent transactions from a list of transactions using an Isolation Forest model.

    Args:
        transactions (list): A list of dictionaries, where each dictionary represents a transaction.

    Returns:
        list: A list of transactions that have been flagged as potentially fraudulent.
    """
    # Extract the transaction amounts and reshape the data for the model
    amounts = np.array([t['amount'] for t in transactions]).reshape(-1, 1)

    # Initialize the Isolation Forest model. The `contamination` parameter is the expected proportion of outliers in the data.
    model = IsolationForest(contamination=0.1)
    # Fit the model to the transaction amounts
    model.fit(amounts)

    # Predict which transactions are outliers (potential fraud)
    preds = model.predict(amounts)

    # Return the transactions that were flagged as outliers (-1)
    flagged = [transactions[i] for i, p in enumerate(preds) if p == -1]
    return flagged

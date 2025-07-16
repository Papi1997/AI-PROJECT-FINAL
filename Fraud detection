# ---------- Module 4: Anomaly Detection for Fraud ----------
import numpy as np
from sklearn.ensemble import IsolationForest

def detect_fraud(transactions):
    amounts = np.array([t['amount'] for t in transactions]).reshape(-1, 1)
    model = IsolationForest(contamination=0.1)
    model.fit(amounts)
    preds = model.predict(amounts)
    flagged = [transactions[i] for i, p in enumerate(preds) if p == -1]
    return flagged

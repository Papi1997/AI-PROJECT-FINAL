# ---------- Module 1: Expense Prediction ----------
import pandas as pd
from prophet import Prophet

def forecast_expenses(expense_data):
    df = pd.DataFrame(expense_data)
    df.columns = ['ds', 'y']  # Prophet requires columns named ds (date) and y (value)
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    return forecast[['ds', 'yhat']]

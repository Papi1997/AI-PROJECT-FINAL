# ---------- Module 1: Expense Prediction ----------

import pandas as pd
from prophet import Prophet

def forecast_expenses(expense_data):
    """
    Forecasts future expenses based on historical data using Facebook's Prophet library.

    Args:
        expense_data (list): A list of tuples, where each tuple contains a date and an expense amount.

    Returns:
        pandas.DataFrame: A DataFrame containing the forecasted expenses, with columns 'ds' (date) and 'yhat' (forecasted value).
    """
    # Create a pandas DataFrame from the input data
    df = pd.DataFrame(expense_data)
    # Prophet requires the columns to be named 'ds' (datestamp) and 'y' (value)
    df.columns = ['ds', 'y']

    # Initialize the Prophet model
    model = Prophet()
    # Fit the model to the expense data
    model.fit(df)

    # Create a DataFrame for future dates to be predicted
    future = model.make_future_dataframe(periods=30)
    # Predict the future expenses
    forecast = model.predict(future)

    # Return the forecasted data, including the date and the predicted value
    return forecast[['ds', 'yhat']]

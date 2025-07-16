# ---------- Main Application Entry Point ----------

# Import custom modules for different functionalities
from modules.forecasting import forecast_expenses  # For predicting future expenses
from modules.gpt_advice import gpt_financial_advice  # For generating financial advice using GPT
from modules.bank_api import fetch_bank_transactions  # For fetching transaction data from bank API
from modules.fraud_detection import detect_fraud  # For detecting suspicious transactions

# Import third-party libraries
import streamlit as st  # Streamlit is used for building the web UI
import pandas as pd  # Pandas is used for data manipulation and analysis


def run_dashboard():
    # Title of the Streamlit web application
    st.title(" AI-Powered Personal Finance Manager")

    # Input field for user to enter their unique user ID
    user_id = st.text_input("Enter your user ID", "user_1")

    # Text area where user describes their financial context
    context = st.text_area("Describe your financial situation:",
        "My monthly income is 5000. I spend heavily on rent and groceries. I want to save more.")

    # When the Analyze button is clicked
    if st.button("Analyze"):
        # Fetch the user's bank transactions using the user ID
        txns = fetch_bank_transactions(user_id)

        # Convert the list of transactions to a pandas DataFrame for easier processing
        df_txns = pd.DataFrame(txns)

        # Filter and prepare expenses (negative amounts) for forecasting
        forecast = forecast_expenses(
            [(t['date'], abs(t['amount'])) for t in txns if t['amount'] < 0]
        )

        # Generate financial advice using GPT model and user-provided context
        advice = gpt_financial_advice(context)

        # Detect fraudulent transactions from the transaction list
        flagged = detect_fraud(txns)

        # Display the forecasted expenses using a line chart
        st.subheader(" Forecasted Expenses")
        st.line_chart(forecast.set_index('ds')['yhat'])

        # Display GPT-generated financial advice
        st.subheader(" GPT Financial Advice")
        st.info(advice)

        # Display flagged suspicious transactions, if any
        st.subheader(" Potential Fraudulent Transactions")
        if flagged:
            st.dataframe(pd.DataFrame(flagged))  # Show the flagged transactions in a table
        else:
            st.success("No suspicious transactions detected.")  # Show a success message if none detected


# Entry point for the script
if __name__ == '__main__':
    run_dashboard()

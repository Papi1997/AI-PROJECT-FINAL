# ---------- Main Application Entry Point ----------

# Import custom modules for different functionalities
from modules.Forecasting import forecast_expenses
from modules.Payment_advice import gpt_financial_advice
from modules.Bank_API import fetch_bank_transactions
from modules.Fraud_detection import detect_fraud

# Import third-party libraries
import streamlit as st
import pandas as pd


def run_dashboard():
    """
    This function runs the main Streamlit dashboard for the Personal Finance Manager.
    """
    # Set the title of the Streamlit web application
    st.title("AI-Powered Personal Finance Manager")

    # Create an input field for the user to enter their unique user ID
    user_id = st.text_input("Enter your user ID", "user_1")

    # Create a text area for the user to describe their financial context
    context = st.text_area(
        "Describe your financial situation:",
        "My monthly income is 5000. I spend heavily on rent and groceries. I want to save more."
    )

    # Create a button that triggers the analysis
    if st.button("Analyze"):
        # Fetch the user's bank transactions using the provided user ID
        txns = fetch_bank_transactions(user_id)

        # Convert the list of transactions to a pandas DataFrame for easier processing
        df_txns = pd.DataFrame(txns)

        # Filter and prepare expenses (negative amounts) for forecasting
        expenses = [(t['date'], abs(t['amount'])) for t in txns if t['amount'] < 0]
        forecast = forecast_expenses(expenses)

        # Generate financial advice using the GPT model and user-provided context
        advice = gpt_financial_advice(context)

        # Detect fraudulent transactions from the transaction list
        flagged = detect_fraud(txns)

        # Display the forecasted expenses using a line chart
        st.subheader("Forecasted Expenses")
        st.line_chart(forecast.set_index('ds')['yhat'])

        # Display the GPT-generated financial advice
        st.subheader("GPT Financial Advice")
        st.info(advice)

        # Display the categorized transactions
        st.subheader("Categorized Transactions")
        st.dataframe(df_txns)

        # Display the flagged suspicious transactions, if any
        st.subheader("Potential Fraudulent Transactions")
        if flagged:
            st.dataframe(pd.DataFrame(flagged))  # Show the flagged transactions in a table
        else:
            st.success("No suspicious transactions detected.")  # Show a success message if none are detected


# Entry point for the script
if __name__ == '__main__':
    run_dashboard()

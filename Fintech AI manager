# ---------- Main Application Entry Point ----------
from modules.forecasting import forecast_expenses
from modules.gpt_advice import gpt_financial_advice
from modules.bank_api import fetch_bank_transactions
from modules.fraud_detection import detect_fraud
import streamlit as st
import pandas as pd


def run_dashboard():
    st.title(" AI-Powered Personal Finance Manager")

    user_id = st.text_input("Enter your user ID", "user_1")
    context = st.text_area("Describe your financial situation:",
        "My monthly income is 5000. I spend heavily on rent and groceries. I want to save more.")

    if st.button("Analyze"):
        txns = fetch_bank_transactions(user_id)
        df_txns = pd.DataFrame(txns)

        forecast = forecast_expenses(
            [(t['date'], abs(t['amount'])) for t in txns if t['amount'] < 0]
        )
        advice = gpt_financial_advice(context)
        flagged = detect_fraud(txns)

        st.subheader(" Forecasted Expenses")
        st.line_chart(forecast.set_index('ds')['yhat'])

        st.subheader(" GPT Financial Advice")
        st.info(advice)

        st.subheader(" Potential Fraudulent Transactions")
        if flagged:
            st.dataframe(pd.DataFrame(flagged))
        else:
            st.success("No suspicious transactions detected.")


if __name__ == '__main__':
    run_dashboard()

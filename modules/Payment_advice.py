# modules/Payment_advice.py

import streamlit as st  #  Required to access secrets
from openai import OpenAI  #  OpenAI Python client

#  Initialize OpenAI with the API key stored securely in Streamlit secrets
client = OpenAI(api_key=st.secrets["openai"]["api_key"])

def gpt_financial_advice(user_context):
    """
    Generates financial advice using OpenAI's GPT-4 model.

    Parameters:
    - user_context (str): A description of the user's financial situation, goals, or concerns.

    Returns:
    - str: AI-generated advice on budgeting, saving, and investing.
    """
    prompt = f"""
    You are a smart financial assistant. A user has the following context:
    {user_context}
    Provide them with budgeting, saving, and investing advice.
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful financial advisor."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

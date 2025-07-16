# modules/Payment_advice.py

import os
from openai import OpenAI

# Load API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def gpt_financial_advice(user_context):
    """
    Generates financial advice using OpenAI's GPT-4 model based on the user's financial context.
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

# modules/Payment_advice.py

import os  # Used to access environment variables
from openai import OpenAI  # Import the OpenAI client library

# Load the OpenAI API key from an environment variable named "OPENAI_API_KEY"
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client with the API key
client = openai.OpenAI(api_key=st.secrets["openai"]["api_key"])

def gpt_financial_advice(user_context):
    """
    This function uses OpenAI's GPT-4 model to generate personalized financial advice.

    Parameters:
    - user_context (str): A description of the user's financial situation, goals, or concerns.

    Returns:
    - str: AI-generated advice on budgeting, saving, and investing based on the user's input.
    """

    # Create a prompt that includes the user's context and asks the AI to provide financial guidance
    prompt = f"""
    You are a smart financial assistant. A user has the following context:
    {user_context}
    Provide them with budgeting, saving, and investing advice.
    """

    # Make a request to the OpenAI API using the chat completion interface
    response = client.chat.completions.create(
        model="gpt-4",  # Use the GPT-4 model for generating responses
        messages=[
            {"role": "system", "content": "You are a helpful financial advisor."},  # Set the assistant's tone/role
            {"role": "user", "content": prompt}  # Pass the actual user prompt
        ]
    )

    # Extract and return the generated response from the API result
    return response.choices[0].message.content

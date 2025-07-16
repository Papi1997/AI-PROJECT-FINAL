# ---------- Module 2: GPT-based Financial Planner ----------
import openai

def gpt_financial_advice(user_context):
    openai.api_key = 'htpps:fdghjkl;koij35378$#%&*..'
    prompt = f"""
    You are a smart financial assistant. A user has the following context:
    {user_context}
    Provide them with budgeting, saving, and investing advice.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful financial advisor."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

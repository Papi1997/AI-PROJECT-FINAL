# AI-Powered FinTech Personal Finance Manager

This is an AI-powered personal finance dashboard built with Python and Streamlit.

flowchart TD

    A[User inputs ID and context] --> B[main.py]

    B --> C[fetch_bank_transactions()]
    C --> C1[bank_api.py returns mock transactions]

    B --> D[forecast_expenses()]
    D --> D1[forecasting.py uses Prophet for predictions]

    B --> E[gpt_financial_advice()]
    E --> E1[gpt_advice.py uses GPT-4 API]

    B --> F[detect_fraud()]
    F --> F1[fraud_detection.py uses IsolationForest]

    D1 --> G[Display forecast chart]
    E1 --> H[Display GPT advice]
    F1 --> I[Show suspicious transactions]

    G --> Z[Streamlit UI]
    H --> Z
    I --> Z

Module	Responsibility
main.py	Runs the app, coordinates all logic, renders UI
bank_api.py	Generates 30 days of mock transactions
forecasting.py	Predicts expenses for next 30 days using Prophet
gpt_advice.py	Sends user context to GPT-4 and returns advice
fraud_detection.py	Identifies suspicious transactions via ML model

## Features

- **Expense Forecasting**: Predict future expenses using Facebook Prophet.
- **GPT-4 Financial Advice**: Get personalized financial advice from OpenAI's GPT-4.
- **Bank and M-PESA API Integration**: Simulated integration for fetching bank and M-PESA transactions.
- **Fraud Detection**: Detect anomalous transactions using Isolation Forest.
- **Streamlit Dashboard**: A user-friendly and interactive web interface.

## Project Structure

```
AI-PROJECT-FINAL/
|
|-- fintech_ai_manager.py       # Streamlit app entry point
|-- requirements.txt            # Project dependencies
|-- README.md                   # Documentation
|-- modules/
|   |-- Forecasting.py          # Forecast future expenses
|   |-- Payment_advice.py       # GPT-4 financial suggestions
|   |-- Bank_API.py             # Simulated transactions / M-PESA
|   `-- Fraud_detection.py      # Fraud/anomaly detection
`-- payment_failures_large.csv  # Sample data for fraud detection
```

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Papi1997/AI-PROJECT-FINAL.git
   cd AI-PROJECT-FINAL
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Add Your OpenAI API Key**

   Open `modules/Payment_advice.py` and replace `'htpps:fdghjkl;koij35378$#%&*..'` with your actual OpenAI API key.

   ```python
   openai.api_key = 'YOUR_OPENAI_API_KEY'
   ```

4. **Run the Streamlit Dashboard**

   ```bash
   streamlit run fintech_ai_manager.py
   ```

## How to Use

1. **Enter Your User ID**: Provide a unique user ID to fetch your transaction data.
2. **Describe Your Financial Situation**: Enter your financial context in the text area. This information will be used by GPT-4 to provide you with personalized financial advice.
3. **Click "Analyze"**: The application will then:
   - Fetch your bank transactions.
   - Forecast your future expenses.
   - Generate personalized financial advice.
   - Detect any potential fraudulent transactions.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

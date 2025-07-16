#  AI-Powered FinTech Personal Finance Manager

This is an AI-powered personal finance dashboard built with Python and Streamlit.

###  Features:
- **Expense Forecasting** using Facebook Prophet
- ** GPT-4 Financial Advice** via OpenAI API
- ** Bank + M-PESA API Integration** (simulated)
- ** Fraud Detection** with anomaly detection
- ** Streamlit Dashboard** UI

---

##  Project Structure
```
AI-PROJECT-FINAL/
│
├── fintech_ai_manager.py       # Streamlit app entry point
├── requirements.txt            # Project dependencies
├── README.md                   # Documentation
└── modules/
    ├── forecasting.py          # Forecast future expenses
    ├── gpt_advice.py           # GPT-4 financial suggestions
    ├── bank_api.py             # Simulated transactions / M-PESA
    └── fraud_detection.py      # Fraud/anomaly detection
```

---

##  Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Papi1997/AI-PROJECT-FINAL.git
cd AI-PROJECT-FINAL
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Add Your OpenAI API Key
Open `modules/gpt_advice.py` and replace:
```python
openai.api_key = 'myapikey'
```

### 4. Run the Streamlit Dashboard
```bash
streamlit run fintech_ai_manager.py
```

---

##  Integrate M-PESA Daraja
You can connect to real M-PESA transactions by modifying `modules/bank_api.py` and adding API requests using your Daraja credentials.

---

##  License
MIT License — free to modify and use.

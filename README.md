# Fraud Detection API 👮‍♂️🔍

A FastAPI-based system to detect fraudulent transactions using a machine learning model trained on synthetic data.

## Features
- **Machine Learning Model**: Random Forest classifier for fraud prediction.
- **Key Features**:
  - Transaction amount
  - Geographic mismatch
  - Device risk score
  - Recipient account risk
  - Active hours anomaly
- **Probability Output**: Returns fraud probability (0-1) and binary flag.

## Setup

### Prerequisites
- Python 3.8+
- Pip package manager

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fraud-detection-api.git
   cd fraud-detection-api 

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows

3. Install dependencies:
   ```bash
   pip install fastapi uvicorn scikit-learn pandas joblib

## Usage

### Start the Server
```bash
uvicorn app.main:app --reload

![image](https://github.com/user-attachments/assets/fee5e78c-c724-45d5-aa6f-d7b5fb913122)# Fraud Detection API 👮‍♂️🔍

A FastAPI-based system to detect fraudulent transactions using rule-based checks. Ideal for proof-of-concept demos.

## Features
- Rule-based fraud detection (geographic mismatch, transaction velocity, etc.).
- Mock user profiles and blocklisted recipients.
- Simple integration with Swagger UI for testing.

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
   pip install fastapi uvicorn

## Usage

### Start the Server
```bash
uvicorn app.main:app --reload

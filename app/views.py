from fastapi import APIRouter
import pandas as pd
import joblib
from datetime import datetime
from app.schema import Transaction
from app.mockdb import USER_PROFILES, HIGH_RISK_RECIPIENTS

model=joblib.load("fraud_model.joblib")

fraud_dec_router=APIRouter()

@fraud_dec_router.post('/check-fraud')
async def check_fraud(transaction: Transaction):
    user_profile=USER_PROFILES.get(transaction.user_id, {})
    start, end=user_profile.get("active_hours", (0, 23))
    is_outside=0 if (start <= transaction.hour_of_day <= end) else 1

    #Prepare features
    features={
        "amount":[transaction.amount],
        "is_outside_active_hours":[is_outside],
        "hour_of_day":[transaction.hour_of_day],
        "user_country":[transaction.user_country],
        "device_id":[transaction.device_id],
        "recipient_account":[transaction.recipient_account]
    }
    
    #One-hot encode categorical features
    df=pd.DataFrame(features)
    df=pd.get_dummies(df, columns=["user_country", "device_id", "recipient_account"])

    #Align columns with training data
    train_colums=model.feature_names_in_
    for col in train_colums:
        if col not in df.columns:
            df[col]=0

    #Predict
    fraud_prob=model.predict_proba(df[train_colums])[0][1]

    return {
        'fraud_probability': round(fraud_prob, 2),
        'is_fraud': bool(fraud_prob > 0.5)        
    }

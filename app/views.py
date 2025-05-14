from fastapi import APIRouter
from app.schema import Transaction
from app.mockdb import USER_PROFILES, HIGH_RISK_RECIPIENTS, TRANSACTION_COUNTS

fraud_dec_router=APIRouter()

@fraud_dec_router.post('/check-fraud')
async def check_fraud(transaction: Transaction):
    user_id=transaction.user_id
    user_profile= USER_PROFILES.get(user_id, {})

    triggered_rules={
        'country_mismatch':user_profile.get('usual_country') != transaction.user_country,
        'unusual_amount':transaction.amount > 3 * user_profile.get('avg_transaction', 0),
        'new_account':user_profile.get('account_age_days', 0) < 7,
        'device_anomaly':transaction.device_id not in user_profile.get('known_devices', []),
        'risky_recipient':transaction.recipient_account in HIGH_RISK_RECIPIENTS

    } 

    TRANSACTION_COUNTS[user_id]+=1
    triggered_rules['transaction_velocity']=TRANSACTION_COUNTS[user_id] > 5

    return {
        'is_fraud': any(triggered_rules.values()),
        'triggered_rules': triggered_rules
    }

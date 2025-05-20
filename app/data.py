import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from app.mockdb import USER_PROFILES, HIGH_RISK_RECIPIENTS

def generate_transactions(n=1000):
    transactions=[]
    user_ids=list(USER_PROFILES.keys())

    for _ in range(n):
        user_id=np.random.choice(user_ids)
        user_profile=USER_PROFILES[user_id]
        is_fraud=np.random.choice([0, 1], p=[0.8, 0.2])

        amount=abs(round(np.random.normal(user_profile["avg_transaction"],
                                          user_profile["avg_transaction"]/3), 2))
        recipient=(np.random.choice(HIGH_RISK_RECIPIENTS) if is_fraud
                   else f"acct_legit_{np.random.randint(1000)}"
        )

        #Simulate transaction time
        timestamp=datetime.now()-timedelta(days=np.random.randint(0, 30))
        hour=timestamp.hour

        #Check if outside active hours
        start, end= user_profile["active_hours"]
        is_outside_active_hours= 0 if (start <= hour <= end) else 1

        #Generate transaction
        transactions.append({
            "user_id":user_id,
            "amount":abs(round(amount, 2)),
            "user_country":user_profile["usual_country"],
            "device_id":"hacked_device" if is_fraud
            else np.random.choice(user_profile["known_devices"]),
            "recipient_account":recipient,
            "hour_of_day":hour,
            "is_outside_active_hours": is_outside_active_hours,
            "is_fraud":is_fraud
        })
    return pd.DataFrame(transactions)

#Generate and save data
df=generate_transactions(5000)
df.to_csv("training_data.csv", index=False)
print("Training data shape:", df.shape)
    
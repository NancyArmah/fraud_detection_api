import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

df=pd.read_csv("training_data.csv")

#Select features
X=df[[
    "amount",
    "is_outside_active_hours",
    "hour_of_day",
    "user_country",
    "device_id",
    "recipient_account"
]]

y=df["is_fraud"]

#Encode categorical columns
X=pd.get_dummies(X, columns=["user_country", "device_id", "recipient_account"])

#Train/test split
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.2, random_state=42)

#Train model
model=RandomForestClassifier(n_estimators=100, class_weight="balanced")
model.fit(X_train, y_train)

y_pred=model.predict(X_test)

#Evaluate and save model
print(classification_report(y_test, y_pred))
joblib.dump(model, "fraud_model.joblib")
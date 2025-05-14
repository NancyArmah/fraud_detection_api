from fastapi import FastAPI
from app.views import fraud_dec_router

app=FastAPI(title="Fraud Police 👮‍♂️🔪🔫",
            description="API for Fraud Detection",
            version="0.1.0",
            debug=True)

app.include_router(
    fraud_dec_router, prefix="/v1", tags=["Predict Fraud"]
)

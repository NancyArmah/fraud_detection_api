from pydantic import BaseModel

class Transaction(BaseModel):
    user_id: str
    amount: float
    user_country: str
    device_id: str
    recipient_account: str

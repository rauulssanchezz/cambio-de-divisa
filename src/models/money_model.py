from pydantic import BaseModel

class MoneyModel(BaseModel):
    amount: float
    source_currency: str
    target_currency: str

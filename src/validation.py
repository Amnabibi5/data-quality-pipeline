from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from datetime import date
import pandas as pd

class CustomerRecord(BaseModel):
    customer_id: Optional[int]
    email: Optional[EmailStr]
    age: Optional[int]
    signup_date: Optional[date]

    @validator('age')
    def check_age(cls, v):
        if v is not None and (v < 0 or v > 120):
            raise ValueError('Age must be 0-120')
        return v

class ProductRecord(BaseModel):
    product_id: Optional[int]
    product_name: Optional[str]
    price: Optional[float]
    stock_date: Optional[date]

    @validator('price')
    def check_price(cls, v):
        if v is not None and v < 0:
            raise ValueError('Price cannot be negative')
        return v

def validate_dataframe(df: pd.DataFrame, model):
    valid_rows = []
    invalid_rows = []
    for idx, row in df.iterrows():
        try:
            # Convert row to dict, handle NaN
            data = {k: (None if pd.isna(v) else v) for k,v in row.to_dict().items()}
            model(**data)
            valid_rows.append(idx)
        except Exception as e:
            invalid_rows.append({"index": idx, "error": str(e), "data": row.to_dict()})
    return valid_rows, invalid_rows
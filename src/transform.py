import pandas as pd

def transform_data(df: pd.DataFrame):
    """Transformation: Standardize dates, fix types"""
    # Validate and standardize dates
    for col in ['signup_date','stock_date','order_date']:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce', dayfirst=True)
    
    # Lowercase emails already done
    return df
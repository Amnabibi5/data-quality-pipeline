import pandas as pd

def clean_data(df: pd.DataFrame):
    initial_rows = len(df)
    
    # 1. Remove duplicates
    dup_count = df.duplicated().sum()
    df = df.drop_duplicates()
    
    # 2. Handle missing & fix types
    # Convert age/price/amount to numeric, invalid -> NaN
    for col in ['age','price','amount','customer_id','product_id','order_id']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Fill numeric missing with median
    for col in df.columns:
        if df[col].dtype in ['float64','int64']:
            if df[col].isnull().sum() > 0:
                df[col] = df[col].fillna(df[col].median())
    
    # Clean text columns
    if 'email' in df.columns:
        df['email'] = df['email'].astype(str).str.lower().str.strip()
    
    final_rows = len(df)
    return df, {
        "initial_rows": initial_rows,
        "duplicates_removed": int(dup_count),
        "final_rows": final_rows
    }
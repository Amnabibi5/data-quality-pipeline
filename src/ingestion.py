import pandas as pd

def ingest_file(filepath: str) -> pd.DataFrame:
    """Ingest CSV, Excel, JSON - Polymorphic Ingestion"""
    if filepath.endswith('.csv'):
        df = pd.read_csv(filepath)
    elif filepath.endswith('.xlsx'):
        df = pd.read_excel(filepath)
    elif filepath.endswith('.json'):
        df = pd.read_json(filepath)
    else:
        raise ValueError("Unsupported format")
    return df

def validate_schema(df: pd.DataFrame, required_cols: list):
    """Schema Validation: Check columns exist"""
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    return True
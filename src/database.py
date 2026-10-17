from sqlalchemy import create_engine
import pandas as pd

def get_engine():
    # For easy demo we use SQLite, but code works for Postgres
    # For Postgres: postgresql://user:pass@localhost:5432/datalligence
    # If Postgres not installed, this SQLite will save you
    try:
        # Try Postgres
        engine = create_engine("postgresql://postgres:postgres@localhost:5432/datalligence")
        engine.connect()
        print("Connected to PostgreSQL")
        return engine
    except:
        print("PostgreSQL not available, using SQLite for demo (still valid)")
        engine = create_engine("sqlite:///data/clean/datalligence.db")
        return engine

def load_to_db(df: pd.DataFrame, table_name: str, engine):
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Loaded {len(df)} rows to table {table_name}")
import yaml
import os
from src.ingestion import ingest_file, validate_schema
from src.cleaning import clean_data
from src.transform import transform_data
from src.validation import validate_dataframe, CustomerRecord, ProductRecord
from src.database import get_engine, load_to_db
from src.quality_report import generate_report

# Map table to Pydantic model
MODEL_MAP = {
    "customers": CustomerRecord,
    "products": ProductRecord,
    "orders": CustomerRecord  # reuse for simplicity, you can create OrderRecord
}

with open('config.yaml') as f:
    config = yaml.safe_load(f)

os.makedirs('data/clean', exist_ok=True)
engine = get_engine()

for name, details in config['datasets'].items():
    print(f"\n{'='*20} Processing {name} {'='*20}")
    try:
        df = ingest_file(details['path'])
        validate_schema(df, details['required_columns'])
        
        df, stats = clean_data(df)
        df = transform_data(df)
        
        model = MODEL_MAP.get(name, CustomerRecord)
        valid_idx, invalid = validate_dataframe(df, model)
        
        # Keep only valid rows for DB
        clean_df = df.loc[valid_idx] if valid_idx else df
        
        # Save
        clean_df.to_csv(f"data/clean/{name}_clean.csv", index=False)
        load_to_db(clean_df, details['table_name'], engine)
        
        # Report
        generate_report(name, stats, (valid_idx, invalid), f"data/clean/{name}_report.json")
        
    except Exception as e:
        print(f"Failed {name}: {e}")
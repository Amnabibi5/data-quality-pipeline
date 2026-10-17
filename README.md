# Data Quality Pipeline - Senior Level

A production-ready data quality pipeline that ingests, validates, cleans, and transforms data from multiple sources.

## 🚀 Features
- **8-Module Architecture:** ingestion, cleaning, validation, transformation, config, logger, utils, pipeline
- **3 Data Sources:** CSV, JSON, Excel
- **Data Validation:** Quality scores, missing values, duplicates, email validation
- **Cleaning:** Removes duplicates, handles missing values, standardizes dates
- **Logging:** Full pipeline logs saved in `/logs`
- **Reports:** Clean data reports in JSON

## 📁 Project Structure
src/
├── config.py - All paths & settings
├── ingestion.py - Loads CSV, JSON, Excel
├── cleaning.py - Removes duplicates & nulls
├── validation.py - Quality checks
├── transformation.py - Standardizes & merges
├── logger.py - Logging system
├── utils.py - Helper functions
└── pipeline.py - Main orchestrator

##  How to Run
pip install -r requirements.txt
python main.py
## Output
Clean files: data/clean/
Quality reports: data/clean/*_report.json
Logs: logs/
Built by Amna Bibi | Data Engineer Internship Project at Datalligence

import json
from datetime import datetime

def generate_report(dataset_name, initial_stats, validation_stats, output_path):
    report = {
        "dataset": dataset_name,
        "timestamp": datetime.now().isoformat(),
        "initial_rows": initial_stats["initial_rows"],
        "duplicates_removed": initial_stats["duplicates_removed"],
        "final_rows": initial_stats["final_rows"],
        "valid_rows": len(validation_stats[0]),
        "invalid_rows": len(validation_stats[1]),
        "invalid_samples": validation_stats[1][:3]  # first 3 errors
    }
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2, default=str)
    print(f"Report saved: {output_path}")
    return report
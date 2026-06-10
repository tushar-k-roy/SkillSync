import json
import csv
from pathlib import Path


INPUT_FILE = Path("data/processed/jd_master.jsonl")
OUTPUT_FILE = Path("data/exports/jd_master.csv")

FIELDNAMES = [
    "entry_id",           # numeric-only ID
    "date_posted",        # NEW: date job was posted (from LinkedIn/company site)
    "date_added",         # date I logged/copied the JD
    "company",
    "role_title_raw",
    "role_title_standardized",
    "industry",
    "location",
    "work_mode",
    "seniority",
    "employment_type",
    "salary",
    "inferred_job_family",
    "inferred_specialization",
    "inferred_role_focus",
    "skills_tools",
    "skills_technical",
    "skills_business_terms",
    "skills_governance_terms",
    "skills_soft",
    "required_skills",
    "preferred_skills",
    "similarity_tags",
    "notes",
]


def normalize_value(value):
    """Convert list -> ' | ' joined string, None -> '', everything else -> str."""
    if isinstance(value, list):
        return " | ".join(str(item) for item in value)
    if value is None:
        return ""
    return str(value)


def coerce_numeric_entry_ids(records, start_index=1):
    """
    Ensure every record has a purely numeric entry_id.
    If entry_id is missing or non-numeric, assign sequential IDs starting from start_index.
    """
    next_id = start_index
    for record in records:
        raw_id = str(record.get("entry_id", "")).strip()
        if not raw_id.isdigit():
            record["entry_id"] = str(next_id)
            next_id += 1
        else:
            # Already numeric, keep as-is
            record["entry_id"] = raw_id
    return records


def main():
    # Read JSON (single object or list of objects)
    with INPUT_FILE.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # Normalize to a list of dicts
    if isinstance(data, dict):
        records = [data]
    elif isinstance(data, list):
        records = data
    else:
        raise ValueError("JSON root must be an object or a list of objects")

    # Ensure numeric-only entry_id values
    records = coerce_numeric_entry_ids(records, start_index=1)

    # Make sure date_posted exists in every record (if missing, set to NOT_MENTIONED)
    for record in records:
        if "date_posted" not in record or record["date_posted"] is None:
            record["date_posted"] = "NOT_MENTIONED"

    # Convert records to rows matching FIELDNAMES
    rows = []
    for record in records:
        row = {}
        for field in FIELDNAMES:
            row[field] = normalize_value(record.get(field, ""))
        rows.append(row)

    # Create output directory
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Write CSV
    with OUTPUT_FILE.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

    print(f"CSV created: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()

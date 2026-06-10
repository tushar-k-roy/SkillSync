# SkillSync

SkillSync is a personal job description tracking project. It stores job descriptions in a structured JSONL format and converts them into CSV for analysis, filtering, and later matching against skills, projects, and resume content.

## Project purpose

The goal of this repository is to build a clean and reusable dataset of job descriptions, starting with manually added entries and later expanding into a larger searchable collection.

This project is useful for:

- Tracking job roles across companies
- Standardizing job description data
- Extracting skills and keywords
- Exporting data into CSV for analysis
- Supporting future resume and portfolio alignment

## Repository structure

```text
skillsync/
├── data/
│   ├── processed/
│   │   └── jd_master.jsonl
│   └── exports/
│       └── jd_master.csv
├── scripts/
│   └── jsonl_to_csv.py
└── README.md
```

## Data format

The main source file is:

`data/processed/jd_master.jsonl`

This file uses JSON Lines format, which means:

- Each line is one complete JSON object
- Each object represents one job description entry
- New entries are added as new lines

Example entry:

```json
{"entry_id":"slice-product-analyst-001","date_added":"2026-06-10","company":"slice","role_title_raw":"Product Analyst","role_title_standardized":"Product Analyst","industry":"BFSI / fintech","location":"Bengaluru","work_mode":"NOT_MENTIONED","seniority":"1-3 years","employment_type":"Full time","salary":"NOT_MENTIONED","inferred_job_family":"Product Analytics","inferred_specialization":"Product / business analytics","inferred_role_focus":"Turning data into business decisions across Growth, Credit, Product, and Leadership through dashboards, diagnostic analysis, recommendations, and end-to-end analytics projects","skills_tools":["Python","Advanced SQL","PySpark","R","Excel","Cursor","Claude","CoPilots"],"skills_technical":["Dashboards","Visualizations","Diagnostic analysis","Prescriptive analysis","End-to-end analytics projects","Problem solving at scale"],"skills_business_terms":["Growth","Credit","Product","Leadership","Business problems","Strategic initiatives","Metrics at scale"],"skills_governance_terms":["NOT_MENTIONED"],"skills_soft":["Storytelling","Cross-functional collaboration","Curiosity","Adaptability"],"required_skills":["1-3 years experience","Python","Advanced SQL","Strong problem solving","Strong visualization skills","Storytelling"],"preferred_skills":["PySpark","R","Excel","AI-native mindset"],"similarity_tags":["product-analyst","sql-heavy","python-required","dashboard-heavy","fintech"],"notes":"Based on slice Product Analyst role emphasizing full-spectrum analytics, dashboards, diagnostic and prescriptive work, collaboration with Growth/Credit/Product/Leadership, and tools including Python and Advanced SQL."}
```

## CSV export

The export file is:

`data/exports/jd_master.csv`

This file is generated from the JSONL source using the Python conversion script in `scripts/jsonl_to_csv.py`.

## How to run the converter

From the repository root folder, run:

```bash
python scripts/jsonl_to_csv.py
```

If Python 3 is required on your system, use:

```bash
python3 scripts/jsonl_to_csv.py
```

## What the script does

The script:

- Reads `data/processed/jd_master.jsonl`
- Parses each JSON object line by line
- Converts list fields into pipe-separated text
- Writes the result to `data/exports/jd_master.csv`

## Current workflow

1. Add a new job description entry to `data/processed/jd_master.jsonl`
2. Save and commit the file
3. Run the conversion script
4. Check the generated CSV in `data/exports/`
5. Commit updated output if needed

## Notes

- Keep the JSONL schema consistent across entries
- Do not place multiple JSON objects on the same line
- Do not break one JSON object across multiple lines
- Use arrays for multi-value fields such as skills and tags
- Use `NOT_MENTIONED` where the job description does not provide a value

## Future plans

Possible future improvements include:

- Adding more job descriptions across companies
- Building keyword frequency analysis
- Creating role comparison views
- Matching jobs against resume skills
- Scoring fit by role type or specialization

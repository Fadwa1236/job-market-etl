import pandas as pd
from pathlib import Path
from src.skills import extract_skills

def transform_jobs(raw_jobs):
    # Remote OK often includes a metadata object as the first item
    jobs = raw_jobs[1:]

    df = pd.DataFrame(jobs)

    columns = [
        "id",
        "company",
        "position",
        "location",
        "tags",
        "salary_min",
        "salary_max",
        "date",
        "description",
    ]

    existing_columns = [col for col in columns if col in df.columns]
    df = df[existing_columns].copy()
    
    if "id" in df.columns:
        df = df.drop_duplicates(subset=["id"])
        
    for column in ["company", "position", "location"]:
        if column in df.columns:
            df[column] = df[column].fillna("").str.strip()
            
    for column in ["salary_min", "salary_max"]:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
        )
            
    if "date" in df.columns:
        df["date"] = pd.to_datetime(
            df["date"],
            errors="coerce"
    )
        
    if "salary_min" in df.columns and "salary_max" in df.columns:
        df["salary_avg"] = (
            df["salary_min"] + df["salary_max"]
        ) / 2
        
    if "description" in df.columns:
        df["extracted_skills"] = df["description"].apply(
            extract_skills
        )
    return df


def save_processed_data(df):
    processed_dir = Path("data/processed")
    processed_dir.mkdir(parents=True, exist_ok=True)

    filepath = processed_dir / "jobs_clean.csv"

    df.to_csv(
        filepath,
        index=False
    )

    return filepath
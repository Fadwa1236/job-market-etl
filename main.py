from src.extract import extract_jobs, save_raw_data
from src.transform import transform_jobs, save_processed_data
from src.load import load_data


def run_pipeline():
    raw_jobs = extract_jobs()

    save_raw_data(raw_jobs)

    clean_jobs = transform_jobs(raw_jobs)

    save_processed_data(clean_jobs)

    load_data(clean_jobs)

    print("Pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()
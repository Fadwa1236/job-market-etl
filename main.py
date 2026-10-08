from src.extract import extract_jobs, save_raw_data
from src.transform import transform_jobs, save_processed_data
from src.load import load_data
from src.validation import validate_jobs
from src.logger import logger

def run_pipeline():
    logger.info("Starting pipeline")
    
    raw_jobs = extract_jobs()

    logger.info("Extracted %s jobs", len(raw_jobs))

    save_raw_data(raw_jobs)

    clean_jobs = transform_jobs(raw_jobs)

    logger.info("Transformed %s jobs", len(clean_jobs))

    save_processed_data(clean_jobs)
    
    validate_jobs(clean_jobs)
    
    load_data(clean_jobs)
    
    logger.info("Pipeline completed")

if __name__ == "__main__":
    run_pipeline()
from src.extract import extract_jobs, save_raw_data
from src.transform import transform_jobs, save_processed_data


raw_jobs = extract_jobs()

save_raw_data(raw_jobs)

clean_jobs = transform_jobs(raw_jobs)

processed_file = save_processed_data(clean_jobs)

print(f"Rows: {len(clean_jobs)}")
print(f"Processed data saved to: {processed_file}")
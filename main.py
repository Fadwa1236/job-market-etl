from src.extract import extract_jobs, save_raw_data


jobs = extract_jobs()

filepath = save_raw_data(jobs)

print(f"Raw data saved to: {filepath}")
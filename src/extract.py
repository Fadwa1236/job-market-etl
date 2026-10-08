import json
from datetime import datetime
from pathlib import Path

import requests


API_URL = "https://remoteok.com/api"


def extract_jobs():
    headers = {
        "User-Agent": "job-market-etl-learning-project"
    }

    response = requests.get(
        API_URL,
        headers=headers,
        timeout=30
    )

    response.raise_for_status()

    return response.json()


def save_raw_data(data):
    raw_dir = Path("data/raw")
    raw_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filepath = raw_dir / f"jobs_{timestamp}.json"

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    return filepath
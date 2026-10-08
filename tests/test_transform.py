import pandas as pd
from src.transform import transform_jobs


def test_remove_duplicates():
    raw = [
        {},
        {
            "id": "1",
            "company": "Test",
            "position": "Engineer"
        },
        {
            "id": "1",
            "company": "Test",
            "position": "Engineer"
        }
    ]

    df = transform_jobs(raw)

    assert len(df) == 1
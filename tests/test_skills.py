from src.skills import extract_skills


def test_extract_skills():
    text = "We need Python, SQL and Airflow experience"

    skills = extract_skills(text)

    assert "python" in skills
    assert "sql" in skills
    assert "airflow" in skills
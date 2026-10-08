SKILLS = [
    "python",
    "sql",
    "pyspark",
    "spark",
    "databricks",
    "snowflake",
    "airflow",
    "dbt",
    "kafka",
    "aws",
    "azure",
    "docker",
    "postgresql",
]


def extract_skills(text):
    if not isinstance(text, str):
        return []

    text = text.lower()

    return [
        skill
        for skill in SKILLS
        if skill in text
    ]
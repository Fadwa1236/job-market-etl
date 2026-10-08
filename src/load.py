from sqlalchemy import text

from src.database import get_engine


def load_companies(df):
    engine = get_engine()

    companies = (
        df["company"]
        .dropna()
        .drop_duplicates()
        .tolist()
    )

    with engine.begin() as connection:
        for company in companies:
            connection.execute(
                text("""
                    INSERT INTO companies (company_name)
                    VALUES (:company_name)
                    ON CONFLICT (company_name) DO NOTHING
                """),
                {"company_name": company}
            )

def load_jobs(df):
    engine = get_engine()

    with engine.begin() as connection:
        for _, row in df.iterrows():

            company_id = connection.execute(
                text("""
                    SELECT company_id
                    FROM companies
                    WHERE company_name = :company_name
                """),
                {"company_name": row["company"]}
            ).scalar()

            connection.execute(
                text("""
                    INSERT INTO jobs (
                        job_id,
                        company_id,
                        position,
                        location,
                        salary_min,
                        salary_max,
                        salary_avg,
                        published_at,
                        description
                    )
                    VALUES (
                        :job_id,
                        :company_id,
                        :position,
                        :location,
                        :salary_min,
                        :salary_max,
                        :salary_avg,
                        :published_at,
                        :description
                    )
                    ON CONFLICT (job_id) DO UPDATE SET
                        position = EXCLUDED.position,
                        location = EXCLUDED.location,
                        salary_min = EXCLUDED.salary_min,
                        salary_max = EXCLUDED.salary_max,
                        salary_avg = EXCLUDED.salary_avg,
                        published_at = EXCLUDED.published_at,
                        description = EXCLUDED.description
                """),
                {
                    "job_id": str(row["id"]),
                    "company_id": company_id,
                    "position": row.get("position"),
                    "location": row.get("location"),
                    "salary_min": row.get("salary_min"),
                    "salary_max": row.get("salary_max"),
                    "salary_avg": row.get("salary_avg"),
                    "published_at": row.get("date"),
                    "description": row.get("description"),
                }
            )

def load_skills(df):
    engine = get_engine()

    with engine.begin() as connection:
        for _, row in df.iterrows():

            job_id = str(row["id"])

            for skill in row["extracted_skills"]:

                connection.execute(
                    text("""
                        INSERT INTO skills (skill_name)
                        VALUES (:skill_name)
                        ON CONFLICT (skill_name) DO NOTHING
                    """),
                    {"skill_name": skill}
                )

                skill_id = connection.execute(
                    text("""
                        SELECT skill_id
                        FROM skills
                        WHERE skill_name = :skill_name
                    """),
                    {"skill_name": skill}
                ).scalar()

                connection.execute(
                    text("""
                        INSERT INTO job_skills (job_id, skill_id)
                        VALUES (:job_id, :skill_id)
                        ON CONFLICT DO NOTHING
                    """),
                    {
                        "job_id": job_id,
                        "skill_id": skill_id
                    }
                )

def load_data(df):
    load_companies(df)
    load_jobs(df)
    load_skills(df)
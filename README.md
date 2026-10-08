# Remote Job Market ETL Pipeline

An end-to-end ETL project that extracts remote job postings from a public API, transforms and cleans the data with Python and Pandas, loads it into PostgreSQL, and analyzes the demand for data engineering skills using SQL.

## Project Goal

The goal of this project is to demonstrate the fundamentals of Data Engineering through a complete local ETL pipeline.

The pipeline answers questions such as:

- Which technical skills are most requested in remote jobs?
- How often are Python, SQL, Spark, Databricks, Airflow, Kafka, and dbt mentioned?
- Which companies are hiring the most?
- What are the most common job locations?
- Which technologies frequently appear together?

## Architecture

```text
Remote Jobs API
       |
       v
    Extract
    Python
       |
       v
   Raw JSON
       |
       v
   Transform
Pandas + Validation
       |
       v
Cleaned Job Data
       |
       v
 PostgreSQL
       |
       v
 SQL Analytics
```

The complete project also runs locally using Docker.

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQL
- SQLAlchemy
- Requests
- Pytest
- Docker
- Docker Compose
- Git & GitHub

## ETL Workflow

### Extract

Job data is retrieved from a remote jobs API using Python and the `requests` library.

The original API response is saved locally as JSON before any transformation is applied.

```text
API
 |
 v
data/raw/
```

Keeping raw data makes it possible to reproduce transformations and debug pipeline issues later.

### Transform

The raw job data is converted into a Pandas DataFrame and cleaned.

Transformations include:

- removing duplicate jobs
- handling missing values
- standardizing text
- converting dates
- converting salary fields
- validating records
- extracting technology skills from job descriptions

Example skills extracted:

```text
Python
SQL
Spark
PySpark
Databricks
Snowflake
Airflow
dbt
Kafka
AWS
Azure
Docker
PostgreSQL
```

### Load

The cleaned data is loaded into PostgreSQL.

The database uses a relational structure instead of storing everything in one table.

```text
companies
    |
    | 1:N
    v
   jobs
    |
    | N:M
    v
job_skills
    |
    v
 skills
```

## Database Schema

### companies

```text
company_id
company_name
```

### jobs

```text
job_id
company_id
position
location
salary_min
salary_max
salary_avg
published_at
description
```

### skills

```text
skill_id
skill_name
```

### job_skills

```text
job_id
skill_id
```

The `job_skills` table represents the many-to-many relationship between jobs and technical skills.

## Project Structure

```text
job-market-etl/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── rejected/
│
├── src/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── database.py
│   ├── validation.py
│   ├── skills.py
│   └── logger.py
│
├── sql/
│   ├── create_tables.sql
│   └── analysis.sql
│
├── tests/
│   ├── test_transform.py
│   └── test_skills.py
│
├── logs/
│
├── main.py
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
├── .env.example
├── requirements.txt
└── README.md
```

## Local Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/job-market-etl.git
```

Move into the project directory:

```bash
cd job-market-etl
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root.

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=job_market
DB_USER=postgres
DB_PASSWORD=your_password
```

Do not commit the `.env` file to GitHub.

An `.env.example` file is included to show the required configuration.

## Run Locally

Make sure PostgreSQL is running.

Then run:

```bash
python main.py
```

The pipeline will:

```text
Extract jobs
     |
     v
Save raw data
     |
     v
Transform and clean
     |
     v
Validate records
     |
     v
Extract skills
     |
     v
Load PostgreSQL
```

## Run with Docker

Build the containers:

```bash
docker compose build
```

Start the project:

```bash
docker compose up
```

The Docker setup contains:

```text
ETL Python Container
        |
        v
PostgreSQL Container
```

To run the ETL again:

```bash
docker compose run --rm etl
```

## Testing

Run the unit tests with:

```bash
pytest
```

Tests cover transformations and skill extraction.

Example:

```python
def test_extract_skills():
    text = "Experience with Python, SQL and Airflow required."

    skills = extract_skills(text)

    assert "python" in skills
    assert "sql" in skills
    assert "airflow" in skills
```

## Example SQL Analysis

### Most Requested Skills

```sql
SELECT
    s.skill_name,
    COUNT(*) AS job_count
FROM job_skills js
JOIN skills s
    ON js.skill_id = s.skill_id
GROUP BY s.skill_name
ORDER BY job_count DESC;
```

### Top Hiring Companies

```sql
SELECT
    c.company_name,
    COUNT(j.job_id) AS number_of_jobs
FROM companies c
JOIN jobs j
    ON c.company_id = j.company_id
GROUP BY c.company_name
ORDER BY number_of_jobs DESC;
```

## Data Quality

The pipeline checks for issues such as:

- missing job IDs
- missing companies
- duplicate jobs
- invalid salaries
- invalid dates
- salary maximum lower than salary minimum

Invalid records can be stored separately instead of being silently discarded.

## Idempotency

The pipeline is designed to avoid creating duplicate records when executed multiple times.

PostgreSQL conflict handling is used for existing jobs and skills.

Example:

```sql
ON CONFLICT (job_id)
DO UPDATE
```

This means the pipeline can be executed repeatedly without duplicating the entire dataset.

## Logging

Pipeline activity is written to the console and log files.

Example:

```text
INFO | Starting ETL pipeline
INFO | Extracted 250 jobs
INFO | Removed 12 duplicate records
INFO | Validated 238 jobs
INFO | Loaded jobs into PostgreSQL
INFO | Pipeline completed successfully
```

## What I Learned

Through this project I practiced:

- ETL pipeline design
- API data extraction
- JSON processing
- Pandas transformations
- data cleaning
- data validation
- relational database modeling
- PostgreSQL
- SQL joins and aggregations
- many-to-many relationships
- idempotent data loading
- logging
- unit testing
- environment variables
- Docker
- Git and GitHub

## Future Improvements

Possible future versions of the project include:

```text
Current
Python + PostgreSQL
        |
        v
Docker
        |
        v
dbt
        |
        v
Airflow
        |
        v
PySpark
        |
        v
Databricks
        |
        v
Kafka
```

Other improvements could include:

- scheduled daily ingestion
- historical job-market analysis
- advanced skill extraction using NLP
- salary trend analysis
- Power BI dashboard
- dbt transformations
- Airflow orchestration
- Spark processing
- cloud deployment

## Author

**Fadoua Mili**

Software Engineer interested in Data Engineering, Artificial Intelligence, Machine Learning, and scalable data systems.
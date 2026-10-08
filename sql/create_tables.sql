CREATE TABLE IF NOT EXISTS companies (
    company_id SERIAL PRIMARY KEY,
    company_name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS jobs (
    job_id VARCHAR(100) PRIMARY KEY,
    company_id INTEGER REFERENCES companies(company_id),
    position VARCHAR(255),
    location VARCHAR(255),
    salary_min NUMERIC,
    salary_max NUMERIC,
    salary_avg NUMERIC,
    published_at TIMESTAMP,
    description TEXT
);

CREATE TABLE IF NOT EXISTS skills (
    skill_id SERIAL PRIMARY KEY,
    skill_name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS job_skills (
    job_id VARCHAR(100) REFERENCES jobs(job_id),
    skill_id INTEGER REFERENCES skills(skill_id),
    PRIMARY KEY (job_id, skill_id)
);
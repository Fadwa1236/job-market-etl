def validate_jobs(df):
    assert df["id"].notna().all(), "Null job IDs found"
    assert df["company"].notna().all(), "Null companies found"

    if "salary_min" in df.columns:
        assert (df["salary_min"].dropna() >= 0).all()

    if "salary_max" in df.columns and "salary_min" in df.columns:
        valid = df.dropna(subset=["salary_min", "salary_max"])
        assert (valid["salary_max"] >= valid["salary_min"]).all()

    return True
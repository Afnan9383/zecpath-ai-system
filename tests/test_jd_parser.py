from parsers.jd_parser import normalize_jd_text, parse_job_description_text


SAMPLE_JD = """
12. AI-Based Logistics Analyst
Experience: 3-8 years
Salary (India): INR 8.0 LPA - INR 22.0 LPA
Job Description:
Uses artificial intelligence and machine learning models to optimize logistics operations.
Key Responsibilities:
- Develop predictive models
- Analyze large datasets
Skills Required:
- Python, machine learning, and data science
- Logistics and supply chain knowledge
"""


def test_normalize_jd_text_removes_extra_spacing():
    raw_text = "Skills Required:\n\n\n- Python     SQL"
    cleaned_text = normalize_jd_text(raw_text)

    assert "\n\n\n" not in cleaned_text
    assert "Python SQL" in cleaned_text


def test_parse_job_description_text_extracts_core_fields():
    parsed_jd = parse_job_description_text(SAMPLE_JD, "AI-Based Logistics Analyst.txt")

    assert parsed_jd["role_name"] == "AI-Based Logistics Analyst"
    assert parsed_jd["role_family"] == "Analyst"
    assert parsed_jd["experience_required"]["minimum_years"] == 3
    assert parsed_jd["experience_required"]["maximum_years"] == 8
    assert parsed_jd["salary_range"]["minimum_lpa"] == 8.0
    assert "Develop predictive models" in parsed_jd["responsibilities"]


def test_parse_job_description_text_normalizes_skill_synonyms():
    parsed_jd = parse_job_description_text(SAMPLE_JD)
    skill_keywords = parsed_jd["ai_profile"]["skill_keywords"]

    assert "python" in skill_keywords
    assert "machine learning" in skill_keywords
    assert "logistics" in skill_keywords

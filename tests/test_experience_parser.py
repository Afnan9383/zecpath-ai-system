from parsers.experience_parser import (
    extract_job_titles,
    extract_years,
    calculate_total_experience,
    calculate_role_relevance,
    parse_experience
)


def test_extract_job_titles():
    text = "Worked as Data Scientist and Python Developer"

    titles = extract_job_titles(text)

    assert "Data Scientist" in titles
    assert "Python Developer" in titles


def test_extract_years():
    text = "Worked from 2021 to 2024"

    years = extract_years(text)

    assert 2021 in years
    assert 2024 in years


def test_calculate_total_experience():
    years = [2021, 2024]

    total = calculate_total_experience(years)

    assert total == 3.0


def test_calculate_role_relevance():
    text = "Python machine learning AI data science"

    score = calculate_role_relevance(text, "Data Scientist")

    assert score > 50


def test_parse_experience():
    resume_text = """
WORK EXPERIENCE
Data Scientist at ABC Analytics 2021 - 2024
Worked on Python and machine learning projects.

EDUCATION
MCA
"""

    result = parse_experience(resume_text, candidate_id="C123", target_role="Data Scientist")

    assert result["candidate_id"] == "C123"
    assert result["experience_summary"]["total_experience_years"] == 3.0
    assert result["experience_summary"]["role_relevance_score"] > 0

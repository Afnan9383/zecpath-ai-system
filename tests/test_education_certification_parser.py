from parsers.education_certification_parser import (
    extract_education,
    extract_certifications,
    categorize_certification,
    calculate_education_relevance,
    parse_academic_profile
)


def test_extract_education():
    text = """
EDUCATION
2023-2025 Master of Computer Applications (MCA), KMCT College of Engineering
"""

    education = extract_education(text)

    assert len(education) > 0
    assert education[0]["degree"] == "Master of Computer Applications"


def test_extract_certifications():
    text = """
CERTIFICATIONS
Cyber Security & AI/ML - NIELIT
Power BI Data Analytics Certification
"""

    certifications = extract_certifications(text)

    assert len(certifications) == 2


def test_categorize_certification():
    category = categorize_certification("Cyber Security & AI/ML - NIELIT")

    assert category in ["AI/ML", "Cybersecurity"]


def test_calculate_education_relevance():
    education_records = [
        {
            "degree": "Master of Computer Applications",
            "field_of_study": "Computer Applications"
        }
    ]

    score = calculate_education_relevance(education_records, "Data Scientist")

    assert score > 0


def test_parse_academic_profile():
    text = """
EDUCATION
2023-2025 Master of Computer Applications (MCA), KMCT College of Engineering

CERTIFICATIONS
Cyber Security & AI/ML - NIELIT
"""

    profile = parse_academic_profile(text, candidate_id="C123", target_role="Data Scientist")

    assert profile["candidate_id"] == "C123"
    assert len(profile["education"]) > 0
    assert len(profile["certifications"]) > 0

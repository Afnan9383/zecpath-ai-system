from parsers.resume_section_classifier import (
    classify_resume_sections,
    detect_heading,
    detect_section_by_keywords
)


def test_detect_heading_skills():
    result = detect_heading("Technical Skills")
    assert result == "skills"


def test_detect_heading_education():
    result = detect_heading("Education")
    assert result == "education"


def test_keyword_based_section_detection():
    result = detect_section_by_keywords("Python SQL Machine Learning Power BI")
    assert result == "skills"


def test_classify_resume_sections():
    resume_text = """
Profile
Data scientist with interest in AI.

Technical Skills
Python
SQL
Machine Learning

Education
Master of Computer Applications

Projects
AI-powered resume screening system
"""

    sections = classify_resume_sections(resume_text)

    assert "Python" in sections["skills"]
    assert "Master of Computer Applications" in sections["education"]
    assert "AI-powered resume screening system" in sections["projects"]

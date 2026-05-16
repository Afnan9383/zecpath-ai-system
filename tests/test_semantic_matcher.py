from ats_engine.semantic_matcher import (
    calculate_semantic_similarity,
    classify_match_score,
    compare_resume_to_jd
)


def test_calculate_semantic_similarity():
    text_a = "Python machine learning data science"
    text_b = "Machine learning with Python for data analysis"

    score = calculate_semantic_similarity(text_a, text_b)

    assert score > 0


def test_classify_match_score():
    assert classify_match_score(80) == "Strong Match"
    assert classify_match_score(60) == "Moderate Match"
    assert classify_match_score(40) == "Weak Match"
    assert classify_match_score(10) == "Low Match"


def test_compare_resume_to_jd():
    resume_profile = {
        "skills": ["Python", "Machine Learning"],
        "experience_summary": "Built machine learning models using Python.",
        "projects": "AI prediction project"
    }

    jd_profile = {
        "required_skills": ["Python", "Machine Learning"],
        "job_description": "Need candidate with machine learning and Python experience.",
        "responsibilities": ["Build AI prediction models"]
    }

    result = compare_resume_to_jd(resume_profile, jd_profile)

    assert result["semantic_scores"]["overall_similarity"] > 0
    assert "match_level" in result

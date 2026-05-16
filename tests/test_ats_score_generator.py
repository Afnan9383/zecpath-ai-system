from ats_engine.ats_score_generator import (
    get_role_weights,
    normalize_score,
    classify_candidate,
    generate_ats_score
)


def test_get_role_weights():
    weights = get_role_weights("Data Scientist")

    assert weights["skill_match"] == 0.35
    assert weights["education_alignment"] == 0.20


def test_normalize_score():
    assert normalize_score(None) == 0.0
    assert normalize_score(-10) == 0.0
    assert normalize_score(120) == 100.0
    assert normalize_score(75) == 75.0


def test_classify_candidate():
    assert classify_candidate(85) == "Strong Fit"
    assert classify_candidate(65) == "Good Fit"
    assert classify_candidate(45) == "Average Fit"
    assert classify_candidate(20) == "Low Fit"


def test_generate_ats_score():
    component_scores = {
        "skill_match": 80,
        "experience_relevance": 70,
        "education_alignment": 90,
        "semantic_similarity": 75
    }

    result = generate_ats_score(
        candidate_id="C123",
        job_id="J456",
        role_name="Data Scientist",
        component_scores=component_scores
    )

    assert result["candidate_id"] == "C123"
    assert result["final_ats_score"] > 0
    assert "explanation" in result

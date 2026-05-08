from ats_engine.ats_scorer import calculate_ats_score

def test_calculate_ats_score():
    candidate_skills = ["Python", "FastAPI"]
    required_skills = ["Python", "FastAPI", "SQL"]

    result = calculate_ats_score(candidate_skills, required_skills)

    assert result["ats_score"] > 0
    assert "Python" in result["matched_skills"]

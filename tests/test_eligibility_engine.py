from ats_engine.eligibility_engine import decide_eligibility


def test_candidate_eligible():
    candidate = {
        "candidate_id": "C1",
        "ats_score": 85,
        "skills": ["Python", "Django"],
        "experience_years": 3,
        "location": "Remote",
        "availability": "Immediate"
    }

    rules = {
        "job_id": "J1",
        "min_ats_score": 75,
        "review_ats_score": 50,
        "mandatory_skills": ["Python"],
        "min_experience": 2,
        "max_experience": 5,
        "allowed_locations": ["Remote"],
        "required_availability": "Immediate"
    }

    result = decide_eligibility(candidate, rules)

    assert result["decision"] == "Eligible"


def test_candidate_review_when_missing_skill():
    candidate = {
        "candidate_id": "C2",
        "ats_score": 78,
        "skills": ["Python"],
        "experience_years": 3,
        "location": "Remote",
        "availability": "Immediate"
    }

    rules = {
        "job_id": "J1",
        "min_ats_score": 75,
        "review_ats_score": 50,
        "mandatory_skills": ["Python", "Django"],
        "min_experience": 2,
        "max_experience": 5,
        "allowed_locations": ["Remote"],
        "required_availability": "Immediate"
    }

    result = decide_eligibility(candidate, rules)

    assert result["decision"] == "Review"
    assert "Django" in result["missing_skills"]


def test_candidate_rejected_for_low_score():
    candidate = {
        "candidate_id": "C3",
        "ats_score": 40,
        "skills": ["Python"],
        "experience_years": 1,
        "location": "Remote",
        "availability": "Immediate"
    }

    rules = {
        "job_id": "J1",
        "min_ats_score": 75,
        "review_ats_score": 50,
        "mandatory_skills": ["Python"],
        "min_experience": 2,
        "max_experience": 5,
        "allowed_locations": ["Remote"],
        "required_availability": "Immediate"
    }

    result = decide_eligibility(candidate, rules)

    assert result["decision"] == "Rejected"
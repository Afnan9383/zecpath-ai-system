from scoring.decision_engine import final_decision

def test_final_decision_selected():
    result = final_decision(
        ats_score=80,
        screening_score=85,
        interview_score=90
    )

    assert result["decision"] == "Selected"
    assert result["final_score"] >= 75

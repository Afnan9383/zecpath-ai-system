from screening_ai.screening_report_generator import (
    extract_highlights,
    extract_missing_data,
    generate_screening_report
)


def test_extract_highlights():
    answers = [
        {
            "skills": ["python", "django"],
            "experience_years": 3,
            "availability": "Immediate",
            "salary_expectation": "6 lpa"
        }
    ]

    result = extract_highlights(answers)

    assert "python" in result["confirmed_skills"]
    assert result["availability"] == "Immediate"
    assert result["salary_expectation"] == "6 lpa"


def test_missing_data():
    answers = [
        {
            "skills": [],
            "experience_years": None,
            "availability": None,
            "salary_expectation": None
        }
    ]

    result = extract_missing_data(answers)

    assert "Salary expectation not provided" in result
    assert "Availability not provided" in result


def test_generate_screening_report():
    understood_answers = [
        {
            "question_id": "Q003",
            "intent": "experience_info",
            "normalized_answer": "i have three years experience in python",
            "skills": ["python"],
            "experience_years": 3,
            "availability": None,
            "salary_expectation": None,
            "is_off_topic": False,
            "is_vague": False
        }
    ]

    screening_score = {
        "final_screening_score": 80,
        "scored_answers": []
    }

    behavioral_signals = [
        {
            "communication_strength": "Strong",
            "flags": []
        }
    ]

    report = generate_screening_report(
        "C123",
        "J101",
        understood_answers,
        screening_score,
        behavioral_signals
    )

    assert report["recommendation"] == "Proceed to HR Interview"
    assert "Strong overall screening performance" in report["strengths"]
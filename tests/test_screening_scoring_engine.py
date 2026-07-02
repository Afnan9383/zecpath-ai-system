from screening_ai.screening_scoring_engine import (
    score_clarity,
    score_relevance,
    score_completeness,
    score_screening_answer,
    calculate_final_screening_score
)


def test_clarity_score():
    answer = {
        "normalized_answer": "i have three years experience in python",
        "flags": []
    }

    assert score_clarity(answer) == 100


def test_relevance_score():
    answer = {
        "intent": "experience_info",
        "is_off_topic": False
    }

    assert score_relevance(answer, "experience_info") == 100


def test_completeness_score():
    answer = {
        "skills": ["python"],
        "experience_years": 3,
        "availability": None,
        "salary_expectation": None,
        "is_vague": False
    }

    result = score_completeness(answer)

    assert result > 50


def test_question_score():
    answer = {
        "question_id": "Q003",
        "normalized_answer": "i have three years experience in python",
        "intent": "experience_info",
        "skills": ["python"],
        "experience_years": 3,
        "availability": None,
        "salary_expectation": None,
        "is_off_topic": False,
        "is_vague": False,
        "flags": []
    }

    result = score_screening_answer(answer, "experience_info")

    assert result["question_score"] > 70


def test_final_screening_score():
    scored_answers = [
        {"question_score": 80},
        {"question_score": 90},
        {"question_score": 70}
    ]

    result = calculate_final_screening_score(scored_answers)

    assert result["final_screening_score"] == 80
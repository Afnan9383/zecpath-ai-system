from screening_ai.answer_understanding_engine import (
    classify_intent,
    extract_skills,
    extract_experience_years,
    extract_availability,
    extract_salary_expectation,
    detect_off_topic,
    detect_vague_answer,
    understand_answer
)


def test_intent_classification():
    answer = "I have three years experience in Python"

    assert classify_intent(answer) == "experience_info"


def test_skill_extraction():
    answer = "I know Python and Django"

    skills = extract_skills(answer)

    assert "python" in skills
    assert "django" in skills


def test_experience_extraction():
    answer = "I have three years experience"

    assert extract_experience_years(answer) == 3


def test_availability_extraction():
    answer = "I can join immediately"

    assert extract_availability(answer) == "Immediate"


def test_salary_extraction():
    answer = "My expected salary is 6 LPA"

    assert extract_salary_expectation(answer) == "6 lpa"


def test_off_topic_detection():
    answer = "I like movies and music"

    assert detect_off_topic(answer) is True


def test_vague_answer_detection():
    answer = "Maybe"

    assert detect_vague_answer(answer) is True


def test_structured_answer():
    answer = "I have 2 years experience in Python"

    result = understand_answer("Q003", answer)

    assert result["intent"] == "experience_info"
    assert result["experience_years"] == 2
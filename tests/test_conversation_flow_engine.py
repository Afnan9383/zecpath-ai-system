from screening_ai.conversation_flow_engine import (
    initialize_conversation,
    get_current_question,
    decide_next_action,
    is_repeated_answer,
    get_ai_prompt
)


def test_initialize_conversation():
    questions = [
        {"question_id": "Q001", "question_text": "Introduce yourself"}
    ]

    conversation = initialize_conversation("C1", "J1", questions)

    assert conversation["candidate_id"] == "C1"
    assert conversation["conversation_status"] == "active"


def test_get_current_question():
    questions = [
        {"question_id": "Q001", "question_text": "Introduce yourself"}
    ]

    conversation = initialize_conversation("C1", "J1", questions)
    question = get_current_question(conversation)

    assert question["question_id"] == "Q001"


def test_silence_action():
    conversation = initialize_conversation("C1", "J1", [])

    answer_analysis = {
        "original_answer": "",
        "intent": "unknown",
        "flags": []
    }

    action = decide_next_action(conversation, answer_analysis)

    assert action == "retry_silence"


def test_repeated_answer_detection():
    previous_answers = [
        {"answer_text": "I have experience in Python"}
    ]

    result = is_repeated_answer(
        "I have experience in Python",
        previous_answers
    )

    assert result is True


def test_fallback_prompt():
    prompt = get_ai_prompt("retry_silence")

    assert "hear your response" in prompt
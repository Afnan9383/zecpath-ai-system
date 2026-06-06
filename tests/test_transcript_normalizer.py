from screening_ai.transcript_normalizer import (
    clean_transcript_text,
    detect_silence,
    detect_partial_answer
)


def test_remove_filler_words():
    text = "Um I have experience in Python"
    result = clean_transcript_text(text)

    assert "um" not in result["cleaned_text"]
    assert result["status"] == "processed"


def test_silence_detection():
    assert detect_silence("") is True


def test_partial_answer_detection():
    text = "I think maybe I can join next month"

    assert detect_partial_answer(text) is True
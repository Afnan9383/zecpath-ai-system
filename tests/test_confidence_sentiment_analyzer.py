from screening_ai.confidence_sentiment_analyzer import (
    detect_hesitation_patterns,
    detect_uncertainty,
    detect_contradictions,
    calculate_sentiment_score,
    calculate_confidence_score,
    analyze_behavioral_signals
)


def test_hesitation_detection():
    text = "Um I think maybe I can join"

    result = detect_hesitation_patterns(text)

    assert "um" in result
    assert "maybe" in result


def test_uncertainty_detection():
    text = "I am not sure about the salary"

    result = detect_uncertainty(text)

    assert "not sure" in result


def test_contradiction_detection():
    text = "I can join immediately but maybe after 30 days"

    result = detect_contradictions(text)

    assert len(result) > 0


def test_positive_sentiment_score():
    text = "I am confident and excited about this role"

    result = calculate_sentiment_score(text)

    assert result > 50


def test_confidence_score():
    text = "I am confident and ready for this opportunity"

    result = calculate_confidence_score(text)

    assert result >= 70


def test_behavioral_signal_output():
    text = "Um I think maybe I can join"

    result = analyze_behavioral_signals("Q009", text)

    assert result["question_id"] == "Q009"
    assert "hesitation_detected" in result["flags"]
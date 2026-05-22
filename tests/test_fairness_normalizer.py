from utils.fairness_normalizer import (
    normalize_resume_text,
    mask_sensitive_attributes,
    normalize_score,
    detect_bias_indicators,
    generate_fairness_report
)


def test_normalize_resume_text():
    text = "Python   Developer\nMachine Learning"

    result = normalize_resume_text(text)

    assert "python developer" in result


def test_mask_sensitive_attributes():
    text = "Email: test@example.com Phone: +91 9876543210"

    result = mask_sensitive_attributes(text)

    assert "[MASKED_EMAIL]" in result
    assert "[MASKED_PHONE]" in result


def test_normalize_score():
    assert normalize_score(None) == 0.0
    assert normalize_score(-5) == 0.0
    assert normalize_score(120) == 100.0
    assert normalize_score(80) == 80.0


def test_detect_bias_indicators():
    text = "Gender: Female Age: 24"

    result = detect_bias_indicators(text)

    assert "gender" in result
    assert "age" in result


def test_generate_fairness_report():
    resume_text = "Email: test@example.com Gender: Female Python developer"

    scores = {
        "skill_match": 80,
        "experience_relevance": 70
    }

    weights = {
        "skill_match": 0.6,
        "experience_relevance": 0.4
    }

    report = generate_fairness_report("C123", resume_text, scores, weights)

    assert report["candidate_id"] == "C123"
    assert report["balanced_score"] > 0
    assert len(report["fairness_notes"]) > 0

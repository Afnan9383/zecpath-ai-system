import re


POSITIVE_WORDS = [
    "confident",
    "interested",
    "passionate",
    "excited",
    "strong",
    "good",
    "comfortable",
    "ready",
    "motivated",
    "experienced"
]


NEGATIVE_WORDS = [
    "difficult",
    "weak",
    "confused",
    "problem",
    "bad",
    "uncomfortable",
    "unable",
    "poor",
    "struggle"
]


HESITATION_WORDS = [
    "um",
    "uh",
    "maybe",
    "i think",
    "not sure",
    "kind of",
    "probably",
    "actually"
]


UNCERTAINTY_WORDS = [
    "maybe",
    "not sure",
    "i don't know",
    "dont know",
    "i think",
    "probably",
    "not confident"
]


CONTRADICTION_PATTERNS = [
    ("immediate", "30 days"),
    ("immediate", "next month"),
    ("no experience", "experienced"),
    ("not confident", "confident")
]


def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s']", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def count_words(text):
    normalized = normalize_text(text)

    if not normalized:
        return 0

    return len(normalized.split())


def detect_hesitation_patterns(text):
    normalized = normalize_text(text)
    detected = []

    for word in HESITATION_WORDS:
        if word in normalized:
            detected.append(word)

    return detected


def detect_uncertainty(text):
    normalized = normalize_text(text)
    detected = []

    for word in UNCERTAINTY_WORDS:
        if word in normalized:
            detected.append(word)

    return detected


def detect_contradictions(text):
    normalized = normalize_text(text)
    contradictions = []

    for first, second in CONTRADICTION_PATTERNS:
        if first in normalized and second in normalized:
            contradictions.append(f"Contradiction detected between '{first}' and '{second}'")

    return contradictions


def calculate_sentiment_score(text):
    normalized = normalize_text(text)
    positive_count = 0
    negative_count = 0

    for word in POSITIVE_WORDS:
        if word in normalized:
            positive_count += 1

    for word in NEGATIVE_WORDS:
        if word in normalized:
            negative_count += 1

    raw_score = 50 + (positive_count * 10) - (negative_count * 10)

    if raw_score > 100:
        raw_score = 100

    if raw_score < 0:
        raw_score = 0

    return raw_score


def classify_sentiment(score):
    if score >= 65:
        return "Positive"
    if score <= 40:
        return "Negative"

    return "Neutral"


def calculate_confidence_score(text):
    word_count = count_words(text)
    hesitations = detect_hesitation_patterns(text)
    uncertainties = detect_uncertainty(text)
    contradictions = detect_contradictions(text)

    score = 80

    if word_count < 4:
        score -= 25

    if word_count >= 8:
        score += 10

    score -= len(hesitations) * 8
    score -= len(uncertainties) * 10
    score -= len(contradictions) * 15

    if score > 100:
        score = 100

    if score < 0:
        score = 0

    return round(score, 2)


def classify_communication_strength(confidence_score, sentiment_score):
    if confidence_score >= 75 and sentiment_score >= 50:
        return "Strong"
    if confidence_score >= 50:
        return "Moderate"

    return "Weak"


def analyze_behavioral_signals(question_id, answer_text):
    word_count = count_words(answer_text)
    hesitations = detect_hesitation_patterns(answer_text)
    uncertainties = detect_uncertainty(answer_text)
    contradictions = detect_contradictions(answer_text)
    sentiment_score = calculate_sentiment_score(answer_text)
    sentiment_label = classify_sentiment(sentiment_score)
    confidence_score = calculate_confidence_score(answer_text)
    communication_strength = classify_communication_strength(
        confidence_score,
        sentiment_score
    )

    flags = []

    if hesitations:
        flags.append("hesitation_detected")

    if uncertainties:
        flags.append("uncertainty_detected")

    if contradictions:
        flags.append("contradiction_detected")

    if word_count < 4:
        flags.append("short_response")

    return {
        "question_id": question_id,
        "answer_text": answer_text,
        "response_length_words": word_count,
        "hesitation_patterns": hesitations,
        "uncertainty_patterns": uncertainties,
        "contradictions": contradictions,
        "sentiment_score": sentiment_score,
        "sentiment_label": sentiment_label,
        "confidence_score": confidence_score,
        "communication_strength": communication_strength,
        "flags": flags
    }
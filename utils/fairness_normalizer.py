import json
import re
from pathlib import Path


SENSITIVE_PATTERNS = {
    "email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "phone": r"\+?\d[\d\s-]{8,}\d",
    "gender": r"\b(male|female|other)\b",
    "age": r"\b(age\s*[:\-]?\s*\d{1,2})\b",
    "marital_status": r"\b(single|married|divorced)\b"
}


BIAS_INDICATORS = [
    "gender",
    "age",
    "religion",
    "marital status",
    "photo",
    "native place",
    "caste",
    "family background"
]


def normalize_resume_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-z0-9\s\.\,\-\+/#]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def mask_sensitive_attributes(text: str) -> str:
    masked_text = text

    for label, pattern in SENSITIVE_PATTERNS.items():
        masked_text = re.sub(
            pattern,
            f"[MASKED_{label.upper()}]",
            masked_text,
            flags=re.IGNORECASE
        )

    return masked_text


def normalize_score(score: float | int | None) -> float:
    if score is None:
        return 0.0

    if score < 0:
        return 0.0

    if score > 100:
        return 100.0

    return round(float(score), 2)


def normalize_component_scores(scores: dict) -> dict:
    return {
        key: normalize_score(value)
        for key, value in scores.items()
    }


def calculate_balanced_score(scores: dict, weights: dict) -> float:
    normalized_scores = normalize_component_scores(scores)

    total_weight = sum(weights.values())

    if total_weight == 0:
        return 0.0

    weighted_score = 0

    for key, score in normalized_scores.items():
        weight = weights.get(key, 0)
        weighted_score += score * weight

    return round(weighted_score / total_weight, 2)


def detect_bias_indicators(text: str) -> list[str]:
    normalized_text = normalize_resume_text(text)
    detected = []

    for indicator in BIAS_INDICATORS:
        if indicator in normalized_text:
            detected.append(indicator)

    return detected


def generate_fairness_report(
    candidate_id: str,
    resume_text: str,
    scores: dict,
    weights: dict
) -> dict:
    masked_resume = mask_sensitive_attributes(resume_text)
    normalized_resume = normalize_resume_text(masked_resume)
    normalized_scores = normalize_component_scores(scores)
    balanced_score = calculate_balanced_score(normalized_scores, weights)
    bias_indicators = detect_bias_indicators(resume_text)

    return {
        "candidate_id": candidate_id,
        "normalized_resume_text": normalized_resume,
        "masked_resume_text": masked_resume,
        "normalized_scores": normalized_scores,
        "weights_used": weights,
        "balanced_score": balanced_score,
        "bias_indicators_detected": bias_indicators,
        "fairness_notes": [
            "Personal attributes are masked before evaluation.",
            "Scores are normalized between 0 and 100.",
            "Balanced scoring reduces over-dependence on one factor.",
            "Bias indicators are flagged for review."
        ]
    }


def save_fairness_report(
    candidate_id: str,
    resume_text: str,
    scores: dict,
    weights: dict,
    output_file: str = "data/fairness_outputs/fairness_report.json"
) -> str:
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)

    report = generate_fairness_report(
        candidate_id=candidate_id,
        resume_text=resume_text,
        scores=scores,
        weights=weights
    )

    Path(output_file).write_text(
        json.dumps(report, indent=2),
        encoding="utf-8"
    )

    return output_file

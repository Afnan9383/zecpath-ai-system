import json
from pathlib import Path


ROLE_WEIGHT_CONFIG = {
    "data_scientist": {
        "skill_match": 0.35,
        "experience_relevance": 0.25,
        "education_alignment": 0.20,
        "semantic_similarity": 0.20
    },
    "software_developer": {
        "skill_match": 0.40,
        "experience_relevance": 0.30,
        "education_alignment": 0.10,
        "semantic_similarity": 0.20
    },
    "logistics_analyst": {
        "skill_match": 0.30,
        "experience_relevance": 0.35,
        "education_alignment": 0.10,
        "semantic_similarity": 0.25
    },
    "default": {
        "skill_match": 0.30,
        "experience_relevance": 0.30,
        "education_alignment": 0.20,
        "semantic_similarity": 0.20
    }
}


def get_role_weights(role_name: str) -> dict:
    normalized_role = role_name.lower().replace(" ", "_")

    return ROLE_WEIGHT_CONFIG.get(normalized_role, ROLE_WEIGHT_CONFIG["default"])


def normalize_score(score: float | int | None) -> float:
    if score is None:
        return 0.0

    if score < 0:
        return 0.0

    if score > 100:
        return 100.0

    return float(score)


def calculate_weighted_score(score: float, weight: float) -> float:
    return round(score * weight, 2)


def classify_candidate(score: float) -> str:
    if score >= 80:
        return "Strong Fit"
    if score >= 60:
        return "Good Fit"
    if score >= 40:
        return "Average Fit"

    return "Low Fit"


def generate_explanation(component_scores: dict, weights: dict) -> list[str]:
    explanations = []

    for component, score in component_scores.items():
        weight = weights.get(component, 0)
        contribution = calculate_weighted_score(score, weight)

        explanations.append(
            f"{component.replace('_', ' ').title()} score {score} with weight {weight} contributed {contribution} points."
        )

    return explanations


def generate_ats_score(
    candidate_id: str,
    job_id: str,
    role_name: str,
    component_scores: dict
) -> dict:
    weights = get_role_weights(role_name)

    normalized_scores = {
        "skill_match": normalize_score(component_scores.get("skill_match")),
        "experience_relevance": normalize_score(component_scores.get("experience_relevance")),
        "education_alignment": normalize_score(component_scores.get("education_alignment")),
        "semantic_similarity": normalize_score(component_scores.get("semantic_similarity"))
    }

    weighted_components = {}

    for component, score in normalized_scores.items():
        weighted_components[component] = calculate_weighted_score(
            score,
            weights.get(component, 0)
        )

    final_score = round(sum(weighted_components.values()), 2)

    return {
        "candidate_id": candidate_id,
        "job_id": job_id,
        "role_name": role_name,
        "weights_used": weights,
        "component_scores": normalized_scores,
        "weighted_components": weighted_components,
        "final_ats_score": final_score,
        "fit_category": classify_candidate(final_score),
        "explanation": generate_explanation(normalized_scores, weights)
    }


def save_ats_score(
    candidate_id: str,
    job_id: str,
    role_name: str,
    component_scores: dict,
    output_file: str = "data/ats_score_outputs/candidate_ats_score.json"
) -> str:
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)

    ats_score = generate_ats_score(
        candidate_id=candidate_id,
        job_id=job_id,
        role_name=role_name,
        component_scores=component_scores
    )

    Path(output_file).write_text(
        json.dumps(ats_score, indent=2),
        encoding="utf-8"
    )

    return output_file

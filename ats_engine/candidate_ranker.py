import json
from pathlib import Path


SHORTLIST_THRESHOLD = 75
REVIEW_THRESHOLD = 50


def classify_candidate_status(score: float) -> str:
    if score >= SHORTLIST_THRESHOLD:
        return "Shortlisted"
    if score >= REVIEW_THRESHOLD:
        return "Review"
    return "Rejected"


def rank_candidates(candidates: list[dict]) -> list[dict]:
    ranked_candidates = sorted(
        candidates,
        key=lambda candidate: candidate.get("final_ats_score", 0),
        reverse=True
    )

    for rank, candidate in enumerate(ranked_candidates, start=1):
        score = candidate.get("final_ats_score", 0)

        candidate["rank"] = rank
        candidate["status"] = classify_candidate_status(score)

    return ranked_candidates


def get_top_candidates(candidates: list[dict], limit: int = 5) -> list[dict]:
    ranked_candidates = rank_candidates(candidates)

    return ranked_candidates[:limit]


def generate_shortlisting_summary(ranked_candidates: list[dict]) -> dict:
    shortlisted = [
        candidate for candidate in ranked_candidates
        if candidate["status"] == "Shortlisted"
    ]

    review = [
        candidate for candidate in ranked_candidates
        if candidate["status"] == "Review"
    ]

    rejected = [
        candidate for candidate in ranked_candidates
        if candidate["status"] == "Rejected"
    ]

    return {
        "total_candidates": len(ranked_candidates),
        "shortlisted_count": len(shortlisted),
        "review_count": len(review),
        "rejected_count": len(rejected)
    }


def generate_ranked_candidate_output(candidates: list[dict]) -> dict:
    ranked_candidates = rank_candidates(candidates)
    summary = generate_shortlisting_summary(ranked_candidates)

    return {
        "shortlisting_threshold": SHORTLIST_THRESHOLD,
        "review_threshold": REVIEW_THRESHOLD,
        "summary": summary,
        "ranked_candidates": ranked_candidates
    }


def save_ranked_candidates(
    candidates: list[dict],
    output_file: str = "data/ranking_outputs/ranked_candidates.json"
) -> str:
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)

    ranked_output = generate_ranked_candidate_output(candidates)

    Path(output_file).write_text(
        json.dumps(ranked_output, indent=2),
        encoding="utf-8"
    )

    return output_file

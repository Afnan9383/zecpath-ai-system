from ats_engine.candidate_ranker import (
    classify_candidate_status,
    rank_candidates,
    get_top_candidates,
    generate_shortlisting_summary
)


def test_classify_candidate_status():
    assert classify_candidate_status(80) == "Shortlisted"
    assert classify_candidate_status(60) == "Review"
    assert classify_candidate_status(40) == "Rejected"


def test_rank_candidates():
    candidates = [
        {"candidate_id": "C1", "final_ats_score": 70},
        {"candidate_id": "C2", "final_ats_score": 90}
    ]

    ranked = rank_candidates(candidates)

    assert ranked[0]["candidate_id"] == "C2"
    assert ranked[0]["rank"] == 1


def test_get_top_candidates():
    candidates = [
        {"candidate_id": "C1", "final_ats_score": 70},
        {"candidate_id": "C2", "final_ats_score": 90},
        {"candidate_id": "C3", "final_ats_score": 85}
    ]

    top_candidates = get_top_candidates(candidates, limit=2)

    assert len(top_candidates) == 2
    assert top_candidates[0]["candidate_id"] == "C2"


def test_generate_shortlisting_summary():
    candidates = [
        {"candidate_id": "C1", "final_ats_score": 80},
        {"candidate_id": "C2", "final_ats_score": 60},
        {"candidate_id": "C3", "final_ats_score": 30}
    ]

    ranked = rank_candidates(candidates)
    summary = generate_shortlisting_summary(ranked)

    assert summary["shortlisted_count"] == 1
    assert summary["review_count"] == 1
    assert summary["rejected_count"] == 1

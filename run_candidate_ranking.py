from ats_engine.candidate_ranker import save_ranked_candidates


candidates = [
    {
        "candidate_id": "C123",
        "candidate_name": "Afnan",
        "job_id": "J456",
        "final_ats_score": 86.5,
        "fit_category": "Strong Fit"
    },
    {
        "candidate_id": "C124",
        "candidate_name": "Rahul",
        "job_id": "J456",
        "final_ats_score": 72.0,
        "fit_category": "Good Fit"
    },
    {
        "candidate_id": "C125",
        "candidate_name": "Neha",
        "job_id": "J456",
        "final_ats_score": 48.0,
        "fit_category": "Average Fit"
    },
    {
        "candidate_id": "C126",
        "candidate_name": "Arjun",
        "job_id": "J456",
        "final_ats_score": 91.0,
        "fit_category": "Strong Fit"
    }
]

output_path = save_ranked_candidates(
    candidates,
    output_file="data/ranking_outputs/ranked_candidates.json"
)

print(f"Ranked candidate output saved at: {output_path}")

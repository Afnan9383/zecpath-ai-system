from ats_engine.ats_score_generator import save_ats_score


component_scores = {
    "skill_match": 85,
    "experience_relevance": 78,
    "education_alignment": 90,
    "semantic_similarity": 82
}

output_path = save_ats_score(
    candidate_id="C123",
    job_id="J456",
    role_name="Data Scientist",
    component_scores=component_scores,
    output_file="data/ats_score_outputs/candidate_ats_score.json"
)

print(f"ATS score output saved at: {output_path}")

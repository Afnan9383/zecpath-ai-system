from utils.fairness_normalizer import save_fairness_report


resume_text = """
Afnan T
Email: afnan@example.com
Phone: +91 9876543210
Gender: Female
Python developer with machine learning and data science experience.
Completed MCA and worked on AI projects.
"""

scores = {
    "skill_match": 88,
    "experience_relevance": 76,
    "education_alignment": 90,
    "semantic_similarity": 82
}

weights = {
    "skill_match": 0.35,
    "experience_relevance": 0.25,
    "education_alignment": 0.20,
    "semantic_similarity": 0.20
}

output_path = save_fairness_report(
    candidate_id="C123",
    resume_text=resume_text,
    scores=scores,
    weights=weights,
    output_file="data/fairness_outputs/fairness_report.json"
)

print(f"Fairness report saved at: {output_path}")

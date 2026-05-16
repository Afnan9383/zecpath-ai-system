from ats_engine.semantic_matcher import save_similarity_output


resume_profile = {
    "skills": ["Python", "Machine Learning", "Data Science", "SQL", "Power BI"],
    "experience_summary": "Worked on machine learning models, data analysis, dashboards, and AI-based prediction systems.",
    "projects": "Built AI-powered resume screening system and data visualization dashboards."
}

jd_profile = {
    "required_skills": ["Python", "Machine Learning", "Data Analytics", "SQL"],
    "job_description": "Looking for a data scientist with experience in machine learning, Python, analytics, and prediction models.",
    "responsibilities": [
        "Build machine learning models",
        "Analyze datasets",
        "Create dashboards",
        "Support AI-based decision making"
    ]
}

output_path = save_similarity_output(
    resume_profile=resume_profile,
    jd_profile=jd_profile,
    candidate_id="C123",
    job_id="J456",
    output_file="data/matching_outputs/resume_jd_similarity.json"
)

print(f"Resume-JD similarity output saved at: {output_path}")

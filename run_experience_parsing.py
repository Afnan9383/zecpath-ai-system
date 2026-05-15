from parsers.experience_parser import save_experience_output


sample_resume_text = """
WORK EXPERIENCE
Data Scientist Intern at ABC Analytics 2023 - 2024
Worked on machine learning models, Python data pipelines, and AI dashboards.

Python Developer at TechSoft Solutions 2021 - 2023
Developed backend APIs and automated reporting tools.

EDUCATION
Master of Computer Applications
"""

output_path = save_experience_output(
    resume_text=sample_resume_text,
    candidate_id="C123",
    target_role="Data Scientist",
    output_file="data/experience_outputs/candidate_experience.json"
)

print(f"Structured experience output saved at: {output_path}")

from ats_engine.skill_extractor import save_structured_skill_output


sample_text = """
Python Developer with experience in Django and REST APIs.
Worked on MERN stack projects.
Strong communication and leadership skills.
"""

output_path = save_structured_skill_output(
    resume_text=sample_text,
    candidate_id="C123",
    output_file="data/skill_outputs/candidate_skills.json"
)

print(f"Structured skill output saved at: {output_path}")

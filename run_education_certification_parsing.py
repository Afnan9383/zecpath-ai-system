from parsers.education_certification_parser import save_academic_profile


sample_resume_text = """
EDUCATION
2023-2025 Master of Computer Applications (MCA), KMCT College of Engineering
2014-2017 Bachelor of Science in Mathematics, MAMO College

CERTIFICATIONS
Cyber Security & AI/ML - NIELIT
Advanced Diploma in Data Science & Artificial Intelligence
Power BI Data Analytics Certification
"""

output_path = save_academic_profile(
    resume_text=sample_resume_text,
    candidate_id="C123",
    target_role="Data Scientist",
    output_file="data/academic_outputs/candidate_academic_profile.json"
)

print(f"Structured academic profile saved at: {output_path}")

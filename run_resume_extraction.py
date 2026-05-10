from parsers.resume_text_extractor import save_extracted_text

resume_path = "data/resumes/sample_resume.pdf"

output_path = save_extracted_text(resume_path)

print(f"Extracted resume text saved at: {output_path}")

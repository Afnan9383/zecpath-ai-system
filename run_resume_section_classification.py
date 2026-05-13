from parsers.resume_section_classifier import save_labeled_resume_sample


input_file = "data/extracted_resumes/sample_resume.txt"

output_path = save_labeled_resume_sample(input_file)

print(f"Labeled resume sample saved at: {output_path}")

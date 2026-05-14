# Day 8 - Resume Section Detection Accuracy Report

## Objective

The objective of Day 8 is to automatically identify and separate major resume sections so downstream AI models can work on structured and meaningful content.

## Resume Sections Detected

The classifier detects the following sections:

- Profile
- Skills
- Work Experience
- Education
- Certifications
- Projects
- Achievements
- Personal Details
- Unknown

## Detection Methods

### 1. Rule-Based Detection

The system identifies common resume headings such as:

- Skills
- Technical Skills
- Work Experience
- Education
- Certifications
- Projects
- Profile

When a heading is found, the following lines are grouped under that section.

### 2. Keyword-Based Detection

If a section heading is missing, the system uses keywords to classify the text.

Examples:

- Python, SQL, Machine Learning → Skills
- MCA, College, University → Education
- Project, Developed, Implemented → Projects

## Labeled Resume Output

The labeled output is stored at:

```text
data/labeled_resumes/sample_resume_labeled.json

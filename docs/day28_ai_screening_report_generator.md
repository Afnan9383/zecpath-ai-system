# Day 28 - AI Screening Report Generator

## Objective

The objective of Day 28 is to transform raw AI screening evaluations into recruiter-friendly screening reports.

## Key Features

- Structured screening report generation
- Key answer summarization
- Strength identification
- Risk identification
- Missing data detection
- Salary expectation highlighting
- Availability highlighting
- Skill confirmation highlighting
- Exportable JSON report format

## Report Sections

### Candidate Information

Includes:

- candidate_id
- job_id
- report_type

### Final Screening Result

Includes:

- final_screening_score
- recommendation

### Highlights

Includes:

- salary_expectation
- availability
- confirmed_skills
- experience_years

### Key Answers

Summarizes important candidate answers.

### Strengths

Identifies positive screening signals.

### Risks

Identifies weak communication, vague answers, off-topic answers, or low score.

### Missing Data

Lists important information not provided by the candidate.

### Behavioral Summary

Includes confidence, sentiment, communication strength, and behavioral flags.

### Score Breakdown

Includes per-question screening score details.

## Sample Output

```json
{
  "candidate_id": "C123",
  "job_id": "J101",
  "report_type": "AI Screening Report",
  "final_screening_score": 82.5,
  "recommendation": "Proceed to HR Interview",
  "highlights": {
    "salary_expectation": "6 lpa",
    "availability": "Immediate",
    "confirmed_skills": ["python", "django"],
    "experience_years": 3
  },
  "strengths": [
    "Strong overall screening performance",
    "Strong communication in screening responses",
    "Confirmed skill: python",
    "Confirmed skill: django"
  ],
  "risks": [],
  "missing_data": []
}



Data Flow
Answer Understanding Output
↓
Screening Score Output
↓
Behavioral Signal Output
↓
Screening Report Generator
↓
Recruiter-Friendly Report
↓
Exportable JSON
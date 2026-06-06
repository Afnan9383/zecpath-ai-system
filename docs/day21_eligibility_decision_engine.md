# Day 21 - Eligibility Decision Engine

## Objective

The Eligibility Decision Engine decides whether a candidate qualifies for the next AI screening stage based on ATS score and recruiter-defined job rules.

## Eligibility Parameters

- Minimum ATS score
- Review ATS score
- Mandatory skills
- Minimum experience
- Maximum experience
- Allowed locations
- Required availability

## Rule Configuration Format

```json
{
  "job_id": "J101",
  "job_role": "Backend Developer",
  "min_ats_score": 75,
  "review_ats_score": 50,
  "mandatory_skills": ["Python", "Django"],
  "min_experience": 2,
  "max_experience": 5,
  "allowed_locations": ["Remote", "Bangalore", "Kochi"],
  "required_availability": "Immediate"
}
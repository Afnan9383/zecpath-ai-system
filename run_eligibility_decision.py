import json
import os

from ats_engine.eligibility_engine import decide_eligibility


candidate = {
    "candidate_id": "C123",
    "ats_score": 82,
    "skills": ["Python", "Django", "SQL"],
    "experience_years": 3,
    "location": "Remote",
    "availability": "Immediate"
}

rules = {
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

result = decide_eligibility(candidate, rules)

os.makedirs("data/eligibility_outputs", exist_ok=True)

with open("data/eligibility_outputs/candidate_eligibility.json", "w") as file:
    json.dump(result, file, indent=4)

print(result)
print("Eligibility result saved at: data/eligibility_outputs/candidate_eligibility.json")
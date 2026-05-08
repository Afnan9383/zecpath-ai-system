def calculate_ats_score(candidate_skills, required_skills):
    matched_skills = set(candidate_skills).intersection(set(required_skills))
    score = len(matched_skills) / len(required_skills) * 100

    return {
        "matched_skills": list(matched_skills),
        "ats_score": round(score, 2)
    }

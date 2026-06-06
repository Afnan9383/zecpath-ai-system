def check_mandatory_skills(candidate_skills, mandatory_skills):
    candidate_skills = [skill.lower() for skill in candidate_skills]
    missing_skills = []

    for skill in mandatory_skills:
        if skill.lower() not in candidate_skills:
            missing_skills.append(skill)

    return missing_skills


def check_experience(candidate_experience, min_experience, max_experience):
    if candidate_experience < min_experience:
        return "below_minimum"

    if max_experience is not None and candidate_experience > max_experience:
        return "above_maximum"

    return "matched"


def check_location(candidate_location, allowed_locations):
    if not allowed_locations:
        return True

    return candidate_location.lower() in [location.lower() for location in allowed_locations]


def check_availability(candidate_availability, required_availability):
    if not required_availability:
        return True

    return candidate_availability.lower() == required_availability.lower()


def decide_eligibility(candidate, rules):
    ats_score = candidate.get("ats_score", 0)
    candidate_skills = candidate.get("skills", [])
    candidate_experience = candidate.get("experience_years", 0)
    candidate_location = candidate.get("location", "")
    candidate_availability = candidate.get("availability", "")

    min_ats_score = rules.get("min_ats_score", 70)
    review_ats_score = rules.get("review_ats_score", 50)
    mandatory_skills = rules.get("mandatory_skills", [])
    min_experience = rules.get("min_experience", 0)
    max_experience = rules.get("max_experience")
    allowed_locations = rules.get("allowed_locations", [])
    required_availability = rules.get("required_availability", "")

    missing_skills = check_mandatory_skills(candidate_skills, mandatory_skills)
    experience_status = check_experience(
        candidate_experience,
        min_experience,
        max_experience
    )
    location_matched = check_location(candidate_location, allowed_locations)
    availability_matched = check_availability(
        candidate_availability,
        required_availability
    )

    reasons = []

    if ats_score < review_ats_score:
        reasons.append("ATS score below review cutoff")

    if missing_skills:
        reasons.append(f"Missing mandatory skills: {', '.join(missing_skills)}")

    if experience_status == "below_minimum":
        reasons.append("Experience below minimum requirement")

    if experience_status == "above_maximum":
        reasons.append("Experience above maximum range")

    if not location_matched:
        reasons.append("Location does not match job constraint")

    if not availability_matched:
        reasons.append("Availability does not match requirement")

    if ats_score >= min_ats_score and not reasons:
        decision = "Eligible"
    elif ats_score >= review_ats_score:
        decision = "Review"
    else:
        decision = "Rejected"

    return {
        "candidate_id": candidate.get("candidate_id"),
        "job_id": rules.get("job_id"),
        "ats_score": ats_score,
        "decision": decision,
        "missing_skills": missing_skills,
        "experience_status": experience_status,
        "location_matched": location_matched,
        "availability_matched": availability_matched,
        "reasons": reasons
    }
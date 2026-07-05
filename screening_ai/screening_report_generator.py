# -------------------------------
# Extract Strengths
# -------------------------------
def extract_strengths(screening_score, behavioral_signals, understood_answers):
    strengths = []

    if screening_score.get("final_screening_score", 0) >= 75:
        strengths.append("Strong overall screening performance")

    for signal in behavioral_signals:
        if signal.get("communication_strength") == "Strong":
            strengths.append("Strong communication in screening responses")
            break

    for answer in understood_answers:
        skills = answer.get("skills", [])
        for skill in skills:
            skill_text = f"Confirmed skill: {skill}"
            if skill_text not in strengths:
                strengths.append(skill_text)

    return strengths


# -------------------------------
# Extract Risks
# -------------------------------
def extract_risks(screening_score, behavioral_signals, understood_answers):
    risks = []

    if screening_score.get("final_screening_score", 0) < 50:
        risks.append("Low screening score")

    for signal in behavioral_signals:
        if signal.get("communication_strength") == "Weak":
            risks.append("Weak communication signal detected")
            break

        if "uncertainty_detected" in signal.get("flags", []):
            risks.append("Uncertainty detected in candidate response")
            break

    for answer in understood_answers:
        if answer.get("is_off_topic"):
            risks.append("Off-topic answer detected")
            break

        if answer.get("is_vague"):
            risks.append("Vague or incomplete answer detected")
            break

    return risks


# -------------------------------
# Extract Missing Data
# -------------------------------
def extract_missing_data(understood_answers):
    missing_data = []

    has_salary = any(answer.get("salary_expectation") for answer in understood_answers)
    has_availability = any(answer.get("availability") for answer in understood_answers)
    has_skills = any(answer.get("skills") for answer in understood_answers)
    has_experience = any(answer.get("experience_years") is not None for answer in understood_answers)

    if not has_salary:
        missing_data.append("Salary expectation not provided")

    if not has_availability:
        missing_data.append("Availability not provided")

    if not has_skills:
        missing_data.append("Skills not confirmed")

    if not has_experience:
        missing_data.append("Experience details not provided")

    return missing_data


# -------------------------------
# Highlight Important Screening Data
# -------------------------------
def extract_highlights(understood_answers):
    highlights = {
        "salary_expectation": None,
        "availability": None,
        "confirmed_skills": [],
        "experience_years": None
    }

    for answer in understood_answers:
        if answer.get("salary_expectation"):
            highlights["salary_expectation"] = answer.get("salary_expectation")

        if answer.get("availability"):
            highlights["availability"] = answer.get("availability")

        if answer.get("experience_years") is not None:
            highlights["experience_years"] = answer.get("experience_years")

        for skill in answer.get("skills", []):
            if skill not in highlights["confirmed_skills"]:
                highlights["confirmed_skills"].append(skill)

    return highlights


# -------------------------------
# Summarize Key Answers
# -------------------------------
def summarize_key_answers(understood_answers):
    key_answers = []

    important_intents = [
        "self_introduction",
        "experience_info",
        "skills_info",
        "availability_info",
        "salary_info"
    ]

    for answer in understood_answers:
        if answer.get("intent") in important_intents:
            key_answers.append({
                "question_id": answer.get("question_id"),
                "intent": answer.get("intent"),
                "answer_summary": answer.get("normalized_answer")
            })

    return key_answers


# -------------------------------
# Generate Final Screening Report
# -------------------------------
def generate_screening_report(
    candidate_id,
    job_id,
    understood_answers,
    screening_score,
    behavioral_signals
):
    highlights = extract_highlights(understood_answers)
    strengths = extract_strengths(
        screening_score,
        behavioral_signals,
        understood_answers
    )
    risks = extract_risks(
        screening_score,
        behavioral_signals,
        understood_answers
    )
    missing_data = extract_missing_data(understood_answers)
    key_answers = summarize_key_answers(understood_answers)

    final_score = screening_score.get("final_screening_score", 0)

    if final_score >= 75:
        recommendation = "Proceed to HR Interview"
    elif final_score >= 50:
        recommendation = "Recruiter Review Required"
    else:
        recommendation = "Reject"

    return {
        "candidate_id": candidate_id,
        "job_id": job_id,
        "report_type": "AI Screening Report",
        "final_screening_score": final_score,
        "recommendation": recommendation,
        "highlights": highlights,
        "key_answers": key_answers,
        "strengths": strengths,
        "risks": risks,
        "missing_data": missing_data,
        "behavioral_summary": behavioral_signals,
        "score_breakdown": screening_score.get("scored_answers", [])
    }
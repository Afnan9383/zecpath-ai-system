def final_decision(ats_score, screening_score, interview_score):
    final_score = (ats_score * 0.4) + (screening_score * 0.2) + (interview_score * 0.4)

    if final_score >= 75:
        decision = "Selected"
    elif final_score >= 50:
        decision = "Hold"
    else:
        decision = "Rejected"

    return {
        "final_score": round(final_score, 2),
        "decision": decision
    }

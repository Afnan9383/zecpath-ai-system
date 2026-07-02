# -------------------------------
# Score Normalization
# -------------------------------
def normalize_score(score):
    if score < 0:
        return 0
    if score > 100:
        return 100

    return round(score, 2)


# -------------------------------
# Clarity Scoring
# -------------------------------
def score_clarity(answer):
    normalized_answer = answer.get("normalized_answer", "")
    flags = answer.get("flags", [])

    if not normalized_answer:
        return 0

    score = 100

    if "vague_or_missing_answer" in flags:
        score -= 40

    if len(normalized_answer.split()) < 5:
        score -= 20

    return normalize_score(score)


# -------------------------------
# Relevance Scoring
# -------------------------------
def score_relevance(answer, expected_intent):
    actual_intent = answer.get("intent", "unknown")
    is_off_topic = answer.get("is_off_topic", False)

    if is_off_topic:
        return 0

    if actual_intent == expected_intent:
        return 100

    if actual_intent == "unknown":
        return 40

    return 60


# -------------------------------
# Completeness Scoring
# -------------------------------
def score_completeness(answer):
    score = 50

    if answer.get("skills"):
        score += 15

    if answer.get("experience_years") is not None:
        score += 15

    if answer.get("availability") is not None:
        score += 10

    if answer.get("salary_expectation") is not None:
        score += 10

    if answer.get("is_vague"):
        score -= 30

    return normalize_score(score)


# -------------------------------
# Consistency Scoring
# -------------------------------
def score_consistency(answer):
    if answer.get("is_off_topic"):
        return 0

    if answer.get("is_vague"):
        return 50

    return 90


# -------------------------------
# Per-question Scoring
# -------------------------------
def score_screening_answer(answer, expected_intent):
    clarity = score_clarity(answer)
    relevance = score_relevance(answer, expected_intent)
    completeness = score_completeness(answer)
    consistency = score_consistency(answer)

    final_score = (
        clarity * 0.25 +
        relevance * 0.35 +
        completeness * 0.25 +
        consistency * 0.15
    )

    return {
        "question_id": answer.get("question_id"),
        "expected_intent": expected_intent,
        "actual_intent": answer.get("intent"),
        "scores": {
            "clarity": clarity,
            "relevance": relevance,
            "completeness": completeness,
            "consistency": consistency
        },
        "question_score": normalize_score(final_score),
        "flags": answer.get("flags", []),
        "explanation": generate_score_explanation(
            clarity,
            relevance,
            completeness,
            consistency,
            answer
        )
    }


# -------------------------------
# Explanation Generator
# -------------------------------
def generate_score_explanation(clarity, relevance, completeness, consistency, answer):
    explanations = []

    if clarity >= 80:
        explanations.append("Answer is clear.")
    else:
        explanations.append("Answer clarity needs improvement.")

    if relevance >= 80:
        explanations.append("Answer is relevant to the question.")
    else:
        explanations.append("Answer relevance is low or unclear.")

    if completeness >= 80:
        explanations.append("Answer contains enough useful information.")
    else:
        explanations.append("Answer is missing some important details.")

    if consistency >= 80:
        explanations.append("Answer appears consistent.")
    else:
        explanations.append("Answer may be vague, unclear, or off-topic.")

    if answer.get("flags"):
        explanations.append(f"Flags detected: {', '.join(answer.get('flags'))}.")

    return explanations


# -------------------------------
# Aggregate Screening Score
# -------------------------------
def calculate_final_screening_score(scored_answers):
    if not scored_answers:
        return {
            "final_screening_score": 0,
            "decision": "Rejected",
            "summary": "No screening answers available."
        }

    total_score = sum(answer["question_score"] for answer in scored_answers)
    final_score = round(total_score / len(scored_answers), 2)

    if final_score >= 75:
        decision = "Proceed to HR Interview"
    elif final_score >= 50:
        decision = "Review Required"
    else:
        decision = "Rejected"

    return {
        "final_screening_score": final_score,
        "decision": decision,
        "total_questions": len(scored_answers),
        "scored_answers": scored_answers
    }
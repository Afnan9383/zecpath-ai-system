# -------------------------------
# Conversation States
# -------------------------------
CONVERSATION_STATES = {
    "START": "start",
    "ASK_QUESTION": "ask_question",
    "WAIT_FOR_ANSWER": "wait_for_answer",
    "PROCESS_ANSWER": "process_answer",
    "FOLLOW_UP": "follow_up",
    "RETRY": "retry",
    "SKIP": "skip",
    "END": "end"
}


# -------------------------------
# Fallback Questions
# -------------------------------
FALLBACK_QUESTIONS = {
    "silence": "I could not hear your response. Could you please answer again?",
    "confusion": "No problem. Let me ask that in a simpler way.",
    "vague": "Could you please provide a little more detail?",
    "repeated": "You already mentioned that. Can you add any new information?",
    "general": "Could you please clarify your answer?"
}


# -------------------------------
# Follow-up Questions
# -------------------------------
FOLLOW_UP_QUESTIONS = {
    "experience_info": "Can you briefly explain your most relevant work experience?",
    "skills_info": "Can you give an example of how you used these skills?",
    "availability_info": "Can you confirm your exact joining availability?",
    "salary_info": "Is your salary expectation negotiable?",
    "self_introduction": "Can you summarize your current career goal?"
}


# -------------------------------
# Initial Conversation State
# -------------------------------
def initialize_conversation(candidate_id, job_id, questions):
    return {
        "candidate_id": candidate_id,
        "job_id": job_id,
        "current_state": CONVERSATION_STATES["START"],
        "current_question_index": 0,
        "questions": questions,
        "answers": [],
        "retry_count": 0,
        "max_retries": 2,
        "conversation_status": "active"
    }


# -------------------------------
# Get Current Question
# -------------------------------
def get_current_question(conversation):
    index = conversation.get("current_question_index", 0)
    questions = conversation.get("questions", [])

    if index >= len(questions):
        return None

    return questions[index]


# -------------------------------
# Detect Repeated Answer
# -------------------------------
def is_repeated_answer(answer_text, previous_answers):
    normalized_answer = answer_text.lower().strip()

    for previous in previous_answers:
        previous_text = previous.get("answer_text", "").lower().strip()
        if normalized_answer == previous_text:
            return True

    return False


# -------------------------------
# Decide Next Action
# -------------------------------
def decide_next_action(conversation, answer_analysis):
    flags = answer_analysis.get("flags", [])
    intent = answer_analysis.get("intent", "unknown")
    answer_text = answer_analysis.get("original_answer", "")

    if not answer_text.strip():
        return "retry_silence"

    if is_repeated_answer(answer_text, conversation.get("answers", [])):
        return "fallback_repeated"

    if "vague_or_missing_answer" in flags:
        return "fallback_vague"

    if intent == "unknown":
        return "fallback_confusion"

    if intent in FOLLOW_UP_QUESTIONS:
        return "follow_up"

    return "next_question"


# -------------------------------
# Apply Conversation Action
# -------------------------------
def apply_conversation_action(conversation, action, answer_analysis=None):
    if answer_analysis:
        conversation["answers"].append(answer_analysis)

    if action == "retry_silence":
        conversation["retry_count"] += 1
        conversation["current_state"] = CONVERSATION_STATES["RETRY"]

        if conversation["retry_count"] > conversation["max_retries"]:
            conversation["current_state"] = CONVERSATION_STATES["SKIP"]
            conversation["current_question_index"] += 1
            conversation["retry_count"] = 0

        return conversation

    if action in ["fallback_confusion", "fallback_vague", "fallback_repeated"]:
        conversation["current_state"] = CONVERSATION_STATES["FOLLOW_UP"]
        return conversation

    if action == "follow_up":
        conversation["current_state"] = CONVERSATION_STATES["FOLLOW_UP"]
        return conversation

    if action == "next_question":
        conversation["current_question_index"] += 1
        conversation["retry_count"] = 0

        if conversation["current_question_index"] >= len(conversation["questions"]):
            conversation["current_state"] = CONVERSATION_STATES["END"]
            conversation["conversation_status"] = "completed"
        else:
            conversation["current_state"] = CONVERSATION_STATES["ASK_QUESTION"]

        return conversation

    return conversation


# -------------------------------
# Get AI Prompt Based On Action
# -------------------------------
def get_ai_prompt(action, answer_analysis=None):
    if action == "retry_silence":
        return FALLBACK_QUESTIONS["silence"]

    if action == "fallback_confusion":
        return FALLBACK_QUESTIONS["confusion"]

    if action == "fallback_vague":
        return FALLBACK_QUESTIONS["vague"]

    if action == "fallback_repeated":
        return FALLBACK_QUESTIONS["repeated"]

    if action == "follow_up":
        intent = answer_analysis.get("intent", "unknown")
        return FOLLOW_UP_QUESTIONS.get(intent, FALLBACK_QUESTIONS["general"])

    return None
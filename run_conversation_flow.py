import json
import os

from screening_ai.answer_understanding_engine import understand_answer
from screening_ai.conversation_flow_engine import (
    initialize_conversation,
    get_current_question,
    decide_next_action,
    apply_conversation_action,
    get_ai_prompt
)


questions = [
    {
        "question_id": "Q001",
        "question_text": "Please introduce yourself briefly.",
        "expected_intent": "self_introduction"
    },
    {
        "question_id": "Q003",
        "question_text": "How many years of relevant work experience do you have?",
        "expected_intent": "experience_info"
    },
    {
        "question_id": "Q009",
        "question_text": "What is your notice period?",
        "expected_intent": "availability_info"
    }
]

candidate_answers = [
    "",
    "Maybe I am not sure.",
    "I have three years experience in Python.",
    "I can join immediately."
]

conversation = initialize_conversation("C123", "J101", questions)
conversation["current_state"] = "ask_question"

events = []

for answer_text in candidate_answers:
    current_question = get_current_question(conversation)

    if current_question is None:
        break

    answer_analysis = understand_answer(
        current_question["question_id"],
        answer_text
    )

    action = decide_next_action(conversation, answer_analysis)
    ai_prompt = get_ai_prompt(action, answer_analysis)

    events.append({
        "question_id": current_question["question_id"],
        "candidate_answer": answer_text,
        "detected_intent": answer_analysis.get("intent"),
        "action": action,
        "ai_prompt": ai_prompt
    })

    conversation = apply_conversation_action(
        conversation,
        action,
        answer_analysis
    )

    if action in ["next_question"]:
        continue

os.makedirs("data/conversation_flow_outputs", exist_ok=True)

output = {
    "conversation": conversation,
    "events": events
}

with open("data/conversation_flow_outputs/sample_conversation_flow.json", "w") as file:
    json.dump(output, file, indent=4)

print(output)
print("Conversation flow saved at: data/conversation_flow_outputs/sample_conversation_flow.json")
import json
import os

from screening_ai.answer_understanding_engine import understand_answer
from screening_ai.screening_scoring_engine import (
    score_screening_answer,
    calculate_final_screening_score
)


sample_answers = [
    {
        "question_id": "Q001",
        "answer_text": "My name is Afnan and I am interested in AI and Data Science.",
        "expected_intent": "self_introduction"
    },
    {
        "question_id": "Q003",
        "answer_text": "I have three years experience in Python and Django.",
        "expected_intent": "experience_info"
    },
    {
        "question_id": "Q009",
        "answer_text": "I can join immediately.",
        "expected_intent": "availability_info"
    },
    {
        "question_id": "Q008",
        "answer_text": "My expected salary is 6 LPA.",
        "expected_intent": "salary_info"
    },
    {
        "question_id": "Q010",
        "answer_text": "Maybe I am not sure.",
        "expected_intent": "availability_info"
    }
]

scored_answers = []

for item in sample_answers:
    understood_answer = understand_answer(
        item["question_id"],
        item["answer_text"]
    )

    scored_answer = score_screening_answer(
        understood_answer,
        item["expected_intent"]
    )

    scored_answers.append(scored_answer)

final_result = calculate_final_screening_score(scored_answers)

os.makedirs("data/screening_score_outputs", exist_ok=True)

with open("data/screening_score_outputs/final_screening_score.json", "w") as file:
    json.dump(final_result, file, indent=4)

print(final_result)
print("Final screening score saved at: data/screening_score_outputs/final_screening_score.json")
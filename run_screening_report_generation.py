import json
import os

from screening_ai.answer_understanding_engine import understand_answer
from screening_ai.screening_scoring_engine import (
    score_screening_answer,
    calculate_final_screening_score
)
from screening_ai.confidence_sentiment_analyzer import analyze_behavioral_signals
from screening_ai.screening_report_generator import generate_screening_report


candidate_id = "C123"
job_id = "J101"

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
    }
]

understood_answers = []
scored_answers = []
behavioral_signals = []

for item in sample_answers:
    understood_answer = understand_answer(
        item["question_id"],
        item["answer_text"]
    )
    understood_answers.append(understood_answer)

    scored_answer = score_screening_answer(
        understood_answer,
        item["expected_intent"]
    )
    scored_answers.append(scored_answer)

    behavioral_signal = analyze_behavioral_signals(
        item["question_id"],
        item["answer_text"]
    )
    behavioral_signals.append(behavioral_signal)

screening_score = calculate_final_screening_score(scored_answers)

report = generate_screening_report(
    candidate_id,
    job_id,
    understood_answers,
    screening_score,
    behavioral_signals
)

os.makedirs("data/screening_reports", exist_ok=True)

with open("data/screening_reports/sample_screening_report.json", "w") as file:
    json.dump(report, file, indent=4)

print(report)
print("Screening report saved at: data/screening_reports/sample_screening_report.json")
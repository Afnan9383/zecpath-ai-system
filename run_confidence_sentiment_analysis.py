import json
import os

from screening_ai.confidence_sentiment_analyzer import analyze_behavioral_signals


answers = [
    {
        "question_id": "Q001",
        "answer_text": "I am confident and passionate about AI development."
    },
    {
        "question_id": "Q003",
        "answer_text": "Um I think maybe I have some experience in Python."
    },
    {
        "question_id": "Q009",
        "answer_text": "I can join immediately but maybe after 30 days."
    },
    {
        "question_id": "Q010",
        "answer_text": "Yes."
    }
]

results = []

for answer in answers:
    result = analyze_behavioral_signals(
        answer["question_id"],
        answer["answer_text"]
    )
    results.append(result)

os.makedirs("data/behavioral_signal_outputs", exist_ok=True)

with open("data/behavioral_signal_outputs/behavioral_indicators.json", "w") as file:
    json.dump(results, file, indent=4)

print(results)
print("Behavioral indicators saved at: data/behavioral_signal_outputs/behavioral_indicators.json")
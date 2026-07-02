import json
import os

from screening_ai.answer_understanding_engine import understand_answer


answers = [
    {
        "question_id": "Q001",
        "answer_text": "My name is Afnan and I am interested in AI and Data Science."
    },
    {
        "question_id": "Q003",
        "answer_text": "I have three years experience in Python and Django."
    },
    {
        "question_id": "Q009",
        "answer_text": "I can join immediately."
    },
    {
        "question_id": "Q008",
        "answer_text": "My expected salary is 6 LPA."
    },
    {
        "question_id": "Q010",
        "answer_text": "Maybe I am not sure."
    },
    {
        "question_id": "Q011",
        "answer_text": "I like movies and music."
    }
]

results = []

for answer in answers:
    result = understand_answer(
        answer["question_id"],
        answer["answer_text"]
    )
    results.append(result)

os.makedirs("data/answer_understanding_outputs", exist_ok=True)

with open("data/answer_understanding_outputs/structured_answers.json", "w") as file:
    json.dump(results, file, indent=4)

print(results)
print("Structured answers saved at: data/answer_understanding_outputs/structured_answers.json")
import json
import os

from screening_ai.clean_transcript_processor import process_audio_transcript


samples = [
    {
        "audio_file": "sample_intro.wav",
        "question_id": "Q001",
        "candidate_id": "C123",
        "job_id": "J101"
    },
    {
        "audio_file": "sample_experience.wav",
        "question_id": "Q003",
        "candidate_id": "C123",
        "job_id": "J101"
    },
    {
        "audio_file": "sample_silence.wav",
        "question_id": "Q004",
        "candidate_id": "C123",
        "job_id": "J101"
    },
    {
        "audio_file": "sample_partial.wav",
        "question_id": "Q009",
        "candidate_id": "C123",
        "job_id": "J101"
    }
]

results = []

for sample in samples:
    result = process_audio_transcript(
        sample["audio_file"],
        sample["question_id"],
        sample["candidate_id"],
        sample["job_id"]
    )
    results.append(result)

os.makedirs("data/stt_outputs", exist_ok=True)

with open("data/stt_outputs/clean_transcript_results.json", "w") as file:
    json.dump(results, file, indent=4)

print(results)
print("Clean transcript results saved at: data/stt_outputs/clean_transcript_results.json")
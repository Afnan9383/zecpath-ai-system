# Day 26 - Screening Scoring Engine

## Objective

The objective of Day 26 is to objectively evaluate candidate screening responses using clarity, relevance, completeness, and consistency.

## Scoring Parameters

### Clarity

Checks whether the answer is understandable and not vague.

### Relevance

Checks whether the answer matches the expected question intent.

### Completeness

Checks whether the answer contains enough useful information.

### Consistency

Checks whether the answer is stable, meaningful, and not off-topic.

## Score Weights

| Parameter | Weight |
|---|---|
| Clarity | 25% |
| Relevance | 35% |
| Completeness | 25% |
| Consistency | 15% |

## Per-question Score Output

```json
{
  "question_id": "Q003",
  "expected_intent": "experience_info",
  "actual_intent": "experience_info",
  "scores": {
    "clarity": 100,
    "relevance": 100,
    "completeness": 80,
    "consistency": 90
  },
  "question_score": 92.5,
  "flags": [],
  "explanation": [
    "Answer is clear.",
    "Answer is relevant to the question.",
    "Answer contains enough useful information.",
    "Answer appears consistent."
  ]
}







Decision Logic
Score Range	Decision
75 and above	Proceed to HR Interview
50 to 74	Review Required
Below 50	Rejected
Data Flow
Structured Answer
↓
Clarity Scoring
↓
Relevance Scoring
↓
Completeness Scoring
↓
Consistency Scoring
↓
Per-question Score
↓
Final Screening Score
↓
Screening Decision
# Day 27 - Confidence & Sentiment Signal Analysis

## Objective

The objective of Day 27 is to assess candidate communication quality and behavioral indicators during AI screening.

## Key Features

- Hesitation pattern detection
- Response length measurement
- Sentiment scoring
- Uncertainty detection
- Contradiction detection
- Communication strength classification

## Behavioral Signals

### Hesitation Patterns

Detected words:

- um
- uh
- maybe
- I think
- not sure
- kind of
- probably

### Sentiment Signals

Positive words include:

- confident
- interested
- passionate
- excited
- strong
- ready
- motivated

Negative words include:

- difficult
- weak
- confused
- unable
- poor
- struggle

### Communication Strength

Communication strength is classified as:

- Strong
- Moderate
- Weak

## Output Structure

```json
{
  "question_id": "Q001",
  "answer_text": "I am confident and passionate about AI development.",
  "response_length_words": 7,
  "hesitation_patterns": [],
  "uncertainty_patterns": [],
  "contradictions": [],
  "sentiment_score": 70,
  "sentiment_label": "Positive",
  "confidence_score": 80,
  "communication_strength": "Strong",
  "flags": []
}




Data Flow
Candidate Answer
↓
Normalize Text
↓
Detect Hesitation
↓
Detect Uncertainty
↓
Detect Contradictions
↓
Calculate Sentiment Score
↓
Calculate Confidence Score
↓
Classify Communication Strength
↓
Behavioral Indicator Report
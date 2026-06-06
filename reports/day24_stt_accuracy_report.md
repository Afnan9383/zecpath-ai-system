# Day 24 - STT Accuracy Test Report

## Objective

To test speech-to-text transcript processing and clean raw voice input into structured text for AI screening analysis.

## STT Integration Type

For this stage, a mock speech-to-text function is used.

In production, this can be replaced with:

- Google Speech-to-Text
- Azure Speech Service
- AWS Transcribe
- OpenAI Whisper
- Local Whisper model

## Test Conditions

| Test Case | Input Type | Result |
|---|---|---|
| Introduction answer | Normal speech | Processed |
| Experience answer | Filler words | Processed |
| Silence | Empty speech | Silence detected |
| Partial answer | Uncertain speech | Flagged for review |

## Cleaning Rules Applied

- Convert text to lowercase
- Remove filler words
- Normalize extra spaces
- Add basic punctuation
- Detect silence
- Detect partial or uncertain answers

## Sample Result

```json
{
  "raw_transcript": "Um my name is Afnan and I am interested in AI and data science",
  "cleaned_transcript": "my name is afnan and i am interested in ai and data science.",
  "status": "processed",
  "flags": []
}
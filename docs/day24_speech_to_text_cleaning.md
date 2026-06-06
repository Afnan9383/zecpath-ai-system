# Day 24 - Speech-to-Text Integration & Cleaning

## Objective

The objective of Day 24 is to convert raw voice input into clean, structured transcript text for AI screening analysis.

## Modules Created

- transcript_normalizer.py
- clean_transcript_processor.py
- run_transcript_processing.py

## Key Features

1. Mock Speech-To-Text Integration

A mock STT function is used to simulate voice-to-text conversion.

2. Filler Word Removal

Removes words such as:

- um
- uh
- like
- you know
- actually
- basically

3. Case Normalization

Converts transcript text into lowercase.

4. Space Normalization

Removes repeated spaces.

5. Basic Punctuation Correction

Adds ending punctuation when missing.

6. Silence Detection

Detects empty transcript responses.

7. Partial Answer Detection

Flags uncertain answers containing phrases like:

- I think
- maybe
- not sure
- I don't know

## Data Flow

Audio Input  
↓  
Speech-To-Text Conversion  
↓  
Raw Transcript  
↓  
Transcript Cleaning  
↓  
Silence / Partial Answer Detection  
↓  
Clean Transcript Output  
↓  
AI Screening Analysis  

## Output Structure

```json
{
  "candidate_id": "C123",
  "job_id": "J101",
  "question_id": "Q001",
  "audio_file": "sample_intro.wav",
  "raw_transcript": "Um my name is Afnan and I am interested in AI and data science",
  "cleaned_transcript": "my name is afnan and i am interested in ai and data science.",
  "status": "processed",
  "flags": []
}
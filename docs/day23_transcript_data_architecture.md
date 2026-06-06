# Day 23 - Transcript Data Architecture

## Objective

The objective of Day 23 is to define how AI screening voice conversations are converted into structured, AI-processable transcript data.

## What Is A Transcript?

A transcript is the text version of a voice conversation. In Zecpath, candidate answers from AI screening calls are converted into text and stored with metadata for analysis and scoring.

## Voice Transcript Schema

Each transcript contains:

- transcript_id
- candidate_id
- job_id
- screening_session_id
- language
- started_at
- completed_at
- transcript_entries

Each transcript entry contains:

- question_id
- question_text
- answer_text
- timestamp
- confidence_level
- speaker
- answer_duration_seconds

## AI Screening Data Structure

After transcript normalization, the AI screening system stores structured answer data.

Each answer contains:

- question_id
- category
- normalized_answer
- answer_type
- confidence_level
- score
- flags

## Metadata Standards

Important metadata fields:

- Candidate ID
- Job ID
- Question ID
- Timestamp
- Confidence level
- Screening session ID
- Language
- Model version

## Transcript Normalization Rules

- Convert text to lowercase
- Remove unwanted symbols
- Remove extra spaces
- Standardize common terms
- Detect unclear answers
- Preserve original transcript for audit

## Database Schema Design

### Screening Sessions Table

| Field | Description |
|---|---|
| screening_session_id | Unique screening session ID |
| candidate_id | Candidate identifier |
| job_id | Job identifier |
| status | pending/completed/failed |
| started_at | Screening start time |
| completed_at | Screening completion time |
| language | Screening language |

### Transcript Entries Table

| Field | Description |
|---|---|
| transcript_entry_id | Unique transcript entry ID |
| screening_session_id | Related screening session |
| question_id | Question asked |
| answer_text | Candidate answer |
| normalized_answer | Cleaned answer |
| timestamp | Answer time |
| confidence_level | Speech-to-text confidence |

### Screening Results Table

| Field | Description |
|---|---|
| result_id | Unique result ID |
| screening_session_id | Related screening session |
| communication_score | Communication score |
| final_screening_score | Final screening score |
| recommendation | AI recommendation |
| processed_at | Processing timestamp |

## Screening Data Flow

AI Screening Call  
↓  
Speech-To-Text Conversion  
↓  
Raw Transcript Storage  
↓  
Transcript Normalization  
↓  
Structured Answer Object  
↓  
Screening Score Generation  
↓  
Screening Result Storage  

## Importance

Transcript data architecture helps Zecpath convert unstructured voice conversations into structured AI-ready data. This allows the system to analyze candidate answers, generate screening scores, and support explainable hiring decisions.

## Future Improvements

- Add multilingual transcript support
- Add sentiment analysis
- Add answer quality scoring
- Add confidence-based review flags
- Integrate with voice AI services
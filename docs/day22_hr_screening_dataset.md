# Day 22 - HR Screening Dataset Creation

## Objective

The objective of Day 22 is to create a structured, AI-ready HR screening question dataset for automated screening calls.

## Dataset Purpose

The HR screening dataset helps the AI interviewer ask consistent questions to candidates before moving them to advanced interview stages.

## Question Categories

- Introduction
- Education
- Experience
- Skills
- Location
- Salary
- Notice Period
- Availability
- Career Goals
- Communication

## Question Tagging Fields

Each question contains:

- question_id
- category
- question_text
- expected_answer_type
- mandatory
- scoring_importance
- roles

## Example Question Object

```json
{
  "question_id": "Q001",
  "category": "Introduction",
  "question_text": "Please introduce yourself briefly.",
  "expected_answer_type": "open_text",
  "mandatory": true,
  "scoring_importance": "high",
  "roles": ["all"]
}
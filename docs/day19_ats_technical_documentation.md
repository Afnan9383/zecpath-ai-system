# Day 19 - ATS Technical Documentation

## Project Title

Zecpath AI Hiring System

## Objective

The objective of the ATS system is to automate resume processing, job matching, candidate scoring, ranking, and shortlisting using AI-powered modules.

## Core ATS Modules

- Resume Text Extraction Engine
- Resume Section Classifier
- Skill Extraction Engine
- Experience Parsing Engine
- Education & Certification Parser
- Job Description Parser
- Semantic Matching Engine
- ATS Score Generator
- Candidate Ranking Engine
- Fairness & Bias Reduction Module

## Data Flow

```text
Resume Upload
        ↓
Resume Text Extraction
        ↓
Resume Section Classification
        ↓
Skill / Experience / Education Parsing
        ↓
Job Description Parsing
        ↓
Semantic Matching
        ↓
ATS Score Generation
        ↓
Fairness Normalization
        ↓
Candidate Ranking
        ↓
Shortlisting Output


Important Folders
parsers/        Resume and JD parsing modules
ats_engine/     ATS scoring, matching, ranking modules
utils/          Logging and fairness utilities
data/           Input and output data
tests/          Automated test scripts
docs/           Documentation
reports/        Evaluation and performance reports
benchmarks/     Performance benchmark scripts
Main Outputs
Cleaned resume text
Structured JD profiles
Skill output
Experience output
Academic profile
Semantic similarity output
ATS score output
Ranked candidate output
Fairness report
Performance benchmark report
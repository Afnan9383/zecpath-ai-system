# Day 16 - ATS API Integration Flow

## Objective

This document explains how backend systems integrate with the Zecpath ATS AI modules.

---

## 1. End-to-End Integration Flow

```text
[Frontend Candidate Portal]
        ↓
[Backend API]
        ↓
[POST /ats/resumes/upload]
        ↓
[Resume Stored in Raw Storage]
        ↓
[Async Job Created]
        ↓
[Resume Parsing AI]
        ↓
[Skill Extraction + Experience Parsing + Education Parsing]
        ↓
[Semantic Matching AI]
        ↓
[ATS Scoring AI]
        ↓
[Candidate Ranking / Shortlisting]
        ↓
[Backend Receives Result]
        ↓
[Recruiter Dashboard Displays Candidate Status]

# Day 16 - API Input/Output Schemas

## Objective

This document defines standard input and output schemas for ATS AI API integration.

---

## 1. Resume Upload Input Schema

```json
{
  "candidate_id": "string",
  "job_id": "string",
  "resume_file": "PDF | DOCX"
}


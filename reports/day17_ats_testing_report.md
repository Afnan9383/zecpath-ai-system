# Day 17 - ATS System Testing Report

## Objective

The objective of Day 17 is to validate ATS accuracy, reliability, and role adaptability across different candidate profiles and job types.

## Testing Scope

The ATS system was tested across the following categories:

- Tech roles
- Non-tech roles
- Fresher resumes
- Senior profiles

## Modules Tested

The following Zecpath AI modules were considered in ATS testing:

- Resume Text Extraction Engine
- Resume Section Classifier
- Skill Extraction Engine
- Experience Parsing Engine
- Education & Certification Parser
- Job Description Parser
- Semantic Matching Engine
- ATS Scoring Engine
- Candidate Ranking & Shortlisting Engine
- Fairness & Bias Reduction Module

## Test Dataset

| Test Case | Candidate Type | Job Role | Expected Result | AI Result | Status |
|---|---|---|---|---|---|
| TC001 | Fresher | Data Scientist | Review | Review | Matched |
| TC002 | Senior | Backend Developer | Shortlisted | Shortlisted | Matched |
| TC003 | Fresher | Marketing Executive | Review | Rejected | Mismatch |
| TC004 | Senior | Logistics Analyst | Shortlisted | Shortlisted | Matched |
| TC005 | Non-tech | HR Executive | Review | Review | Matched |

## Manual Review vs AI Output

Manual review was used as the reference decision. The AI output was compared against the expected manual decision.

Decision categories used:

- Shortlisted
- Review
- Rejected

## Mismatch Cases

### TC003 - Fresher Marketing Executive

Expected manual decision:

```text
Review

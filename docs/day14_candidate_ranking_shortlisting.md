# Day 14 - Candidate Ranking & Shortlisting

## Objective

The objective of Day 14 is to automate ranking, filtering, and shortlisting of candidates based on their final ATS scores.

## Module

```text
ats_engine/candidate_ranker.py


Key Features
1. Candidate Ranking
Candidates are sorted in descending order based on final ATS score.

Highest scoring candidate receives rank 1.

2. Shortlisting Thresholds
The system uses three decision zones:

75 and above → Shortlisted
50 to 74 → Review
Below 50 → Rejected
3. Auto-Reject and Review Zones
Candidates below the review threshold are automatically marked as rejected.

Candidates between 50 and 74 are placed in the recruiter review zone.

4. Top Candidate List
The system can generate a top candidate list for recruiters.

Example:

Top 5 candidates
Top 10 candidates
5. Recruiter-Friendly Output
The output includes:

candidate_id
candidate_name
job_id
final_ats_score
fit_category
rank
status
# Day 19 - ATS Architecture Diagrams

## 1. ATS System Architecture

```text
[Candidate Resume]
        ↓
[Resume Text Extraction Engine]
        ↓
[Resume Section Classifier]
        ↓
[Skill Extraction Engine]
        ↓
[Experience Parser]
        ↓
[Education & Certification Parser]
        ↓
[Structured Candidate Profile]
        ↓
[Job Description Parser]
        ↓
[Structured Job Profile]
        ↓
[Semantic Matching Engine]
        ↓
[ATS Score Generator]
        ↓
[Fairness & Bias Reduction]
        ↓
[Candidate Ranking Engine]
        ↓
[Shortlisted / Review / Rejected]


2. ATS Data Storage Flow
data/resumes/
        ↓
data/extracted_resumes/
        ↓
data/labeled_resumes/
        ↓
data/skill_outputs/
        ↓
data/experience_outputs/
        ↓
data/academic_outputs/
        ↓
data/matching_outputs/
        ↓
data/ats_score_outputs/
        ↓
data/ranking_outputs/
        ↓
data/fairness_outputs/


3. Backend Integration Flow
[Frontend]
        ↓
[Backend API]
        ↓
[ATS AI API]
        ↓
[Resume Parsing]
        ↓
[Scoring]
        ↓
[Ranking]
        ↓
[Backend Database]
        ↓
[Recruiter Dashboard]
4. Testing Flow
[Code Module]
        ↓
[Test Script]
        ↓
[pytest]
        ↓
[Test Result]
        ↓
[Fix Issues if Failed]
        ↓
[Commit to GitHub]

# Day 13 - ATS Scoring Formula Design

## Objective

The objective of Day 13 is to design a transparent and explainable candidate scoring framework.

## Module

```text
ats_engine/ats_score_generator.py

Final Score Formula
Final ATS Score =
(Skill Match × Skill Weight) +
(Experience Relevance × Experience Weight) +
(Education Alignment × Education Weight) +
(Semantic Similarity × Semantic Weight)

Example
Skill Match = 85
Experience Relevance = 78
Education Alignment = 90
Semantic Similarity = 82
For Data Scientist:

Final ATS Score =
85 × 0.35 +
78 × 0.25 +
90 × 0.20 +
82 × 0.20

Final ATS Score = 83.65
Fit Categories
80 - 100 → Strong Fit
60 - 79 → Good Fit
40 - 59 → Average Fit
Below 40 → Low Fit
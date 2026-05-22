# Day 15 - Fairness, Normalization & Bias Reduction

## Objective

The objective of Day 15 is to improve fairness, reduce bias, and standardize resume evaluation in the Zecpath AI hiring system.

## Module

```text
utils/fairness_normalizer.py



Key Features
1. Resume Normalization
The system converts resume text into a standard format.

It performs:

Lowercase conversion
Extra space removal
Symbol cleanup
Standard text formatting
2. Sensitive Attribute Masking
The system masks non-essential personal attributes.

Masked fields include:

Email
Phone number
Gender
Age
Marital status
Example:

Email: afnan@example.com
becomes:

Email: [MASKED_EMAIL]
3. Score Normalization
All scores are normalized between 0 and 100.

Rules:

Missing score → 0
Negative score → 0
Score above 100 → 100
Valid score → unchanged
4. Balanced Scoring
Balanced scoring prevents one score from dominating the entire evaluation.

It uses weights for:

Skill match
Experience relevance
Education alignment
Semantic similarity
5. Bias Indicator Detection
The system detects possible bias-related terms.

Examples:

Gender
Age
Religion
Marital status
Caste
Photo
Native place
These indicators are flagged for review.
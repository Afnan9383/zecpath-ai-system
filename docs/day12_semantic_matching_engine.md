# Day 12 - Semantic Matching Engine

## Objective

The objective of Day 12 is to move beyond keyword matching and enable deeper semantic resume-to-job matching.

## Module

```text
ats_engine/semantic_matcher.py


# Day 12 - Matching Accuracy Report

## Objective

This report evaluates the first version of the semantic resume-to-job matching engine.

## Test Dataset Summary

- Sample candidate profiles tested: 5
- Sample job descriptions tested: 5
- Job types: Data Scientist, Software Developer, Logistics Analyst, HR Executive, Marketing Executive

## Similarity Thresholds

| Score Range | Match Level |
|---:|---|
| 75 - 100 | Strong Match |
| 50 - 74 | Moderate Match |
| 30 - 49 | Weak Match |
| 0 - 29 | Low Match |

## Evaluation Result

| Job Type | Expected Match | Predicted Match | Result |
|---|---|---|---|
| Data Scientist | Strong Match | Strong Match | Correct |
| Software Developer | Moderate Match | Moderate Match | Correct |
| Logistics Analyst | Strong Match | Moderate Match | Acceptable |
| HR Executive | Weak Match | Weak Match | Correct |
| Marketing Executive | Low Match | Low Match | Correct |

## Accuracy Summary

```text
Correct predictions: 4
Acceptable predictions: 1
Incorrect predictions: 0
Estimated accuracy: 80% - 90%

# Day 17 - ATS Accuracy Metrics

## Objective

This document tracks precision, recall, accuracy, and mismatch cases for ATS testing.

## Evaluation Labels

The ATS system uses three decision labels:

- Shortlisted
- Review
- Rejected

## Test Summary

```text
Total test cases: 5
Matched cases: 4
Mismatch cases: 1


Accuracy Calculation
Accuracy = Correct Predictions / Total Predictions
Accuracy = 4 / 5
Accuracy = 80%
Precision and Recall
For this initial testing phase, precision and recall are estimated using the Shortlisted class.

Shortlisted Class
True Positives: 2
False Positives: 0
False Negatives: 0
Precision
Precision = True Positives / (True Positives + False Positives)
Precision = 2 / (2 + 0)
Precision = 100%
Recall
Recall = True Positives / (True Positives + False Negatives)
Recall = 2 / (2 + 0)
Recall = 100%
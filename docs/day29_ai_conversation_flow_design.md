# Day 29 - AI Conversation Flow Design

## Objective

The objective of Day 29 is to define how AI interacts dynamically with candidates during screening calls.

## Key Features

- AI call decision tree
- Conversation state machine
- Silence handling
- Confusion handling
- Repeated answer handling
- Fallback questions
- Follow-up triggers
- Polite retry logic
- Error-handling flow

## Conversation States

| State | Description |
|---|---|
| START | Conversation starts |
| ASK_QUESTION | AI asks the current question |
| WAIT_FOR_ANSWER | AI waits for candidate response |
| PROCESS_ANSWER | Candidate answer is analyzed |
| FOLLOW_UP | AI asks follow-up or clarification |
| RETRY | AI retries due to silence or unclear response |
| SKIP | AI skips after retry limit |
| END | Conversation ends |

## AI Decision Tree

Candidate Answer  
↓  
Is answer silent?  
↓ Yes → Retry silence prompt  
↓ No  
Is answer repeated?  
↓ Yes → Ask for new information  
↓ No  
Is answer vague?  
↓ Yes → Ask for more detail  
↓ No  
Is intent unknown?  
↓ Yes → Ask simpler question  
↓ No  
Is follow-up needed?  
↓ Yes → Ask follow-up question  
↓ No  
Move to next question  

## Fallback Questions

| Case | AI Prompt |
|---|---|
| Silence | I could not hear your response. Could you please answer again? |
| Confusion | No problem. Let me ask that in a simpler way. |
| Vague answer | Could you please provide a little more detail? |
| Repeated answer | You already mentioned that. Can you add any new information? |
| General | Could you please clarify your answer? |

## Follow-up Questions

| Intent | Follow-up |
|---|---|
| experience_info | Can you briefly explain your most relevant work experience? |
| skills_info | Can you give an example of how you used these skills? |
| availability_info | Can you confirm your exact joining availability? |
| salary_info | Is your salary expectation negotiable? |
| self_introduction | Can you summarize your current career goal? |

## Error Handling

- Silence is retried politely
- Maximum retry count is limited
- Repeated answers trigger clarification
- Vague answers trigger more detail request
- Unknown intent triggers simplified question
- After repeated failure, AI skips to next question

## Output Example

```json
{
  "question_id": "Q001",
  "candidate_answer": "",
  "detected_intent": "unknown",
  "action": "retry_silence",
  "ai_prompt": "I could not hear your response. Could you please answer again?"
}
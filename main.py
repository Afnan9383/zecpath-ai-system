from parsers.resume_parser import parse_resume
from ats_engine.ats_scorer import calculate_ats_score
from scoring.decision_engine import final_decision
from utils.logger import get_logger

logger = get_logger()

resume_text = "Python developer with FastAPI and Machine Learning experience"

candidate = parse_resume(resume_text)

required_skills = ["Python", "FastAPI", "SQL", "Machine Learning"]

ats_result = calculate_ats_score(candidate["skills"], required_skills)

decision = final_decision(
    ats_score=ats_result["ats_score"],
    screening_score=80,
    interview_score=85
)

logger.info("Candidate evaluation completed")

print(candidate)
print(ats_result)
print(decision)

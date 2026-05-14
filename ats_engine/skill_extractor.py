import json
import re
from pathlib import Path


SKILL_DB = {
    "python": {
        "variants": ["python", "py"],
        "category": "Programming"
    },
    "javascript": {
        "variants": ["javascript", "js"],
        "category": "Programming"
    },
    "react": {
        "variants": ["react", "reactjs"],
        "category": "Frontend"
    },
    "node": {
        "variants": ["node", "nodejs"],
        "category": "Backend"
    },
    "django": {
        "variants": ["django"],
        "category": "Backend"
    },
    "sql": {
        "variants": ["sql", "mysql", "postgresql"],
        "category": "Database"
    },
    "mongodb": {
        "variants": ["mongodb", "mongo db"],
        "category": "Database"
    },
    "express": {
        "variants": ["express", "expressjs"],
        "category": "Backend"
    },
    "angular": {
        "variants": ["angular", "angularjs"],
        "category": "Frontend"
    },
    "excel": {
        "variants": ["excel", "ms excel", "microsoft excel"],
        "category": "Business"
    },
    "machine learning": {
        "variants": ["machine learning", "ml"],
        "category": "AI"
    },
    "data science": {
        "variants": ["data science"],
        "category": "AI"
    },
    "communication": {
        "variants": ["communication", "communication skills"],
        "category": "Soft Skill"
    },
    "leadership": {
        "variants": ["leadership", "team leadership"],
        "category": "Soft Skill"
    }
}


SKILL_STACKS = {
    "mern": ["mongodb", "express", "react", "node"],
    "mean": ["mongodb", "express", "angular", "node"]
}


def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s\.\,\-\+]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def contains_skill_variant(text: str, variant: str) -> bool:
    pattern = rf"(?<![a-z0-9]){re.escape(variant)}(?![a-z0-9])"
    return re.search(pattern, text) is not None


def calculate_confidence(skill: str, text: str, source: str = "resume") -> float:
    cleaned_text = clean_text(text)
    occurrences = cleaned_text.count(skill)

    if source == "stack_detected":
        return 0.75

    if occurrences >= 3:
        return 0.95
    if occurrences == 2:
        return 0.85
    if occurrences == 1:
        return 0.75

    return 0.70


def extract_skills(text: str) -> list[str]:
    cleaned_text = clean_text(text)
    extracted_skills = []

    for skill, details in SKILL_DB.items():
        for variant in details["variants"]:
            if contains_skill_variant(cleaned_text, variant):
                extracted_skills.append(skill)
                break

    for stack, stack_skills in SKILL_STACKS.items():
        if contains_skill_variant(cleaned_text, stack):
            extracted_skills.extend(stack_skills)

    return sorted(set(extracted_skills))


def extract_skills_with_confidence(text: str, candidate_id: str = "C123") -> dict:
    cleaned_text = clean_text(text)
    skills = []
    seen = set()

    for skill, details in SKILL_DB.items():
        for variant in details["variants"]:
            if contains_skill_variant(cleaned_text, variant):
                confidence = calculate_confidence(skill, cleaned_text, source="resume")

                skills.append({
                    "skill_name": skill.title(),
                    "normalized_skill": skill,
                    "category": details["category"],
                    "confidence": round(confidence, 2),
                    "source": "resume"
                })

                seen.add(skill)
                break

    for stack, stack_skills in SKILL_STACKS.items():
        if contains_skill_variant(cleaned_text, stack):
            for skill in stack_skills:
                if skill not in seen:
                    details = SKILL_DB.get(skill, {"category": "Technical"})

                    skills.append({
                        "skill_name": skill.title(),
                        "normalized_skill": skill,
                        "category": details["category"],
                        "confidence": calculate_confidence(skill, cleaned_text, source="stack_detected"),
                        "source": "stack_detected"
                    })

                    seen.add(skill)

    return {
        "candidate_id": candidate_id,
        "skills": skills
    }


def save_structured_skill_output(
    resume_text: str,
    candidate_id: str = "C123",
    output_file: str = "data/skill_outputs/candidate_skills.json"
) -> str:
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)

    skill_output = extract_skills_with_confidence(resume_text, candidate_id)

    Path(output_file).write_text(
        json.dumps(skill_output, indent=2),
        encoding="utf-8"
    )

    return output_file

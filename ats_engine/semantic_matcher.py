import json
import re
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s\+\#\.]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def calculate_semantic_similarity(text_a: str, text_b: str) -> float:
    cleaned_a = clean_text(text_a)
    cleaned_b = clean_text(text_b)

    if not cleaned_a or not cleaned_b:
        return 0.0

    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        stop_words="english"
    )

    vectors = vectorizer.fit_transform([cleaned_a, cleaned_b])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    return round(float(similarity) * 100, 2)


def classify_match_score(score: float) -> str:
    if score >= 75:
        return "Strong Match"
    if score >= 50:
        return "Moderate Match"
    if score >= 30:
        return "Weak Match"

    return "Low Match"


def compare_resume_to_jd(resume_profile: dict, jd_profile: dict, candidate_id: str = "C123", job_id: str = "J456") -> dict:
    resume_skills = " ".join(resume_profile.get("skills", []))
    jd_skills = " ".join(jd_profile.get("required_skills", []))

    resume_experience = resume_profile.get("experience_summary", "")
    jd_description = jd_profile.get("job_description", "")

    resume_projects = resume_profile.get("projects", "")
    jd_responsibilities = " ".join(jd_profile.get("responsibilities", []))

    skill_similarity = calculate_semantic_similarity(resume_skills, jd_skills)
    experience_similarity = calculate_semantic_similarity(resume_experience, jd_description)
    project_similarity = calculate_semantic_similarity(resume_projects, jd_responsibilities)

    overall_score = round(
        (skill_similarity * 0.45)
        + (experience_similarity * 0.35)
        + (project_similarity * 0.20),
        2
    )

    return {
        "candidate_id": candidate_id,
        "job_id": job_id,
        "semantic_scores": {
            "skill_similarity": skill_similarity,
            "experience_similarity": experience_similarity,
            "project_similarity": project_similarity,
            "overall_similarity": overall_score
        },
        "match_level": classify_match_score(overall_score)
    }


def save_similarity_output(
    resume_profile: dict,
    jd_profile: dict,
    candidate_id: str = "C123",
    job_id: str = "J456",
    output_file: str = "data/matching_outputs/resume_jd_similarity.json"
) -> str:
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)

    result = compare_resume_to_jd(resume_profile, jd_profile, candidate_id, job_id)

    Path(output_file).write_text(
        json.dumps(result, indent=2),
        encoding="utf-8"
    )

    return output_file

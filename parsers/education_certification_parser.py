import json
import re
from pathlib import Path


DEGREE_NORMALIZATION = {
    "mca": "Master of Computer Applications",
    "master of computer applications": "Master of Computer Applications",
    "bsc": "Bachelor of Science",
    "b.sc": "Bachelor of Science",
    "b.tech": "Bachelor of Technology",
    "btech": "Bachelor of Technology",
    "mba": "Master of Business Administration",
    "ba": "Bachelor of Arts",
    "bcom": "Bachelor of Commerce",
    "b.com": "Bachelor of Commerce"
}


FIELD_KEYWORDS = {
    "computer applications": ["computer applications", "mca"],
    "computer science": ["computer science", "cs", "software"],
    "mathematics": ["mathematics", "maths"],
    "data science": ["data science", "analytics", "artificial intelligence", "ai"],
    "business administration": ["business administration", "management", "mba"],
    "commerce": ["commerce", "accounting", "finance"]
}


CERTIFICATION_CATEGORIES = {
    "AI/ML": ["ai", "ml", "machine learning", "artificial intelligence", "data science"],
    "Cybersecurity": ["cybersecurity", "cyber security", "ethical hacking", "network security"],
    "Cloud": ["aws", "azure", "google cloud", "gcp"],
    "Data Analytics": ["power bi", "tableau", "excel", "analytics"],
    "Programming": ["python", "java", "sql", "django"]
}


def normalize_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s\.\-/&]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_section(resume_text: str, section_names: list[str], stop_sections: list[str]) -> list[str]:
    lines = resume_text.splitlines()
    captured_lines = []
    capture = False

    section_names_lower = [section.lower() for section in section_names]
    stop_sections_lower = [section.lower() for section in stop_sections]

    for line in lines:
        clean_line = line.strip()
        lower_line = clean_line.lower()

        if not clean_line:
            continue

        if lower_line in section_names_lower:
            capture = True
            continue

        if lower_line in stop_sections_lower:
            capture = False

        if capture:
            captured_lines.append(clean_line)

    return captured_lines


def normalize_degree(line: str) -> str | None:
    normalized_line = normalize_text(line)

    for variation, standard_degree in DEGREE_NORMALIZATION.items():
        if variation in normalized_line:
            return standard_degree

    return None


def extract_field_of_study(line: str) -> str | None:
    normalized_line = normalize_text(line)

    for field, keywords in FIELD_KEYWORDS.items():
        for keyword in keywords:
            if keyword in normalized_line:
                return field.title()

    return None


def extract_graduation_year(line: str) -> int | None:
    years = re.findall(r"\b(19\d{2}|20\d{2})\b", line)

    if not years:
        return None

    return int(years[-1])


def extract_institution(line: str) -> str:
    separators = [",", " - ", " | "]

    for separator in separators:
        if separator in line:
            parts = [part.strip() for part in line.split(separator) if part.strip()]
            if len(parts) >= 2:
                return parts[-1]

    return "Unknown"


def extract_education(resume_text: str) -> list[dict]:
    education_lines = extract_section(
        resume_text,
        section_names=["Education", "Academic Background", "Qualifications"],
        stop_sections=["Skills", "Technical Skills", "Projects", "Certifications", "Experience", "Personal Details"]
    )

    education_records = []

    for line in education_lines:
        degree = normalize_degree(line)

        if not degree:
            continue

        education_records.append({
            "degree": degree,
            "field_of_study": extract_field_of_study(line),
            "institution": extract_institution(line),
            "graduation_year": extract_graduation_year(line),
            "raw_text": line
        })

    return education_records


def categorize_certification(certification_text: str) -> str:
    normalized_certification = normalize_text(certification_text)

    for category, keywords in CERTIFICATION_CATEGORIES.items():
        for keyword in keywords:
            if keyword in normalized_certification:
                return category

    return "General"


def extract_certifications(resume_text: str) -> list[dict]:
    certification_lines = extract_section(
        resume_text,
        section_names=["Certifications", "Certificates", "Courses", "Training"],
        stop_sections=["Skills", "Projects", "Experience", "Education", "Personal Details"]
    )

    certifications = []

    for line in certification_lines:
        certifications.append({
            "certification_name": line,
            "category": categorize_certification(line),
            "raw_text": line
        })

    return certifications


def calculate_education_relevance(education_records: list[dict], target_role: str) -> float:
    target_role_lower = target_role.lower()
    score = 0

    for record in education_records:
        field = (record.get("field_of_study") or "").lower()
        degree = (record.get("degree") or "").lower()

        if "data scientist" in target_role_lower:
            if "computer" in field or "data science" in field or "mathematics" in field:
                score += 1
            if "master" in degree:
                score += 0.5

        elif "software developer" in target_role_lower:
            if "computer" in field:
                score += 1

        elif "business" in target_role_lower:
            if "business" in field or "commerce" in field:
                score += 1

    if not education_records:
        return 0.0

    max_score = len(education_records) * 1.5

    return round((score / max_score) * 100, 2)


def parse_academic_profile(
    resume_text: str,
    candidate_id: str = "C123",
    target_role: str = "Data Scientist"
) -> dict:
    education_records = extract_education(resume_text)
    certifications = extract_certifications(resume_text)
    relevance_score = calculate_education_relevance(education_records, target_role)

    return {
        "candidate_id": candidate_id,
        "target_role": target_role,
        "education": education_records,
        "certifications": certifications,
        "education_relevance_score": relevance_score
    }


def save_academic_profile(
    resume_text: str,
    candidate_id: str = "C123",
    target_role: str = "Data Scientist",
    output_file: str = "data/academic_outputs/candidate_academic_profile.json"
) -> str:
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)

    academic_profile = parse_academic_profile(resume_text, candidate_id, target_role)

    Path(output_file).write_text(
        json.dumps(academic_profile, indent=2),
        encoding="utf-8"
    )

    return output_file

import json
import re
from pathlib import Path
from datetime import datetime


ROLE_KEYWORDS = {
    "data scientist": ["data scientist", "machine learning", "ai", "data science", "python"],
    "software developer": ["software developer", "developer", "backend", "frontend", "api"],
    "logistics analyst": ["logistics", "supply chain", "warehouse", "dispatch", "inventory"],
    "hr executive": ["hr", "human resources", "recruitment", "employee"],
    "marketing executive": ["marketing", "seo", "campaign", "branding", "sales"]
}


def extract_experience_lines(resume_text: str) -> list[str]:
    lines = resume_text.splitlines()
    experience_lines = []

    capture = False

    for line in lines:
        cleaned_line = line.strip()

        if not cleaned_line:
            continue

        lower_line = cleaned_line.lower()

        if lower_line in ["experience", "work experience", "professional experience", "internships"]:
            capture = True
            continue

        if lower_line in ["education", "skills", "projects", "certifications", "personal details"]:
            capture = False

        if capture:
            experience_lines.append(cleaned_line)

    return experience_lines


def extract_job_titles(text: str) -> list[str]:
    known_titles = [
        "data scientist",
        "software developer",
        "python developer",
        "machine learning engineer",
        "logistics analyst",
        "hr executive",
        "marketing executive",
        "intern"
    ]

    found_titles = []

    text_lower = text.lower()

    for title in known_titles:
        if title in text_lower:
            found_titles.append(title.title())

    return sorted(set(found_titles))


def extract_company_names(text: str) -> list[str]:
    company_patterns = [
        r"at\s+([A-Z][A-Za-z0-9 &.-]+)",
        r"with\s+([A-Z][A-Za-z0-9 &.-]+)",
        r"([A-Z][A-Za-z0-9 &.-]+)\s+-\s+[A-Za-z ]+"
    ]

    companies = []

    for pattern in company_patterns:
        matches = re.findall(pattern, text)

        for match in matches:
            company = match.strip()
            if len(company) > 2:
                companies.append(company)

    return sorted(set(companies))


def extract_years(text: str) -> list[int]:
    years = re.findall(r"\b(20\d{2}|19\d{2})\b", text)
    return [int(year) for year in years]


def calculate_total_experience(years: list[int]) -> float:
    if len(years) < 2:
        return 0.0

    start_year = min(years)
    end_year = max(years)

    total_years = end_year - start_year

    return max(float(total_years), 0.0)


def detect_experience_gaps(years: list[int]) -> list[str]:
    gaps = []

    if len(years) < 2:
        return gaps

    sorted_years = sorted(set(years))

    for index in range(len(sorted_years) - 1):
        gap = sorted_years[index + 1] - sorted_years[index]

        if gap > 1:
            gaps.append(f"Gap detected between {sorted_years[index]} and {sorted_years[index + 1]}")

    return gaps


def calculate_role_relevance(candidate_text: str, target_role: str) -> float:
    target_role_lower = target_role.lower()
    candidate_text_lower = candidate_text.lower()

    keywords = ROLE_KEYWORDS.get(target_role_lower, target_role_lower.split())

    matched_keywords = 0

    for keyword in keywords:
        if keyword in candidate_text_lower:
            matched_keywords += 1

    if not keywords:
        return 0.0

    relevance_score = matched_keywords / len(keywords)

    return round(relevance_score * 100, 2)


def parse_experience(resume_text: str, candidate_id: str = "C123", target_role: str = "Data Scientist") -> dict:
    experience_lines = extract_experience_lines(resume_text)
    experience_text = " ".join(experience_lines)

    job_titles = extract_job_titles(experience_text)
    company_names = extract_company_names(experience_text)
    years = extract_years(experience_text)

    total_experience = calculate_total_experience(years)
    gaps = detect_experience_gaps(years)
    relevance_score = calculate_role_relevance(experience_text, target_role)

    return {
        "candidate_id": candidate_id,
        "target_role": target_role,
        "experience_summary": {
            "job_titles": job_titles,
            "company_names": company_names,
            "employment_years_found": years,
            "total_experience_years": total_experience,
            "experience_gaps": gaps,
            "role_relevance_score": relevance_score
        },
        "experience_text": experience_lines
    }


def save_experience_output(
    resume_text: str,
    candidate_id: str = "C123",
    target_role: str = "Data Scientist",
    output_file: str = "data/experience_outputs/candidate_experience.json"
) -> str:
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)

    experience_output = parse_experience(resume_text, candidate_id, target_role)

    Path(output_file).write_text(
        json.dumps(experience_output, indent=2),
        encoding="utf-8"
    )

    return output_file

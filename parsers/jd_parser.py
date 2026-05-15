import json
import re
from pathlib import Path
from typing import Any

from utils.logger import get_logger

logger = get_logger()


SKILL_SYNONYMS = {
    "ai": "artificial intelligence",
    "artificial intelligence": "artificial intelligence",
    "ml": "machine learning",
    "machine learning": "machine learning",
    "data science": "data science",
    "python": "python",
    "sql": "sql",
    "excel": "excel",
    "power bi": "power bi",
    "logistics": "logistics",
    "supply chain": "supply chain",
    "inventory": "inventory management",
    "inventory management": "inventory management",
    "warehouse": "warehouse management",
    "warehouse management": "warehouse management",
    "dispatch": "dispatch planning",
    "dispatch planning": "dispatch planning",
    "route optimization": "route optimization",
    "customs": "customs compliance",
    "customs compliance": "customs compliance",
    "documentation": "documentation",
    "compliance": "compliance",
    "coordination": "coordination",
    "supervision": "supervision",
    "problem-solving": "problem solving",
    "problem solving": "problem solving",
}


ROLE_VARIATIONS = {
    "analyst": "Analyst",
    "coordinator": "Coordinator",
    "manager": "Manager",
    "specialist": "Specialist",
    "planner": "Planner",
    "supervisor": "Supervisor",
    "executive": "Executive",
}


def normalize_jd_text(raw_text: str) -> str:
    text = raw_text.replace("\r", "\n")

    replacements = {
        "\u00e2\u20ac\u00a2": "-",
        "\u00e2\u20ac\u201c": "-",
        "\u00e2\u20ac\u201d": "-",
        "\u00e2\u201a\u00b9": "INR ",
        "\u2022": "-",
        "\u2013": "-",
        "\u20b9": "INR ",
        "\t": " ",
    }

    for old_value, new_value in replacements.items():
        text = text.replace(old_value, new_value)

    text = re.sub(r"[\u2022\u25cf\u25aa\u25a0]", "-", text)
    text = re.sub(r" +", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[^\S\n]+", " ", text)

    return text.strip()


def extract_role_name(cleaned_text: str, fallback_name: str = "") -> str:
    first_line = cleaned_text.splitlines()[0].strip() if cleaned_text.strip() else fallback_name
    first_line = re.sub(r"^\d+\.\s*", "", first_line)

    return first_line or fallback_name


def extract_role_family(role_name: str) -> str:
    role_name_lower = role_name.lower()

    for keyword, normalized_role in ROLE_VARIATIONS.items():
        if keyword in role_name_lower:
            return normalized_role

    return "Other"


def extract_experience_requirement(cleaned_text: str) -> dict[str, Any]:
    match = re.search(
        r"(?i)experience\s*:\s*(\d+)\s*[-\u2013]?\s*(\d+)?\s*years?",
        cleaned_text,
    )

    if not match:
        return {
            "minimum_years": None,
            "maximum_years": None,
            "raw_text": "",
        }

    minimum_years = int(match.group(1))
    maximum_years = int(match.group(2)) if match.group(2) else minimum_years

    return {
        "minimum_years": minimum_years,
        "maximum_years": maximum_years,
        "raw_text": match.group(0),
    }


def extract_salary_range(cleaned_text: str) -> dict[str, Any]:
    match = re.search(
        r"(?i)salary\s*\(india\)\s*:\s*(?:INR\s*)?([\d.]+)\s*LPA\s*[-\u2013]\s*(?:INR\s*)?([\d.]+)\s*LPA",
        cleaned_text,
    )

    if not match:
        return {
            "minimum_lpa": None,
            "maximum_lpa": None,
            "currency": "INR",
            "raw_text": "",
        }

    return {
        "minimum_lpa": float(match.group(1)),
        "maximum_lpa": float(match.group(2)),
        "currency": "INR",
        "raw_text": match.group(0),
    }


def extract_section(cleaned_text: str, start_heading: str, end_headings: list[str]) -> str:
    if not end_headings:
        pattern = rf"(?is){re.escape(start_heading)}\s*:?\s*(.*)\Z"
        match = re.search(pattern, cleaned_text)
        return match.group(1).strip() if match else ""

    end_pattern = "|".join(re.escape(heading) for heading in end_headings)
    pattern = rf"(?is){re.escape(start_heading)}\s*:?\s*(.*?)(?:\n(?:{end_pattern})\s*:?\s*|\Z)"

    match = re.search(pattern, cleaned_text)

    return match.group(1).strip() if match else ""


def extract_bullet_items(section_text: str, split_commas: bool = False) -> list[str]:
    items = []

    for line in section_text.splitlines():
        line = line.strip()
        line = re.sub(r"^-+\s*", "", line)

        if not line:
            continue

        if split_commas and "," in line:
            items.extend(part.strip() for part in line.split(",") if part.strip())
        else:
            items.append(line)

    return items


def normalize_skill(skill_text: str) -> dict[str, Any]:
    skill_text = re.sub(r"^(and|or)\s+", "", skill_text.strip(), flags=re.IGNORECASE)
    skill_lower = skill_text.lower().strip(" .")

    normalized_name = skill_lower
    matched_synonyms = []

    for synonym, canonical_name in sorted(SKILL_SYNONYMS.items(), key=lambda item: len(item[0]), reverse=True):
        synonym_pattern = rf"(?<![a-z0-9]){re.escape(synonym)}(?![a-z0-9])"

        if re.search(synonym_pattern, skill_lower):
            normalized_name = canonical_name
            matched_synonyms.append(synonym)
            break

    return {
        "skill_name": skill_text.strip(" ."),
        "normalized_name": normalized_name,
        "importance": "mandatory",
        "matched_synonyms": matched_synonyms,
    }


def extract_required_skills(cleaned_text: str) -> list[dict[str, Any]]:
    skills_section = extract_section(cleaned_text, "Skills Required", [])
    skill_items = extract_bullet_items(skills_section, split_commas=True)

    seen = set()
    skills = []

    for item in skill_items:
        expanded_items = [part.strip() for part in re.split(r",|\s+and\s+", item) if part.strip()]

        for expanded_item in expanded_items:
            skill = normalize_skill(expanded_item)
            key = skill["normalized_name"]

            if key not in seen:
                seen.add(key)
                skills.append(skill)

    return skills


def extract_responsibilities(cleaned_text: str) -> list[str]:
    section = extract_section(cleaned_text, "Key Responsibilities", ["Skills Required"])

    return extract_bullet_items(section)


def extract_job_description(cleaned_text: str) -> str:
    return extract_section(cleaned_text, "Job Description", ["Key Responsibilities", "Skills Required"])


def extract_education_preferences(cleaned_text: str) -> list[str]:
    education_section = extract_section(cleaned_text, "Education", ["Skills Required", "Key Responsibilities"])
    qualification_section = extract_section(cleaned_text, "Qualification", ["Skills Required", "Key Responsibilities"])
    qualifications_section = extract_section(cleaned_text, "Qualifications", ["Skills Required", "Key Responsibilities"])

    combined = "\n".join(
        section for section in [education_section, qualification_section, qualifications_section] if section
    )

    return extract_bullet_items(combined)


def parse_job_description_text(raw_text: str, source_file: str = "") -> dict[str, Any]:
    cleaned_text = normalize_jd_text(raw_text)

    source_path = Path(source_file)
    role_name = extract_role_name(cleaned_text, source_path.stem)

    required_skills = extract_required_skills(cleaned_text)
    experience_required = extract_experience_requirement(cleaned_text)

    return {
        "job_id": source_path.stem.lower().replace(" ", "_") if source_file else "",
        "source_file": source_path.name if source_file else "",
        "role_name": role_name,
        "role_family": extract_role_family(role_name),
        "experience_required": experience_required,
        "salary_range": extract_salary_range(cleaned_text),
        "job_description": extract_job_description(cleaned_text),
        "responsibilities": extract_responsibilities(cleaned_text),
        "required_skills": required_skills,
        "education_preferences": extract_education_preferences(cleaned_text),
        "ai_profile": {
            "normalized_role": role_name.lower(),
            "skill_keywords": [
                skill["normalized_name"] for skill in required_skills
            ],
            "experience_minimum_years": experience_required["minimum_years"],
        },
    }


def parse_job_description_file(file_path: str) -> dict[str, Any]:
    path = Path(file_path)

    raw_text = path.read_text(encoding="utf-8", errors="ignore")
    parsed_jd = parse_job_description_text(raw_text, str(path))

    logger.info(f"Job description parsed successfully: {path}")

    return parsed_jd


def save_structured_jd(input_file: str, output_folder: str = "data/structured_jds") -> str:
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    parsed_jd = parse_job_description_file(input_file)
    output_path = Path(output_folder) / f"{Path(input_file).stem}.json"

    output_path.write_text(
        json.dumps(parsed_jd, indent=2),
        encoding="utf-8",
    )

    logger.info(f"Structured JD saved: {output_path}")

    return str(output_path)


def save_all_structured_jds(input_folder: str = "data/JD", output_folder: str = "data/structured_jds") -> list[str]:
    input_path = Path(input_folder)
    output_paths = []

    for jd_file in sorted(input_path.glob("*.txt")):
        output_paths.append(save_structured_jd(str(jd_file), output_folder))

    logger.info(f"Total structured JDs saved: {len(output_paths)}")

    return output_paths

import json
import re
from pathlib import Path
from typing import Dict, List


SECTION_PATTERNS = {
    "profile": [
        "profile",
        "summary",
        "professional summary",
        "career objective",
        "objective"
    ],
    "skills": [
        "skills",
        "technical skills",
        "core skills",
        "key skills",
        "tools and technologies",
        "programming languages"
    ],
    "work_experience": [
        "experience",
        "work experience",
        "professional experience",
        "employment history",
        "internships"
    ],
    "education": [
        "education",
        "academic background",
        "qualification",
        "qualifications"
    ],
    "certifications": [
        "certifications",
        "certificates",
        "courses",
        "training"
    ],
    "projects": [
        "projects",
        "academic projects",
        "personal projects",
        "main project",
        "mini project"
    ],
    "achievements": [
        "achievements",
        "awards",
        "honors"
    ],
    "personal_details": [
        "personal details",
        "languages",
        "references"
    ]
}


KEYWORD_HINTS = {
    "skills": [
        "python", "java", "sql", "machine learning", "django",
        "power bi", "tableau", "tensorflow", "html", "css"
    ],
    "education": [
        "bachelor", "master", "degree", "university", "college",
        "mca", "bsc", "b.tech", "graduation"
    ],
    "work_experience": [
        "intern", "worked", "company", "responsible", "experience",
        "developed", "managed"
    ],
    "projects": [
        "project", "developed", "designed", "implemented", "technologies used"
    ],
    "certifications": [
        "certificate", "certification", "bootcamp", "training", "course"
    ]
}


def normalize_line(line: str) -> str:
    line = line.strip()
    line = re.sub(r"\s+", " ", line)
    return line


def detect_heading(line: str) -> str | None:
    cleaned_line = normalize_line(line).lower().strip(":")
    cleaned_line = re.sub(r"[^a-z0-9 &/.-]", "", cleaned_line)

    for section_name, patterns in SECTION_PATTERNS.items():
        for pattern in patterns:
            if cleaned_line == pattern:
                return section_name

    return None


def detect_section_by_keywords(text_block: str) -> str:
    block_lower = text_block.lower()

    scores = {}

    for section_name, keywords in KEYWORD_HINTS.items():
        score = 0

        for keyword in keywords:
            if keyword in block_lower:
                score += 1

        scores[section_name] = score

    best_section = max(scores, key=scores.get)

    if scores[best_section] == 0:
        return "unknown"

    return best_section


def classify_resume_sections(resume_text: str) -> Dict[str, List[str]]:
    sections = {
        "profile": [],
        "skills": [],
        "work_experience": [],
        "education": [],
        "certifications": [],
        "projects": [],
        "achievements": [],
        "personal_details": [],
        "unknown": []
    }

    current_section = "unknown"

    lines = resume_text.splitlines()

    for line in lines:
        cleaned_line = normalize_line(line)

        if not cleaned_line:
            continue

        detected_heading = detect_heading(cleaned_line)

        if detected_heading:
            current_section = detected_heading
            continue

        sections[current_section].append(cleaned_line)

    for section_name, content_lines in list(sections.items()):
        if section_name != "unknown":
            continue

        reclassified_lines = []

        for line in content_lines:
            predicted_section = detect_section_by_keywords(line)

            if predicted_section != "unknown":
                sections[predicted_section].append(line)
            else:
                reclassified_lines.append(line)

        sections["unknown"] = reclassified_lines

    return sections


def save_labeled_resume_sample(
    input_file: str,
    output_folder: str = "data/labeled_resumes"
) -> str:
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    input_path = Path(input_file)
    resume_text = input_path.read_text(encoding="utf-8", errors="ignore")

    labeled_sections = classify_resume_sections(resume_text)

    output_path = Path(output_folder) / f"{input_path.stem}_labeled.json"

    output_path.write_text(
        json.dumps(labeled_sections, indent=2),
        encoding="utf-8"
    )

    return str(output_path)

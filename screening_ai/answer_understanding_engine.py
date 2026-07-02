import re


INTENT_KEYWORDS = {
    "self_introduction": ["my name", "i am", "i'm", "myself"],
    "education_info": ["btech", "b.tech", "mca", "mba", "degree", "graduated", "qualification"],
    "experience_info": ["experience", "worked", "years", "internship", "developer", "engineer"],
    "skills_info": ["python", "django", "java", "sql", "react", "machine learning", "data science"],
    "availability_info": ["immediate", "join", "notice period", "available", "month", "days"],
    "salary_info": ["salary", "ctc", "package", "expected", "lpa"],
    "location_info": ["located", "from", "living", "relocate", "remote", "onsite"]
}


SKILL_KEYWORDS = [
    "python",
    "django",
    "java",
    "sql",
    "react",
    "node",
    "machine learning",
    "data science",
    "excel",
    "communication"
]


OFF_TOPIC_KEYWORDS = [
    "weather",
    "movie",
    "food",
    "politics",
    "sports",
    "music"
]


VAGUE_KEYWORDS = [
    "maybe",
    "not sure",
    "i think",
    "some",
    "little",
    "few",
    "kind of"
]


def normalize_answer(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s\.]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def classify_intent(answer_text):
    normalized = normalize_answer(answer_text)
    matched_intents = {}

    for intent, keywords in INTENT_KEYWORDS.items():
        score = 0

        for keyword in keywords:
            if keyword in normalized:
                score += 1

        if score > 0:
            matched_intents[intent] = score

    if not matched_intents:
        return "unknown"

    return max(matched_intents, key=matched_intents.get)


def extract_skills(answer_text):
    normalized = normalize_answer(answer_text)
    skills = []

    for skill in SKILL_KEYWORDS:
        if skill in normalized:
            skills.append(skill)

    return list(set(skills))


def extract_experience_years(answer_text):
    normalized = normalize_answer(answer_text)

    digit_match = re.search(r"(\d+)\s*(year|years|yrs)", normalized)
    if digit_match:
        return int(digit_match.group(1))

    word_number_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10
    }

    for word, number in word_number_map.items():
        if f"{word} year" in normalized or f"{word} years" in normalized:
            return number

    return None


def extract_availability(answer_text):
    normalized = normalize_answer(answer_text)

    if "immediate" in normalized:
        return "Immediate"

    notice_match = re.search(r"(\d+)\s*(day|days|month|months)", normalized)
    if notice_match:
        return f"{notice_match.group(1)} {notice_match.group(2)}"

    if "next month" in normalized:
        return "Next month"

    return None


def extract_salary_expectation(answer_text):
    normalized = normalize_answer(answer_text)

    salary_match = re.search(r"(\d+)\s*(lpa|lakhs|lakh)", normalized)
    if salary_match:
        return f"{salary_match.group(1)} {salary_match.group(2)}"

    return None


def detect_off_topic(answer_text):
    normalized = normalize_answer(answer_text)

    for keyword in OFF_TOPIC_KEYWORDS:
        if keyword in normalized:
            return True

    return False


def detect_vague_answer(answer_text):
    normalized = normalize_answer(answer_text)

    if len(normalized.split()) < 3:
        return True

    for keyword in VAGUE_KEYWORDS:
        if keyword in normalized:
            return True

    return False


def understand_answer(question_id, answer_text):
    normalized = normalize_answer(answer_text)
    intent = classify_intent(answer_text)

    flags = []

    if detect_off_topic(answer_text):
        flags.append("off_topic_response")

    if detect_vague_answer(answer_text):
        flags.append("vague_or_missing_answer")

    structured_answer = {
        "question_id": question_id,
        "original_answer": answer_text,
        "normalized_answer": normalized,
        "intent": intent,
        "skills": extract_skills(answer_text),
        "experience_years": extract_experience_years(answer_text),
        "availability": extract_availability(answer_text),
        "salary_expectation": extract_salary_expectation(answer_text),
        "is_off_topic": detect_off_topic(answer_text),
        "is_vague": detect_vague_answer(answer_text),
        "flags": flags
    }

    return structured_answer
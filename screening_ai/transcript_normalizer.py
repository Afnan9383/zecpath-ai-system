import re


FILLER_WORDS = [
    "um",
    "uh",
    "umm",
    "ah",
    "like",
    "you know",
    "actually",
    "basically"
]


def normalize_case(text):
    return text.lower().strip()


def remove_filler_words(text):
    cleaned_text = text

    for filler in FILLER_WORDS:
        cleaned_text = re.sub(
            rf"\b{re.escape(filler)}\b",
            "",
            cleaned_text,
            flags=re.IGNORECASE
        )

    return cleaned_text


def normalize_spaces(text):
    return re.sub(r"\s+", " ", text).strip()


def correct_basic_punctuation(text):
    text = normalize_spaces(text)

    if text and text[-1] not in [".", "?", "!"]:
        text += "."

    return text


def detect_silence(text):
    return len(text.strip()) == 0


def detect_partial_answer(text):
    partial_markers = ["i think", "maybe", "not sure", "i don't know", "dont know"]

    text_lower = text.lower()

    return any(marker in text_lower for marker in partial_markers)


def clean_transcript_text(text):
    if detect_silence(text):
        return {
            "cleaned_text": "",
            "status": "silence_detected",
            "flags": ["No speech detected"]
        }

    cleaned = normalize_case(text)
    cleaned = remove_filler_words(cleaned)
    cleaned = normalize_spaces(cleaned)
    cleaned = correct_basic_punctuation(cleaned)

    flags = []

    if detect_partial_answer(cleaned):
        flags.append("Partial or uncertain answer detected")

    return {
        "cleaned_text": cleaned,
        "status": "processed",
        "flags": flags
    }
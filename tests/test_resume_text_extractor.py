from parsers.resume_text_extractor import clean_resume_text


def test_clean_resume_text_removes_extra_spaces():
    raw_text = "Skills\nPython     FastAPI\n\n\nExperience"
    cleaned_text = clean_resume_text(raw_text)

    assert "     " not in cleaned_text
    assert "SKILLS" in cleaned_text
    assert "EXPERIENCE" in cleaned_text


def test_clean_resume_text_normalizes_bullets():
    raw_text = "• Python\n● FastAPI\n▪ SQL"
    cleaned_text = clean_resume_text(raw_text)

    assert "- Python" in cleaned_text
    assert "- FastAPI" in cleaned_text
    assert "- SQL" in cleaned_text

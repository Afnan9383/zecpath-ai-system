from ats_engine.skill_extractor import extract_skills, extract_skills_with_confidence


def test_skill_extraction():
    text = "Python Django React MERN communication"

    skills = extract_skills(text)

    assert "python" in skills
    assert "django" in skills
    assert "react" in skills
    assert "communication" in skills


def test_skill_extraction_with_confidence():
    text = "Python developer with Python and Django experience"

    result = extract_skills_with_confidence(text)

    assert result["candidate_id"] == "C123"
    assert len(result["skills"]) > 0
    assert any(skill["normalized_skill"] == "python" for skill in result["skills"])


def test_stack_expansion():
    text = "Worked on MERN stack project"

    skills = extract_skills(text)

    assert "mongodb" in skills
    assert "express" in skills
    assert "react" in skills
    assert "node" in skills

# Day 6 - Job Description Parsing System

## Objective

The Day 6 objective is to convert employer job descriptions into structured AI-readable job requirement objects. These objects help Zecpath compare candidate resumes against role requirements during ATS screening and later interview stages.

## Input Data

The parser reads plain text job descriptions from:

```text
data/JD/
```

Each file may contain:

- Role name
- Experience requirement
- Salary range
- Job description
- Key responsibilities
- Skills required
- Education or qualification preferences, if available

## Parser Module

The main parser file is:

```text
parsers/jd_parser.py
```

It performs these steps:

1. Normalize copied text artifacts, extra spaces, bullet points, and section headings.
2. Extract the role name from the first line.
3. Detect role family such as Analyst, Manager, Coordinator, Specialist, Planner, or Supervisor.
4. Extract minimum and maximum experience requirements.
5. Extract salary range when available.
6. Extract job description, responsibilities, required skills, and education preferences.
7. Normalize skill synonyms into AI-friendly skill keywords.
8. Save structured JSON files for downstream AI systems.

## Structured Output

Structured JD outputs are saved in:

```text
data/structured_jds/
```

Each JSON file contains:

- job_id
- source_file
- role_name
- role_family
- experience_required
- salary_range
- job_description
- responsibilities
- required_skills
- education_preferences
- ai_profile

## AI-Friendly Profile

The `ai_profile` field prepares data for ATS matching and scoring. It contains:

- normalized_role
- skill_keywords
- experience_minimum_years

This allows the ATS engine to compare resume skills, candidate experience, and job requirements using consistent fields.

## Skill Synonym Detection

The parser maps common variations to standard skill names.

Examples:

- AI -> artificial intelligence
- ML -> machine learning
- inventory -> inventory management
- warehouse -> warehouse management
- customs -> customs compliance
- problem-solving -> problem solving

## Running the Parser

Use:

```powershell
python run_jd_parsing.py
```

This converts all `.txt` files from `data/JD/` into structured `.json` files inside `data/structured_jds/`.

## Testing

Run:

```powershell
pytest
```

The tests validate:

- JD text normalization
- Role extraction
- Experience extraction
- Salary extraction
- Responsibility extraction
- Skill synonym normalization

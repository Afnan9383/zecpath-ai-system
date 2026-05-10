import re
from pathlib import Path
from pypdf import PdfReader
from docx import Document
from utils.logger import get_logger

logger = get_logger()


def extract_text_from_pdf(file_path: str) -> str:
    text = ""

    try:
        reader = PdfReader(file_path)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        logger.info(f"PDF text extracted successfully: {file_path}")
        return text

    except Exception as error:
        logger.error(f"PDF extraction failed: {file_path} | {error}")
        return ""


def extract_text_from_docx(file_path: str) -> str:
    text = ""

    try:
        document = Document(file_path)

        for paragraph in document.paragraphs:
            if paragraph.text.strip():
                text += paragraph.text + "\n"

        for table in document.tables:
            for row in table.rows:
                row_text = []
                for cell in row.cells:
                    if cell.text.strip():
                        row_text.append(cell.text.strip())
                if row_text:
                    text += " | ".join(row_text) + "\n"

        logger.info(f"DOCX text extracted successfully: {file_path}")
        return text

    except Exception as error:
        logger.error(f"DOCX extraction failed: {file_path} | {error}")
        return ""


def clean_resume_text(raw_text: str) -> str:
    text = raw_text

    text = text.replace("\r", "\n")
    text = re.sub(r"[•●▪■]", "-", text)
    text = re.sub(r"\t+", " ", text)
    text = re.sub(r" +", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[^\S\n]+", " ", text)

    section_headings = [
        "summary",
        "profile",
        "skills",
        "experience",
        "work experience",
        "education",
        "projects",
        "certifications",
        "achievements",
        "contact"
    ]

    for heading in section_headings:
        pattern = rf"(?im)^\s*{heading}\s*$"
        text = re.sub(pattern, heading.upper(), text)

    return text.strip()


def extract_resume_text(file_path: str) -> str:
    file_extension = Path(file_path).suffix.lower()

    if file_extension == ".pdf":
        raw_text = extract_text_from_pdf(file_path)
    elif file_extension == ".docx":
        raw_text = extract_text_from_docx(file_path)
    else:
        logger.error(f"Unsupported resume format: {file_extension}")
        return ""

    return clean_resume_text(raw_text)


def save_extracted_text(input_file: str, output_folder: str = "data/extracted_resumes") -> str:
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    cleaned_text = extract_resume_text(input_file)

    output_file_name = Path(input_file).stem + ".txt"
    output_path = Path(output_folder) / output_file_name

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(cleaned_text)

    logger.info(f"Cleaned resume text saved: {output_path}")

    return str(output_path)

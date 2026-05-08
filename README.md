\# Zecpath AI System



Zecpath AI System is the artificial intelligence backend for the Zecpath hiring platform. It supports resume parsing, ATS scoring, AI screening, interview evaluation, behavior analysis, and final candidate scoring.



\## Project Structure



\- data/ - Stores sample resumes, job descriptions, and test data.

\- parsers/ - Resume parsing and candidate data extraction.

\- ats\_engine/ - ATS score calculation and job matching.

\- screening\_ai/ - AI voice screening and eligibility checks.

\- interview\_ai/ - HR and technical interview evaluation.

\- scoring/ - Final decision and ranking logic.

\- utils/ - Logging, configuration, and helper functions.

\- tests/ - Unit tests for AI modules.



\## Setup Instructions



```bash

python -m venv venv

venv\\Scripts\\activate

pip install -r requirements.txt

python main.py




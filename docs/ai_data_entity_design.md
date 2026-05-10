\# Zecpath AI Data Entity Design Document



\## Objective



The purpose of Day 4 is to understand hiring data and convert unstructured resumes and job descriptions into structured AI-ready formats. This helps Zecpath AI perform resume parsing, ATS scoring, screening, interview evaluation, and final decision-making.



\## Resume Data Understanding



Resumes usually contain unstructured information such as candidate name, contact details, skills, work experience, education, projects, and certifications.



Zecpath AI must extract this information and convert it into structured JSON format.



\## Common Resume Entities



\### Candidate Profile



The candidate profile stores the complete details of a job applicant.



Fields include:



\- Candidate ID

\- Full name

\- Email

\- Phone number

\- Location

\- LinkedIn profile

\- Portfolio

\- Professional summary

\- Total experience

\- Current designation

\- Domain



\### Skill Object



The skill object stores candidate skills in a structured format.



Fields include:



\- Skill name

\- Skill type

\- Proficiency level

\- Years of experience



Skill types:



\- Technical skill

\- Soft skill

\- Tool

\- Programming language

\- Communication skill



\### Experience Object



The experience object stores employment history.



Fields include:



\- Company name

\- Designation

\- Start date

\- End date

\- Duration

\- Responsibilities

\- Technologies used



\### Education Object



The education object stores academic background.



Fields include:



\- Degree

\- Institution

\- Field of study

\- Start year

\- End year

\- Grade or percentage



\### Certification Object



The certification object stores professional certifications.



Fields include:



\- Certification name

\- Issuing organization

\- Issue date

\- Expiry date



\## Job Description Data Understanding



Job descriptions contain hiring requirements such as role title, required skills, responsibilities, qualifications, experience range, work mode, and salary range.



Zecpath AI must structure job descriptions so they can be compared with candidate resumes.



\## Job Profile Entity



The job profile represents a hiring requirement created by a recruiter.



Fields include:



\- Job ID

\- Job title

\- Department

\- Job type

\- Work mode

\- Location

\- Required experience

\- Required skills

\- Responsibilities

\- Qualifications

\- Certifications

\- Salary range

\- Selection process



\## Why Structured Data is Required



Structured data is required because AI systems need clean and consistent inputs. Resume and job description data may come in different formats, but AI scoring requires a standard format.



Structured data helps in:



\- Resume parsing

\- ATS score calculation

\- Skill matching

\- Experience matching

\- Candidate ranking

\- Interview question generation

\- Final hiring decision support



\## Example AI Usage



1\. Resume Parser extracts candidate information.

2\. ATS AI compares resume data with job description data.

3\. Screening AI uses candidate profile and job profile to ask questions.

4\. Interview AI evaluates answers based on role requirements.

5\. Decision AI combines all scores and recommends selection, rejection, or hold.



\## Conclusion



The structured resume schema and job description schema form the foundation of the Zecpath AI hiring pipeline. These schemas help convert unstructured hiring data into clean AI-ready data for fair, scalable, and automated recruitment.




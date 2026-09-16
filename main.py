import os
import json
from dotenv import load_dotenv
from google import genai


# ==============================
# SETUP
# ==============================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the .env file.")

client = genai.Client(api_key=api_key)


# ==============================
# AI JOB ANALYSIS FUNCTION
# ==============================

def analyze_job(job_description, my_skills):

    response = client.models.generate_content(
        model="gemini-3.6-flash",

        contents=f"""
        Analyze this job description and compare it
        with the candidate's skills.

        Candidate skills:
        {my_skills}

        Job description:
        {job_description}

        Do semantic matching.

        For example:
        - "n8n" can match "n8n automation"
        - "JavaScript" can match "JavaScript development"
        - "API integration" should NOT automatically match
          just because the candidate knows JavaScript.

        Return ONLY valid JSON in this structure:

        {{
            "required_skills": [],
            "matched_skills": [],
            "related_skills": [],
            "missing_skills": [],
            "recommendation": ""
        }}

        Rules:

        matched_skills:
        Skills the candidate clearly has.

        related_skills:
        Skills that are closely related but not exactly the same.

        missing_skills:
        Skills the candidate does not have.

        recommendation:
        Give a short practical recommendation.
        Mention strengths, important gaps and what to learn first.

        Keep skill names concise.
        """,

        config={
            "response_mime_type": "application/json"
        }
    )

    return json.loads(response.text)


# ==============================
# SCORE CALCULATION FUNCTION
# ==============================

def calculate_score(data):

    matched_count = len(data["matched_skills"])
    related_count = len(data["related_skills"])
    missing_count = len(data["missing_skills"])

    total_required = (
        matched_count
        + related_count
        + missing_count
    )

    if total_required == 0:
        return 0

    score = (
        (matched_count * 1.0)
        + (related_count * 0.5)
    ) / total_required * 100

    return score


# ==============================
# YOUR SKILLS
# ==============================

my_skills = [
    "Webflow",
    "HTML",
    "CSS",
    "JavaScript",
    "n8n",
    "Make",
    "Kajabi"
]


# ==============================
# GET JOB DESCRIPTION
# ==============================

print("\nPaste the job description below.")
print("Type END on a new line when finished.\n")

job_lines = []

while True:
    line = input()

    if line.strip() == "END":
        break

    job_lines.append(line)

job_description = "\n".join(job_lines)


# ==============================
# RUN ANALYSIS
# ==============================

data = analyze_job(
    job_description,
    my_skills
)


# ==============================
# CALCULATE SCORE
# ==============================

score = calculate_score(data)


# ==============================
# DISPLAY RESULT
# ==============================

print("\n==============================")
print("       AI JOB ANALYSIS")
print("==============================")


print("\nRequired Skills:")

for skill in data["required_skills"]:
    print("-", skill)


print("\nMatched Skills:")

for skill in data["matched_skills"]:
    print("-", skill)


print("\nRelated Skills:")

for skill in data["related_skills"]:
    print("-", skill)


print("\nMissing Skills:")

for skill in data["missing_skills"]:
    print("-", skill)


print("\n------------------------------")
print(f"Match Score: {score:.0f}%")
print("------------------------------")


print("\nRecommendation:")
print(data["recommendation"])
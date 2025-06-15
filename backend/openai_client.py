import json
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)

async def ask(prompt: str) -> str:
    response = await client.chat.completions.create(
        model="mistralai/mistral-7b-instruct:free",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=600  # increase tokens for full response
    )
    content = response.choices[0].message.content.strip()
    print("Raw AI response:", content)  # DEBUG: log raw response
    return content

def safe_json_loads(text: str):
    try:
        return json.loads(text)
    except Exception as e:
        print(f"JSON parse error: {e}\nText was: {text}")  # DEBUG: log parse error
        return None

async def generate_ai_summary(resume_text: str, jd_text: str) -> dict:
    prompt_matched = f"""
You are an AI assistant.

From the resume below, identify skills or experiences that match with the job description.

**IMPORTANT:** ONLY reply with a valid JSON array of strings.

Job Description:
{jd_text}

Resume:
{resume_text}
"""

    prompt_missing = f"""
You are an AI assistant.

From the job description below, identify important skills that are missing in the resume.

**IMPORTANT:** ONLY reply with a valid JSON array of strings.

Job Description:
{jd_text}

Resume:
{resume_text}
"""

    prompt_summary = f"""
You are an AI assistant.

Based on the job description and resume, rate the candidate's fitness on a scale of 0 to 100.

Then provide a short summary paragraph highlighting strengths and areas of improvement.

**IMPORTANT:** ONLY reply with a valid JSON object with keys:
- rating_percent (integer)
- summary (string)

Job Description:
{jd_text}

Resume:
{resume_text}
"""

    try:
        matched_skills_str = await ask(prompt_matched)
        matched_skills = safe_json_loads(matched_skills_str)
        if matched_skills is None:
            matched_skills = []

        missing_skills_str = await ask(prompt_missing)
        missing_skills = safe_json_loads(missing_skills_str)
        if missing_skills is None:
            missing_skills = []

        summary_str = await ask(prompt_summary)
        summary_response = safe_json_loads(summary_str)
        if summary_response is None:
            summary_response = {"rating_percent": 0, "summary": "Failed to parse AI summary."}

        return {
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "rating_percent": summary_response.get("rating_percent", 0),
            "summary": summary_response.get("summary", "")
        }

    except Exception as e:
        return {
            "matched_skills": [],
            "missing_skills": [],
            "rating_percent": 0,
            "summary": f"AI error: {str(e)}"
        }

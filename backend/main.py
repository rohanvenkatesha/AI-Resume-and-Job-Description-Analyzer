from fastapi import FastAPI, UploadFile, File, Form
from typing import Optional

from parser import extract_text
from matcher import match_skills
from openai_client import generate_ai_summary

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend (e.g. localhost:3000) to access backend APIs
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with ["http://localhost:3000"] in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze/")
async def analyze_resume_and_jd(
    resume: UploadFile = File(...),
    job_description: str = Form(...),
    use_ai: Optional[bool] = Form(False)
):
    if not resume.filename.endswith(".pdf"):
        return {"error": "Resume must be a PDF file."}

    resume_bytes = await resume.read()

    try:
        resume_text = extract_text(resume_bytes, resume.filename)
    except ValueError as e:
        return {"error": str(e)}

    jd_text = job_description

    if use_ai:
        # Use AI to get matched, missing, rating, summary
        ai_result = await generate_ai_summary(resume_text, jd_text)

        return {
            "matched_keywords": ai_result.get("matched_skills", []),
            "missing_keywords": ai_result.get("missing_skills", []),
            "match_score": ai_result.get("rating_percent", 0),
            "ai_summary": ai_result.get("summary", "")
        }

    else:
        # Fallback keyword matcher (non-AI)
        result = match_skills(resume_text, jd_text)
        missing = result.get("missing_keywords", [])
        ai_summary = (
            "Suggestion: Consider including skills like: " + ", ".join(missing[:5])
            if missing else
            "Good match! Your resume covers the key job requirements."
        )

        return {
            **result,
            "ai_summary": ai_summary
        }

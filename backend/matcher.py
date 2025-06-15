import spacy
from typing import List, Dict

nlp = spacy.load("en_core_web_sm")

def extract_skill_phrases(text: str) -> List[str]:
    doc = nlp(text.lower())
    phrases = set()

    for chunk in doc.noun_chunks:
        phrase = chunk.text.strip()
        if 2 <= len(phrase) <= 40:
            phrases.add(phrase)

    return list(phrases)

def match_skills(resume_text: str, jd_text: str) -> Dict[str, any]:
    resume_skills = extract_skill_phrases(resume_text)
    jd_skills = extract_skill_phrases(jd_text)

    matched = [skill for skill in jd_skills if skill in resume_skills]
    missing = [skill for skill in jd_skills if skill not in resume_skills]

    match_score = round(len(matched) / len(jd_skills) * 100, 2) if jd_skills else 0.0

    return {
        "match_score": match_score,
        "matched_keywords": matched,
        "missing_keywords": missing
    }

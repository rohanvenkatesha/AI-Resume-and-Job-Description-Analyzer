# 🧠 AI Resume and Job Description Analyzer

A full-stack AI-powered application that compares a candidate's resume with a job description and returns keyword matches, missing skills, a fit score, and a smart AI-generated summary.

---

## 🚀 Tech Stack

### 🖥️ Backend
- **FastAPI** – High-performance API framework
- **Python** – Main backend language
- **spaCy** – NLP processing (for text analysis and skill extraction)
- **OpenAI-compatible API via OpenRouter** – Uses **Mistral 7B Instruct** model
- **Uvicorn** – ASGI server for FastAPI

### 🌐 Frontend
- **Next.js** with **TypeScript** – React-based frontend framework
- **Axios** – For API requests
- **Tailwind CSS / Custom Styles** – Styling components

## 📄 Features

- 🧾 Upload **Resume (PDF)** and **Job Description (Text/Plain)**
- ⚙️ Extracts and matches tech & soft skills using NLP (spaCy)
- 💡 AI-generated summary (optional) using **Mistral 7B**
- 📊 Output:
  - `matched_skills`
  - `missing_skills`
  - `rating_percent` (fit score)
  - `summary` (smart overview)

---

## 📁 Project Structure

```

AI-Resume-and-Job-Description-Analyzer/
├── backend/
│   ├── main.py               # FastAPI API server
│   ├── parser.py             # Resume text extractor using PyMuPDF or similar
│   ├── matcher.py            # spaCy-powered skill matcher
│   ├── openai_client.py      # Calls OpenRouter (Mistral 7B)
│   ├── requirements.txt      # Python packages including spaCy
│   └── .env                  # Contains OpenRouter API key (ignored by Git)
├── frontend/
│   ├── pages/                # Next.js pages
│   ├── components/           # Upload & display components
│   ├── styles/               # CSS or Tailwind
│   └── package.json          # Frontend dependencies
├── .gitignore
└── README.md

````

---

## 🛠️ Backend Setup

1. Navigate to backend folder:
    ```bash
    cd backend
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    ```bash
    python -m spacy download en_core_web_sm
    ```
3. Create a `.env` file with your API key:
    ```
    OPENROUTER_API_KEY=your_openrouter_api_key
    ```

4. Run the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

---

## 💻 Frontend Setup

1. Navigate to frontend folder:
    ```bash
    cd frontend
    ```

2. Install frontend dependencies:
    ```bash
    npm install
    ```

3. Start the development server:
    ```bash
    npm run dev
    ```

---

## 🧪 Sample Output

```json
{
  "matched_skills": ["Python", "AWS", "Docker", "CI/CD"],
  "missing_skills": ["Kafka", "IaC", "React"],
  "rating_percent": 75,
  "summary": "Candidate has strong backend experience, especially with AWS and Python, but lacks some frontend and DevOps-related skills needed for the role."
}
````

---

## 🔒 Environment Variables

Your `.env` file (located inside `/backend`) should include:

```
OPENROUTER_API_KEY=your_openrouter_api_key
```

✅ `.env` is already excluded in `.gitignore`.

---

## 🙋‍♂️ Author

**Rohan Venkatesha**
🔗 [GitHub](https://github.com/rohanvenkatesha)
💼 [LinkedIn](https://linkedin.com/in/rohanvenkatesha)

---

## 📜 License

MIT License – Feel free to use, adapt, and contribute!

```

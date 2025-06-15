# 🧠 AI Resume and Job Description Analyzer

A web application that analyzes resumes against job descriptions and provides keyword matches, missing skills, and an AI-generated summary of how well the resume fits the job.

Built with:
- Frontend: [Next.js](https://nextjs.org/) + TypeScript
- Backend: [FastAPI](https://fastapi.tiangolo.com/)
- AI Model: [Mistral 7B via OpenRouter](https://openrouter.ai/)

---

## 🔧 Features

- 📄 Upload your **Resume (PDF)** and **Job Description (text)**
- 🧠 Optional **AI-enhanced analysis** using Mistral 7B
- 📊 Outputs:
  - Matched keywords
  - Missing skills
  - Fit score (0-100%)
  - AI-generated summary

---

## 📁 Project Structure

```

AI-Resume-and-Job-Description-Analyzer/
├── backend/
│   ├── main.py               # FastAPI API server
│   ├── parser.py             # Resume text extraction logic
│   ├── matcher.py            # Keyword comparison engine
│   ├── openai_client.py      # Mistral 7B client via OpenRouter
│   ├── requirements.txt      # Python dependencies
│   └── .env                  # API keys (excluded from version control)
├── frontend/
│   ├── pages/                # Next.js frontend pages
│   ├── components/           # Reusable UI components
│   ├── styles/               # Styling (CSS/SCSS)
│   └── package.json          # Node dependencies
├── .gitignore
└── README.md

````

---

## 🖥️ Backend Setup

1. Navigate to the backend folder:
    ```bash
    cd backend
    ```

2. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file:
    ```
    OPENROUTER_API_KEY=your_openrouter_api_key
    ```

4. Run FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

---

## 🌐 Frontend Setup

1. Navigate to the frontend folder:
    ```bash
    cd frontend
    ```

2. Install Node dependencies:
    ```bash
    npm install
    ```

3. Run the Next.js development server:
    ```bash
    npm run dev
    ```

---

## 🔒 Environment Variables

Create a `.env` file inside the `backend/` folder with:

````

OPENROUTER\_API\_KEY=your\_openrouter\_api\_key

```

Make sure `.env` is excluded from Git using `.gitignore`.

---

## 🙋‍♂️ Author

**Rohan Venkatesha**  
🔗 [GitHub](https://github.com/rohanvenkatesha)  
💼 [LinkedIn](https://linkedin.com/in/rohanvenkatesha)

---

## 📜 License

MIT License - Feel free to use, modify, and share.
```

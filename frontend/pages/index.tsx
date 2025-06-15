import React, { useState } from "react";
import axios from "axios";
import { CircularProgressbar, buildStyles } from "react-circular-progressbar";
import "react-circular-progressbar/dist/styles.css";

type AnalysisResult = {
  match_score: number;
  matched_keywords: string[];
  missing_keywords: string[];
  ai_summary: string;
};

export default function Home() {
  const [resumeFile, setResumeFile] = useState<File | null>(null);
  const [jobDescription, setJobDescription] = useState("");
  const [useAI, setUseAI] = useState(false);

  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<AnalysisResult | null>(null);
  const [error, setError] = useState("");

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setResult(null);

    if (!resumeFile) {
      setError("Please upload a resume PDF file.");
      return;
    }

    if (!jobDescription.trim()) {
      setError("Please enter the job description.");
      return;
    }

    if (!resumeFile.name.toLowerCase().endsWith(".pdf")) {
      setError("Resume file must be a PDF.");
      return;
    }

    setLoading(true);

    try {
      const formData = new FormData();
      formData.append("resume", resumeFile);
      formData.append("job_description", jobDescription);
      formData.append("use_ai", useAI ? "true" : "false");

      const response = await axios.post(
        `${process.env.NEXT_PUBLIC_API_URL}/analyze/`,
        formData,
        {
          headers: { "Content-Type": "multipart/form-data" },
        }
      );

      if (response.data.error) {
        setError(response.data.error);
      } else {
        setResult(response.data);
      }
    } catch (err: any) {
      console.error(err);
      setError("Failed to analyze. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  // Determine circle color based on score
  const getCircleColor = (score: number) => {
    if (score > 70) return "#4caf50"; // Green
    if (score > 40) return "#ff9800"; // Orange
    return "#f44336"; // Red
  };

  return (
    <div className="max-w-3xl mx-auto p-6 font-sans">
      <h1 className="text-3xl font-bold mb-6">AI Resume & Job Description Analyzer</h1>

      <form onSubmit={onSubmit} className="space-y-6 mb-8">
        <div>
          <label htmlFor="resume" className="block mb-2 font-medium">
            Upload Resume (PDF only):
          </label>
          <input
            type="file"
            id="resume"
            accept="application/pdf"
            onChange={(e) => setResumeFile(e.target.files ? e.target.files[0] : null)}
            className="block w-full text-sm text-gray-600 file:mr-4 file:py-2 file:px-4
              file:rounded file:border-0
              file:text-sm file:font-semibold
              file:bg-blue-50 file:text-blue-700
              hover:file:bg-blue-100"
          />
        </div>

        <div>
          <label htmlFor="jd" className="block mb-2 font-medium">
            Paste Job Description:
          </label>
          <textarea
            id="jd"
            rows={8}
            className="w-full rounded border border-gray-300 p-2 text-sm resize-y"
            value={jobDescription}
            onChange={(e) => setJobDescription(e.target.value)}
            placeholder="Paste the job description here..."
          />
        </div>

        <div className="flex items-center space-x-2">
          <input
            type="checkbox"
            id="useAI"
            checked={useAI}
            onChange={() => setUseAI(!useAI)}
            className="h-4 w-4 text-blue-600"
          />
          <label htmlFor="useAI" className="font-medium select-none">
            Enable AI-powered analysis (requires OpenAI API)
          </label>
        </div>

        <button
          type="submit"
          disabled={loading}
          className="bg-blue-600 text-white px-4 py-2 rounded disabled:opacity-50"
        >
          {loading ? "Analyzing..." : "Analyze"}
        </button>
      </form>

      {error && <p className="text-red-600">{error}</p>}

      {result && (
        <div>
          <h2 className="text-2xl font-semibold mb-4">Skill Match Results</h2>

          <table className="w-full border border-gray-300 mb-6 text-sm text-left border-collapse">
            <thead>
              <tr>
                <th className="border border-gray-300 p-2 bg-gray-100">Matched Skills</th>
                <th className="border border-gray-300 p-2 bg-gray-100">Missing Skills</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td className="border border-gray-300 p-2 align-top">
                  <ul className="list-disc pl-5">
                    {result.matched_keywords.map((skill, i) => (
                      <li key={`m-${i}`}>{skill}</li>
                    ))}
                  </ul>
                </td>
                <td className="border border-gray-300 p-2 align-top">
                  <ul className="list-disc pl-5">
                    {result.missing_keywords.map((skill, i) => (
                      <li key={`mm-${i}`}>{skill}</li>
                    ))}
                  </ul>
                </td>
              </tr>
            </tbody>
          </table>

          <div className="flex items-center space-x-8">
            <div className="w-24 h-24">
              <CircularProgressbar
                value={result.match_score}
                text={`${result.match_score}%`}
                styles={buildStyles({
                  textColor: getCircleColor(result.match_score),
                  pathColor: getCircleColor(result.match_score),
                  trailColor: "#ddd",
                })}
              />
            </div>
            <div className="flex-1">
              <h3 className="text-xl font-semibold mb-2">Match Summary</h3>
              <p className="text-gray-700 whitespace-pre-line">{result.ai_summary}</p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

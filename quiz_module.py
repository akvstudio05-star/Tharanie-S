from google import genai
import os
import json

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_quiz(topic: str) -> str:
    prompt = f"""
You are EduGenie, an educational quiz generator.

Create exactly 3 multiple-choice questions about:
{topic}

Each question must have exactly 4 options (A, B, C, D)
and one correct answer.

Return ONLY valid JSON in this format:

[
  {{
    "question": "Question text",
    "options": {{
      "A": "Option A",
      "B": "Option B",
      "C": "Option C",
      "D": "Option D"
    }},
    "answer": "A"
  }}
]

Do not add markdown, explanations, or any text outside the JSON.
"""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )
    try:
        quiz_data = json.loads(response.text)
        return quiz_data
    except json.JSONDecodeError:
        return []
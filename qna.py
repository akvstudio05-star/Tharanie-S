from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def answer_question(question: str) -> str:
    prompt = f"""
You are EduGenie, a helpful learning assistant for students.

Answer the following question clearly and concisely.
Use simple language and give a short example when useful.

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return response.text
from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def summarize_text(text: str) -> str:
    prompt = f"""
You are EduGenie, an educational assistant.

Summarize the following passage in simple and clear language.

Passage:
{text}

Give:
- Main idea
- Important points
- Short summary
"""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return response.text
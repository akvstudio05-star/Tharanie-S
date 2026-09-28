from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def explain_concept(concept: str) -> str:
    prompt = f"""
You are EduGenie, an educational assistant.

Explain the following concept in very simple language so that a student
can understand it easily.

Concept:
{concept}

Give:
1. Simple definition
2. Easy explanation
3. One real-world example
4. Short summary
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
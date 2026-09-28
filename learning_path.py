from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def recommend_learning_path(topic: str) -> str:
    prompt = f"""
You are EduGenie, a personalized learning assistant.

Create a simple learning path for a student who wants to learn:
{topic}

Include:
1. Beginner topics
2. Intermediate topics
3. Advanced topics
4. Practice activities
5. Useful project ideas

Keep the recommendations clear, practical, and easy to follow.
"""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return response.text
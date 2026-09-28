from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv

load_dotenv()

from qna import answer_question
from explanation_module import explain_concept
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import recommend_learning_path


app = FastAPI(
    title="EduGenie - AI Powered Learning Assistant",
    description="Google Gemini powered learning assistant for students.",
    version="1.0.0"
)


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
   return templates.TemplateResponse(
    request=request,
    name="index.html"
)


@app.get("/qa")
async def qa(question: str = Query(...)):
    answer = answer_question(question)
    return {
        "question": question,
        "answer": answer
    }


@app.post("/explain")
async def explain_api(request: Request):
    data = await request.json()
    topic = data.get("topic")

    if not topic:
        return JSONResponse(
            content={"error": "Please provide a topic."},
            status_code=400
        )

    explanation = explain_concept(topic)

    return {
        "topic": topic,
        "explanation": explanation
    }


@app.post("/quiz")
async def quiz_api(request: Request):
    data = await request.json()
    topic = data.get("topic")

    if not topic:
        return JSONResponse(
            content={"error": "Please provide a topic."},
            status_code=400
        )

    quiz = generate_quiz(topic)

    return {
        "topic": topic,
        "quiz": quiz
    }


@app.post("/summarize")
async def summarize_api(request: Request):
    data = await request.json()
    text = data.get("text")

    if not text:
        return JSONResponse(
            content={"error": "Please provide text to summarize."},
            status_code=400
        )

    summary = summarize_text(text)

    return {
        "summary": summary
    }


@app.get("/learn/recommendations")
async def learning_recommendations(
    topic: str = Query(...)
):
    recommendation = recommend_learning_path(topic)

    return {
        "topic": topic,
        "recommendation": recommendation
    }
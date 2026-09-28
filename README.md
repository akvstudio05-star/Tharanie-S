# EduGenie – Google Gemini Powered Learning Assistant

EduGenie is a lightweight AI-powered educational assistant designed to make learning easier through generative AI. It helps students ask questions, understand complex concepts, generate quizzes, summarize educational content, and receive personalized learning recommendations.

## 👥 Team Details

* **Team ID:** SWTID-2026-6841
* **Team Size:** 4
* **Team Leader:** Tharanie S
* **Team Members:**

  * Thirisha S
  * Thrisha R
  * Tiksha P

## ✨ Features

EduGenie provides the following learning features:

1. **Question & Answer**

   * Ask academic or general knowledge questions.
   * Receive AI-generated answers using Google Gemini.

2. **Concept Explanation**

   * Explains difficult topics in simple and easy-to-understand language.
   * Uses the lightweight LaMini-Flan-T5 model for concept explanation.

3. **Quiz Generation**

   * Generates quizzes from a topic or supplied text.
   * Provides multiple-choice questions with four options.
   * Identifies the correct answer.

4. **Summarization**

   * Converts long educational passages into concise summaries.
   * Keeps the important information while removing unnecessary details.

5. **Personalized Learning Path**

   * Creates a structured learning path from beginner to advanced level.
   * Can provide suggested learning resources such as videos, articles, and books.

## 🛠️ Technologies Used

* **Python 3.10+**
* **FastAPI** – Backend REST API
* **Google Gemini API** – AI-powered Q&A, quiz generation, summarization, and learning recommendations
* **LaMini-Flan-T5-783M** – Local concept explanation model
* **HTML5** – Frontend structure
* **CSS3** – Frontend styling
* **Jinja2** – HTML templating
* **Uvicorn** – ASGI server

## 📁 Project Structure

```text
EduGenie/
│
├── main.py
├── explanation_module.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── .env
├── requirements.txt
└── README.md
```

## 🔌 API Endpoints

| Endpoint                 | Purpose                           |
| ------------------------ | --------------------------------- |
| `/qa`                    | Question answering                |
| `/explain`               | Explain a concept                 |
| `/quiz`                  | Generate a quiz                   |
| `/summarize`             | Summarize text                    |
| `/learn/recommendations` | Generate learning recommendations |

## ⚙️ Installation

### 1. Install Python

Install **Python 3.10 or later**.

Verify the installation:

```bash
python --version
```

If `python` is not recognized on Windows, try:

```bash
py --version
```

### 2. Clone or open the project

Open the EduGenie project folder in VS Code.

### 3. Create a virtual environment

Windows:

```bash
py -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

If `py` is unavailable but Python is installed as `python3`:

```bash
python3 -m venv venv
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

If your project does not yet contain `requirements.txt`, install the main packages:

```bash
pip install fastapi uvicorn jinja2 python-dotenv google-generativeai
```

Install the required local-model packages only if the current implementation uses LaMini-Flan-T5:

```bash
pip install transformers torch sentencepiece
```

## 🔑 Gemini API Configuration

Create a `.env` file in the project root.

Example:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Replace the placeholder with your Gemini API key.

**Important:** Never upload your real API key to GitHub. Add `.env` to `.gitignore`.

Example `.gitignore`:

```gitignore
venv/
__pycache__/
.env
*.pyc
```

## ▶️ Run the Project

From the project root:

```bash
uvicorn main:app --reload
```

The application will normally be available at:

```text
http://127.0.0.1:8000
```

Open that address in your browser.

## 🧪 Functional Testing

After starting the application, test each feature:

### Ask a Question

Enter a question and select **QnA**.

### Explain a Topic

Enter a difficult topic and select **Explain**.

### Generate a Quiz

Enter a topic and select **Quiz**.

### Summarize Content

Paste a long paragraph and select **Summary**.

### Get a Learning Path

Enter a subject or topic and select **Recommend Path**.

## 🔄 Project Workflow

```text
User
  │
  ▼
HTML + CSS Frontend
  │
  ▼
FastAPI Backend
  │
  ├── /qa ───────────────► Gemini
  │
  ├── /explain ──────────► LaMini-Flan-T5
  │
  ├── /quiz ─────────────► Gemini
  │
  ├── /summarize ────────► Gemini
  │
  └── /learn/recommendations ─► Gemini
  │
  ▼
AI Generated Result
  │
  ▼
Displayed in Web Interface
```

## 🧩 Module Description

### `main.py`

Creates the FastAPI application and defines the API endpoints.

### `explanation_module.py`

Handles simplified concept explanations using the local LaMini-Flan-T5 model.

### `qna.py`

Handles question-answering requests using Gemini.

### `quiz_module.py`

Generates structured multiple-choice quizzes.

### `summary_module.py`

Summarizes long educational passages.

### `learning_path.py`

Generates personalized learning recommendations from beginner to advanced level.

### `templates/index.html`

Contains the main web interface.

### `static/style.css`

Contains the styling and responsive design for the frontend.

## 📌 Example Use Cases

* A student asks: **"Which is the largest ocean?"**
* A student requests a quiz on **Pythagoras Theorem**.
* A learner studying SQL requests a **step-by-step learning path**.
* A student pastes a long lesson and asks EduGenie to **summarize it**.
* A beginner asks EduGenie to **explain a difficult concept simply**.

## 🚀 Future Enhancements

The project can be extended with:

* Voice-based interaction
* Multilingual support
* Mobile application
* Offline learning features
* Progress tracking dashboards
* Gamification such as badges and learning streaks
* Adaptive learning paths
* Group study sessions
* Teacher and parent dashboards
* Moodle or Google Classroom integration
* Image and PDF input
* Snapshot-based doubt solving
* Smart notifications

## 🔒 Security Notes

* Keep the Gemini API key private.
* Store secrets in `.env`.
* Do not commit `.env` to GitHub.
* Use environment variables instead of hard-coding API keys.
* Review AI-generated answers before using them for important academic decisions.

## 📄 License

This project is intended as an educational/project-development application. Add an appropriate open-source license if the project is distributed publicly.

## 👩‍💻 Team

**Team ID:** SWTID-2026-6841
**Team Leader:** Tharanie S
**Members:** Thirisha S, Thrisha R, Tiksha P

Chatbot Platform – Backend API

Software Engineer Intern Assignment

A backend API for a chatbot platform where authenticated users can create projects, manage prompts, and chat with an AI model. Built with clean architecture, secure authentication, and modern AI integration.

🚀 Key Features

JWT authentication (Register / Login)

Project-based isolation & ownership

Prompt management per project

AI-powered chat endpoint

Secure, RESTful API design

🛠️ Tech Stack

Backend: Django, Django REST Framework

Auth: JWT (SimpleJWT)

AI: OpenAI Responses API

Database: SQLite

Testing: Postman

⚙️ Quick Setup
git clone <repo-url>
cd chatbot-platform-assignment/backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt


Create .env:

DEBUG=True
SECRET_KEY=your-secret-key
OPENAI_API_KEY=your-openai-api-key

python manage.py migrate
python manage.py runserver


Server runs at:

http://127.0.0.1:8000/

🔐 Auth Flow

Register

POST /api/auth/register/


Login

POST /api/auth/login/


Use returned access token:

Authorization: Bearer <ACCESS_TOKEN>

📡 Core API Endpoints

Projects

POST /api/projects/
GET  /api/projects/


Prompts

POST /api/projects/{project_id}/prompts/
GET  /api/projects/{project_id}/prompts/


Chat (Main Feature)

POST /api/projects/{project_id}/chat/

{
  "message": "Explain Django in simple terms"
}


Response

{
  "reply": "Django is a Python web framework..."
}

🧠 Design Highlights

Strong project ownership enforcement

Prompt-based system context injection

Stateless JWT authentication

Uses latest OpenAI API (non-deprecated)

API-first design (no frontend required)

🎥 Demo

A short demo video shows:

Authentication

Project & prompt creation

AI chat response

👤 Author

Tarun HT
Software Engineer Intern Candidate

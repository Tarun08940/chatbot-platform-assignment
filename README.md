# Chatbot Platform – Backend API  
**Software Engineer Intern Assignment**

A backend API for a chatbot platform where authenticated users can create projects, manage prompts, and chat with an AI model. Built with clean architecture, secure authentication, and modern AI integration.

---

## 🎥 Demo Video
▶️ https://your-demo-video-link-here

The demo shows authentication, project creation, prompt setup, and an AI chat response.

---

## 🚀 Key Features

- JWT authentication (Register / Login)
- Project-based isolation and ownership
- Prompt management per project
- AI-powered chat endpoint
- Secure RESTful API design

---

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework  
- **Authentication:** JWT (SimpleJWT)  
- **AI Integration:** OpenAI Responses API  
- **Database:** SQLite  
- **Testing:** Postman  

---

## ⚙️ Quick Setup

```bash
git clone https://github.com/Tarun08940/chatbot-platform-assignment.git
cd chatbot-platform-assignment/backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
Create a .env file:

DEBUG=True
SECRET_KEY=your-secret-key
OPENAI_API_KEY=your-openai-api-key

python manage.py migrate
python manage.py runserver


Server runs at:

http://127.0.0.1:8000/

🔐 Authentication

Register

POST /api/auth/register/


Login

POST /api/auth/login/


Use the returned access token:

Authorization: Bearer <ACCESS_TOKEN>

💬 Chat Endpoint (Core Feature)
POST /api/projects/{project_id}/chat/

{
  "message": "Explain Django in simple terms"
}


Response

{
  "reply": "Django is a Python web framework that helps developers build web applications quickly..."
}

🧠 Design Highlights

Strict project ownership enforcement

Prompt-based system context injection

Stateless JWT authentication

Uses latest non-deprecated OpenAI API

API-first backend design

👤 Author

Tarun HT
Software Engineer Intern Candidate

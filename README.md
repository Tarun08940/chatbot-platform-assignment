# Chatbot Platform – Backend API

**Software Engineer Intern Assignment**

A backend API for a chatbot platform where authenticated users can create projects, manage prompts, and chat with an AI model.  
Built with Django REST Framework, JWT authentication, and OpenAI integration.

---

## 🚀 Features

- JWT Authentication (Register / Login)
- Project-based access control
- Prompt management per project
- AI-powered chat endpoint
- Secure environment-based configuration
- Clean, modular backend architecture

---

## 🧠 Tech Stack

- Python
- Django
- Django REST Framework
- SimpleJWT (Authentication)
- OpenAI API
- SQLite (local development)

---

## 🎥 Demo Video

👉 **Demo Link:** https://your-demo-video-link-here

The demo shows:
- User authentication
- Project creation
- Authenticated AI chat requests
- API testing via Postman

---

## 🧪 API Testing

All endpoints were tested locally using **Postman**.

Example flow:
1. Register / Login
2. Obtain JWT access token
3. Create a project
4. Send chat messages to AI endpoint using Bearer token

---

## ⚙️ Setup Instructions (Local)

```bash
git clone https://github.com/Tarun08940/chatbot-platform-assignment.git
cd chatbot-platform-assignment/backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
Create a .env file:

env
Copy code
SECRET_KEY=your-secret-key
DEBUG=True
OPENAI_API_KEY=your-openai-api-key
Run migrations and start server:

bash
Copy code
python manage.py migrate
python manage.py runserver
🌍 Deployment Note
The application is deployment-ready and configured for cloud hosting.
Live deployment was not included to avoid paid infrastructure for an assignment submission.

👤 Author
Tarun
Backend-focused Software Engineer Intern Candidate

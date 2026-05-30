# 🚀 RAG Chatbot using FastAPI, JWT, Docker & AWS Fargate

## 📌 Project Overview

This project is a production-ready AI-powered RAG (Retrieval Augmented Generation) chatbot built using:

* FastAPI
* LangChain
* OpenAI
* Pinecone Vector Database
* JWT Authentication
* Docker
* AWS ECS Fargate

The chatbot supports secure login authentication and is deployed on AWS cloud using containerized infrastructure.

---

# 🛠️ Tech Stack

## Backend

* FastAPI
* Python

## AI & RAG

* LangChain
* OpenAI
* Pinecone

## Authentication

* JWT Authentication

## Frontend

* HTML
* CSS
* Jinja2 Templates

## Deployment

* Docker
* AWS ECR
* AWS ECS Fargate
* Application Load Balancer

---

# 📂 Project Structure

```bash
DAY10/
│
├── auth/
│   ├── auth_bearer.py
│   ├── jwt_handler.py
│   └── users.py
│
├── data/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── login.html
│
├── .dockerignore
├── .env
├── app.py
├── ingest.py
├── query.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

# 🔐 Features

* JWT-based login authentication
* Secure chatbot routes
* Retrieval Augmented Generation (RAG)
* Vector search using Pinecone
* FastAPI backend APIs
* Beautiful dark-mode chatbot UI
* Dockerized application
* AWS cloud deployment using ECS Fargate
* Public access via Load Balancer

---

# ⚙️ Setup Instructions

# 1️⃣ Clone Repository

```bash
git clone <your-repository-url>
cd DAY10
```

---

# 2️⃣ Create Virtual Environment

```bash
python -m venv ragbotnew
```

Activate environment:

## Windows

```bash
ragbotnew\Scripts\activate
```

## Linux/Mac

```bash
source ragbotnew/bin/activate
```

---

# 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 4️⃣ Configure Environment Variables

Create `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_environment
```

---

# ▶️ Run Application Locally

```bash
uvicorn app:app --reload
```

Application runs on:

```bash
http://127.0.0.1:8000
```

---

# 🔑 Default Login Credentials

```bash
Username: jay
Password: 1234
```

---

# 🐳 Docker Setup

# Build Docker Image

```bash
docker build -t ragchatbot .
```

# Run Docker Container

```bash
docker run -p 8000:8000 ragchatbot
```

---

# ☁️ AWS ECS Fargate Deployment

## Deployment Flow

```text
VS Code
   ↓
Docker Build
   ↓
AWS ECR
   ↓
AWS ECS Fargate
   ↓
Application Load Balancer
   ↓
Public URL
```

---

# 📌 AWS Services Used

* Amazon ECR
* Amazon ECS
* AWS Fargate
* Application Load Balancer
* IAM

---

# 🧠 RAG Workflow

```text
User Query
    ↓
LangChain Retrieval
    ↓
Pinecone Vector Search
    ↓
Relevant Context Fetch
    ↓
OpenAI Response Generation
    ↓
Chatbot Response
```

---

# 🔒 Authentication Flow

```text
User Login
    ↓
JWT Token Generation
    ↓
Token Stored in Cookies
    ↓
Protected Chat Routes
    ↓
Authenticated Access
```

---

# 📸 Screenshots

## Login Page

<img width="886" height="460" alt="image" src="https://github.com/user-attachments/assets/722dd008-d48d-45c4-8766-e4c4fedb9d57" />


## Chatbot UI

<img width="956" height="619" alt="image" src="https://github.com/user-attachments/assets/a424398f-6ffa-40f3-b1ad-c137a1f37283" />


## AWS ECS Deployment

<img width="1019" height="305" alt="image" src="https://github.com/user-attachments/assets/580bd3a4-78a1-47df-a7dc-3b74a98ebe29" />


# 📈 Future Improvements

* User registration
* MongoDB integration
* Password hashing using bcrypt
* HTTPS with SSL
* CI/CD using GitHub Actions
* Auto scaling
* CloudWatch monitoring
* Chat history storage

---

# 👨‍💻 Author

## Jayachandra

AI/GenAI Engineer | FastAPI | LangChain | AWS | Docker

---

# ⭐ GitHub

If you like this project, give it a ⭐ on GitHub.

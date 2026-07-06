# AI Assistant

An AI-powered web assistant built using **Flask** and **Groq's Llama 3.3 70B Versatile** model. The application allows users to ask questions and summarize lengthy emails through a clean and responsive web interface.

---

##  Features

* 💬 AI-powered question answering
* 📧 Email summarization
* ⚡ Fast responses using the Groq API
* 🌐 Responsive web interface
* 🔒 Secure API key management using environment variables
* ✅ Automated testing with Pytest
* 🔄 Continuous Integration (CI) using GitHub Actions
* 📊 99% automated test coverage

---

##  Project Workflow

1. User enters a question or email.
2. Flask receives the request.
3. The request is sent to the Groq API.
4. Llama 3.3 processes the prompt.
5. AI-generated response is returned.
6. The response is displayed in the web interface.

---

## Tech Stack

### Backend

* Python
* Flask

### Frontend

* HTML
* CSS

### AI

* Groq API
* Llama 3.3 70B Versatile

### Testing

* Pytest
* Pytest-Cov
* unittest.mock

### DevOps

* Git
* GitHub
* GitHub Actions (Continuous Integration)

### Environment Management

* python-dotenv
* Virtual Environment (.venv)

---

## Project Structure

```text
AI-Assistant/
│── .github/
│   └── workflows/
│       └── ci.yml
│── static/
│── templates/
│── tests/
│── main.py
│── requirements.txt
│── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd AI-Assistant
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows**

```bash
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Create a `.env` file and add:

```text
GROQ_API_KEY=your_api_key
```

Run the application:

```bash
python main.py
```

---

##  Running Tests

Run all tests:

```bash
python -m pytest
```

Run tests with coverage:

```bash
python -m pytest --cov=.
```

Current Coverage:

* **main.py:** 96%
* **Overall Project:** 99%

---

## Continuous Integration

This project uses **GitHub Actions** to automatically:

* Install project dependencies
* Execute all Pytest test cases
* Verify application stability on every push and pull request

---

##  Deployment

The application is deployed on **Vercel**, which automatically redeploys the application whenever new changes are pushed to the main branch.

---

##  Future Improvements

* Voice input and speech output
* Conversation history
* User authentication
* AWS EC2 deployment
* Complete CI/CD pipeline with automated deployment
* Docker containerization

---

## Author

**Rimple Kosta**







# 🚀 Incident AI System

An automated Incident Management System built using FastAPI and Python, designed to simulate real-world IT Service Management (ITSM) workflows.

---

## 📌 Overview

This project replicates a production support environment where incidents are:
- Logged via API
- Automatically categorized
- Assigned priority levels
- Tracked for resolution

---

## 🔧 Features

- ✅ Create incidents via REST API
- ✅ Auto-classification (Database, Network, Application, General)
- ✅ Dynamic priority assignment (P1, P2, P3)
- ✅ Incident status tracking
- ✅ Timestamp logging

---

## 🧠 Real-World Use Case

This system mimics tools like:
- ServiceNow
- Azure DevOps
- ITSM platforms used in enterprise environments

It helps reduce manual effort in:
- Incident triage
- Priority assignment
- Initial diagnosis

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Uvicorn

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install fastapi uvicorn

2. Start server
uvicorn main:app --reload

3. Open API docs
http://127.0.0.1:8000/docs

sample request
{
  "title": "Database outage",
  "description": "Users unable to connect to DB",
  "severity": "High"
}

📡 API Endpoints
🔹 Create Incident

POST /create-incident

Sample Request:

{
  "title": "Database outage",
  "description": "Users unable to connect to DB",
  "severity": "High"
}
🔹 Get All Incidents

GET /incidents

📊 Sample Output
{
  "id": 1,
  "title": "Database outage",
  "category": "Database",
  "priority": "P1",
  "status": "Open"
}
🔮 Future Enhancements
🔔 Email alerts for P1 incidents
☁️ Azure cloud deployment
📊 Dashboard (Power BI / Streamlit)
🤖 AI-based incident classification (NLP)
👨‍💻 Author

Shaik Fahad
IT Support Engineer | Incident Management | Azure | Python

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

incidents = []

class Incident(BaseModel):
    title: str
    description: str
    severity: str


def classify_incident(description):
    description = description.lower()
    
    if "database" in description:
        return "Database"
    elif "network" in description:
        return "Network"
    elif "login" in description:
        return "Application"
    else:
        return "General"


def assign_priority(severity):
    if severity.lower() == "high":
        return "P1"
    elif severity.lower() == "medium":
        return "P2"
    else:
        return "P3"


@app.post("/create-incident")
def create_incident(incident: Incident):
    category = classify_incident(incident.description)
    priority = assign_priority(incident.severity)

    incident_data = {
        "id": len(incidents) + 1,
        "title": incident.title,
        "description": incident.description,
        "severity": incident.severity,
        "category": category,
        "priority": priority,
        "status": "Open",
        "created_at": str(datetime.now())
    }

    incidents.append(incident_data)

    return {
        "message": "Incident created successfully",
        "data": incident_data
    }


@app.get("/incidents")
def get_incidents():
    return incidents
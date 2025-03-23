import requests

PLAGIARISM_API = "https://www.duplichecker.com/api/v1/plagiarism-check"

def check_plagiarism(text):
    payload = {"text": text}
    response = requests.post(PLAGIARISM_API, json=payload)
    if response.status_code == 200:
        return response.json().get("plagiarism_score", "Error fetching score")
    return "API Error"

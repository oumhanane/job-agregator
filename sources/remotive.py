import requests
from core.normalize import normalize


def fetch():
    url = "https://remotive.com/api/remote-jobs?search=devops"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException:
        return []

    jobs = data.get("jobs", [])

    return [normalize(job, "remotive") for job in jobs]
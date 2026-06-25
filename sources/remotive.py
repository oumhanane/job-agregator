import requests
from core.normalize import normalize

def fetch():
    url = "https://remotive.com/api/remote-jobs?search=devops"
    data = requests.get(url).json()

    jobs = data["jobs"]

    return [normalize(j, "remotive") for j in jobs]
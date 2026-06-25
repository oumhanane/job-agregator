# config.py

# API sources
REMOTIVE_URL = "https://remotive.com/api/remote-jobs?search=devops"

# scoring
MIN_SCORE = 5

# localisation (Île-de-France)
LOCATION_KEYWORDS = [
    "paris",
    "ile-de-france",
    "île-de-france",
    "france",
    "idf"
]

# mots-clés DevOps
DEVOPS_KEYWORDS = {
    "devops": 5,
    "kubernetes": 5,
    "terraform": 4,
    "aws": 3,
    "azure": 3,
    "cloud": 2,
    "sre": 5,
    "platform": 4,
    "ci/cd": 4,
    "docker": 3,
    "linux": 2
}
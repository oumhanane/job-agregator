KEYWORDS = {
    "devops": 10,
    "kubernetes": 10,
    "terraform": 8,
    "ansible": 7,
    "aws": 6,
    "gcp": 6,
    "azure": 6,
    "ci/cd": 6,
    "docker": 5,
    "sre": 10,
    "platform engineer": 9,
    "cloud": 3,
    "linux": 2
}

def score(job):
    text = (job["title"] + " " + job["description"]).lower()

    total = 0
    for k, weight in KEYWORDS.items():
        if k in text:
            total += weight

    return total
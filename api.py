from fastapi import FastAPI, Query
from sources import remotive, hellowork, wttj
from core.filter import is_idf
from core.scorer import score
from config import MIN_SCORE

app = FastAPI(title="Job Aggregator DevOps")


# -------------------------
# HEALTHCHECK / ROOT
# -------------------------
@app.get("/")
def root():
    return {"status": "job-aggregator running"}


# -------------------------
# COLLECTE DES JOBS
# -------------------------
def get_all_jobs():
    jobs = []

    jobs += remotive.fetch()
    jobs += hellowork.fetch()
    jobs += wttj.fetch()

    return jobs


# -------------------------
# ENDPOINT JOBS
# -------------------------
@app.get("/jobs")
def get_jobs(
    min_score: int = Query(default=MIN_SCORE, ge=0),
    source: str = Query(default=None),
    location: str = Query(default=None)
):
    jobs = get_all_jobs()
    filtered = []

    for job in jobs:
        s = score(job)
        job_source = job.get("source", "")

        # filtre par source
        if source and job_source != source:
            continue

        # filtre géographique (FR sources uniquement)
        if job_source in ["hellowork", "wttj"]:
            if not is_idf(job):
                continue

        # filtre location optionnel
        if location:
            job_location = job.get("location", "").lower()
            if location.lower() not in job_location:
                continue

        # filtre score
        if s >= min_score:
            job["score"] = s
            filtered.append(job)

    return {
        "total_jobs": len(jobs),
        "filtered_jobs": len(filtered),
        "filters": {
            "min_score": min_score,
            "source": source,
            "location": location
        },
        "jobs": filtered
    }


# -------------------------
# ENDPOINT STATS
# -------------------------
@app.get("/stats")
def get_stats():
    jobs = get_all_jobs()

    stats = {
        "total_jobs": len(jobs),
        "by_source": {},
        "by_location": {
            "idf": 0,
            "other": 0
        }
    }

    for job in jobs:
        source = job.get("source", "unknown")
        location = job.get("location", "").lower()

        # count by source
        stats["by_source"][source] = stats["by_source"].get(source, 0) + 1

        # simple geo split
        if "paris" in location or "ile-de-france" in location or "idf" in location:
            stats["by_location"]["idf"] += 1
        else:
            stats["by_location"]["other"] += 1

    return stats
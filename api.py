from fastapi import FastAPI, Query
from fastapi.responses import FileResponse

from sources import remotive, hellowork, wttj
from core.filter import is_idf
from core.scorer import score
from config import MIN_SCORE


# -------------------------
# APP INIT
# -------------------------
app = FastAPI(title="Job Aggregator DevOps")


# -------------------------
# DATA PIPELINE
# -------------------------
def get_all_jobs():
    """Collecte multi-sources"""
    jobs = []
    jobs += remotive.fetch()
    jobs += hellowork.fetch()
    jobs += wttj.fetch()
    return jobs


def enrich_jobs(jobs):
    """Ajoute score sans modifier les objets originaux"""
    enriched = []

    for job in jobs:
        job_copy = job.copy()
        job_copy["score"] = score(job)
        enriched.append(job_copy)

    return enriched


def apply_filters(jobs, min_score, source=None, location=None):
    """Filtrage métier centralisé"""
    filtered = []

    for job in jobs:
        job_source = job.get("source", "")

        # filtre source
        if source and job_source != source:
            continue

        # filtre géographique (FR sources uniquement)
        if job_source in ["hellowork", "wttj"] and not is_idf(job):
            continue

        # filtre location
        if location:
            job_location = job.get("location", "").lower()
            if location.lower() not in job_location:
                continue

        # filtre score
        if job.get("score", 0) >= min_score:
            filtered.append(job)

    return filtered


# -------------------------
# HEALTHCHECK
# -------------------------
@app.get("/")
def root():
    return {"status": "job-aggregator running"}


# -------------------------
# API JSON
# -------------------------
@app.get("/jobs")
def get_jobs(
    min_score: int = Query(default=MIN_SCORE, ge=0),
    source: str = Query(default=None),
    location: str = Query(default=None)
):
    jobs = get_all_jobs()
    jobs = enrich_jobs(jobs)
    jobs = apply_filters(jobs, min_score, source, location)

    return {
        "total_jobs": len(get_all_jobs()),
        "filtered_jobs": len(jobs),
        "filters": {
            "min_score": min_score,
            "source": source,
            "location": location
        },
        "jobs": jobs
    }


# -------------------------
# STATS API
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

        stats["by_source"][source] = stats["by_source"].get(source, 0) + 1

        if any(x in location for x in ["paris", "ile-de-france", "idf"]):
            stats["by_location"]["idf"] += 1
        else:
            stats["by_location"]["other"] += 1

    return stats


# -------------------------
# UI (STATIC HTML)
# -------------------------
@app.get("/ui")
def ui():
    return FileResponse("static/index.html")
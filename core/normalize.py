def normalize(job, source):
    return {
        "title": job.get("title", ""),
        "company": job.get("company_name", job.get("company", "")),
        "location": job.get("location", ""),
        "url": job.get("url", job.get("link", "")),
        "description": job.get("description", ""),
        "source": source
    }
def is_idf(job):
    text = (job["title"] + " " + job["description"] + " " + job["location"]).lower()

    keywords = [
        "paris",
        "ile-de-france",
        "île-de-france",
        "france",
        "idf"
    ]

    return any(k in text for k in keywords)
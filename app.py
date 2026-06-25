from sources import remotive, hellowork, wttj
from core.filter import is_idf
from core.scorer import score
from config import MIN_SCORE

import csv


def collect_jobs():
    """Collecte multi-sources"""
    jobs = []

    jobs += remotive.fetch()
    jobs += hellowork.fetch()
    jobs += wttj.fetch()

    return jobs


def filter_and_score(jobs):
    """Filtre + scoring"""
    filtered = []

    for job in jobs:

        # sécurité : champs obligatoires
        if not job.get("title") or not job.get("description"):
            continue

        # score DevOps
        s = score(job)

        source = job.get("source", "")

        # filtre géographique uniquement pour sources FR
        if source in ["hellowork", "wttj"]:
            if not is_idf(job):
                continue

        # seuil de pertinence
        if s >= MIN_SCORE:
            filtered.append((job, s))

    return filtered


def export_csv(filtered):
    """Export CSV final"""
    output_file = "output/jobs.csv"

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow([
            "title",
            "company",
            "location",
            "url",
            "score",
            "source"
        ])

        for job, s in filtered:
            writer.writerow([
                job.get("title", ""),
                job.get("company", ""),
                job.get("location", ""),
                job.get("url", ""),
                s,
                job.get("source", "")
            ])

    print("CSV généré ✔ ->", output_file)


def main():
    jobs = collect_jobs()

    filtered = filter_and_score(jobs)

    filtered.sort(key=lambda x: x[1], reverse=True)

    print("Jobs totaux :", len(jobs))
    print("Jobs filtrés :", len(filtered))

    export_csv(filtered)


if __name__ == "__main__":
    main()
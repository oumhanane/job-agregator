import csv

INPUT = "output/jobs.csv"
OUTPUT = "output/jobs.html"

html = """
<html>
<head>
    <title>Job Aggregator DevOps</title>
    <style>
        body { font-family: Arial; margin: 20px; }
        .job { border: 1px solid #ddd; padding: 10px; margin-bottom: 10px; }
        .score { font-weight: bold; color: green; }
    </style>
</head>
<body>
<h1>Jobs DevOps filtrés</h1>
"""

with open(INPUT, newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        html += f"""
        <div class="job">
            <h3>{row['title']}</h3>
            <p><b>Company:</b> {row['company']}</p>
            <p><b>Location:</b> {row['location']}</p>
            <p><b>Source:</b> {row['source']}</p>
            <p class="score">Score: {row['score']}</p>
            <a href="{row['url']}" target="_blank">Voir l’offre</a>
        </div>
        """

html += "</body></html>"

with open(OUTPUT, "w") as f:
    f.write(html)

print("HTML généré ✔ → output/jobs.html")
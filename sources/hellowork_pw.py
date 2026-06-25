from playwright.sync_api import sync_playwright

def fetch():
    jobs = []

    url = "https://www.hellowork.com/fr-fr/emploi/recherche.html?k=devops&l=ile-de-france"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url, timeout=60000)

        # attendre chargement JS
        page.wait_for_timeout(5000)

        # récupérer les blocs d'annonces
        cards = page.query_selector_all("article")

        for c in cards[:15]:
            text = c.inner_text().strip()

            if not text:
                continue

            lines = text.split("\n")

            title = lines[0] if len(lines) > 0 else "No title"

            jobs.append({
                "title": title,
                "company": "HelloWork",
                "location": "Île-de-France",
                "url": url,
                "description": text,
                "source": "hellowork"
            })

        browser.close()

    return jobs
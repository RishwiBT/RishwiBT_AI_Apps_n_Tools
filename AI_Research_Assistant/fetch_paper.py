import arxiv
import requests
import tempfile

def fetch_arxiv_pdf(query: str) -> str | None:
    search = arxiv.Search(query=query, max_results=1)
    results = list(search.results())

    if not results:
        return None

    paper = results[0]
    pdf_url = paper.pdf_url

    response = requests.get(pdf_url)
    if response.status_code != 200:
        return None

    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    temp.write(response.content)
    temp.close()
    return temp.name

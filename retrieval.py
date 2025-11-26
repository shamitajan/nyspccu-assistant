"""
Simple KB ingestion and retrieval helper.
Builds a tiny in-memory corpus and optionally uses sentence-transformers + FAISS for embeddings.
"""

import requests
from bs4 import BeautifulSoup

# default KB sources
NYSP_CC_URL = "https://troopers.ny.gov/computer-crimes"

def fetch_public_text(url):
    try:
        r = requests.get(url, timeout=8)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        for s in soup(["script","style","nav","header","footer","aside"]):
            s.decompose()
        parts = [t.get_text(" ", strip=True) for t in soup.find_all(["h1","h2","h3","p","li"])]
        return "\n".join(p for p in parts if p)
    except Exception as e:
        return f"Error fetching page: {e}"

def build_kb():
    """
    Returns a simple corpus (list of dicts). Consumers can optionally compute embeddings.
    """
    nysp_text = fetch_public_text(NYSP_CC_URL)
    corpus = [
        {"id": "nysp_ccu", "text": nysp_text},
        {"id": "tips", "text": "Basic cybersecurity tips: enable MFA, use unique passwords, keep software updated, avoid suspicious links."}
    ]
    return corpus

def retrieve_snippets(query, corpus=None, k=2):
    """
    Simple retrieval: returns top-k corpus texts. If embeddings provided externally,
    replace with vector search. For prototype we return the most relevant by naive substring score.
    """
    if corpus is None:
        corpus = build_kb()
    # naive scoring: count substring occurrences
    q = (query or "").lower()
    scored = []
    for doc in corpus:
        text = (doc.get("text") or "").lower()
        score = text.count(q) if q else 0
        scored.append((score, doc))
    # fallback: if all scores zero, return the first k docs
    scored.sort(key=lambda x: x[0], reverse=True)
    results = [d for s, d in scored if s > 0]
    if not results:
        # fallback: return top k original docs
        return [doc for doc in corpus[:k]]
    return [d for d in results[:k]]

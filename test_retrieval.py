from nyspccu.retrieval import build_kb, retrieve_snippets

def test_build_kb_non_empty():
    corpus = build_kb()
    assert isinstance(corpus, list)
    assert len(corpus) >= 1

def test_retrieve_basic():
    corpus = build_kb()
    hits = retrieve_snippets("password", corpus, k=2)
    assert isinstance(hits, list)
    assert len(hits) >= 1

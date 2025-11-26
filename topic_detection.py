"""
Topic detection utilities for nyspccu-assistant.
Provides a robust is_on_topic() function and simple PII detection.
"""

import re
import numpy as np

# Conservative keyword lists
CYBER_KEYWORDS = [
    "cyber","security","malware","ransom","ransomware","phish","phishing","breach",
    "vulnerab","exploit","forensic","incident","mfa","2fa","password","credential",
    "ddos","botnet","encryption","vpn","report","scan","patch","update","intrusion",
    "investigate","mitigate","protect","secure"
]

INTENT_WORDS = [
    "how","how to","how do i","what do i","what should i","what to do","report",
    "detect","secure","protect","mitigate","scan","investigate","enable","configure",
    "setup","reporting","report a"
]

NEGATIVE_KEYWORDS = [
    "weather","movie","color","colour","song","music","food","recipe","sky","sport",
    "football","cricket","dance","joke","memes"
]

CYBER_RE = re.compile("|".join(re.escape(k) for k in CYBER_KEYWORDS), re.I)
INTENT_RE = re.compile("|".join(re.escape(k) for k in INTENT_WORDS), re.I)
NEG_RE = re.compile(r"\b(" + "|".join(re.escape(k) for k in NEGATIVE_KEYWORDS) + r")\b", re.I)

REFUSAL_MESSAGE = "I only answer cybersecurity-related questions (incidents, prevention, reporting, laws)."

# PII detection patterns (basic)
PII_PATTERNS = {
    "email": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "ssn": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
    "credit_card": re.compile(r"\b(?:\d[ -]*?){13,16}\b"),
    "phone": re.compile(r"\b(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{2,4}\)?[-.\s]?)?\d{3,4}[-.\s]?\d{3,4}\b")
}

def contains_pii(text):
    """
    Return dict of PII types found in text. Empty dict if none found.
    """
    hits = {}
    if not text:
        return hits
    for name, pat in PII_PATTERNS.items():
        if pat.search(text):
            hits[name] = True
    return hits

def is_on_topic(user_text, use_semantic=False, semantic_score=None, semantic_threshold=0.55):
    """
    Decide whether user_text is cybersecurity-related.
    Returns (on_topic_bool, details_dict).

    details_dict contains:
      - keyword: bool
      - intent: bool
      - negative: bool
      - semantic: bool (if use_semantic True)
      - sem_score: float or None
    """
    details = {"keyword": False, "intent": False, "negative": False, "semantic": False, "sem_score": None}

    if not user_text or not user_text.strip():
        return False, details

    txt = user_text.strip().lower()

    # Negative quick filter
    if NEG_RE.search(txt):
        details["negative"] = True
        return False, details

    # Keyword substring check
    for kw in CYBER_KEYWORDS:
        if kw in txt:
            details["keyword"] = True
            break

    # Intent heuristic
    if INTENT_RE.search(txt):
        details["intent"] = True

    # Semantic signal (if provided)
    if use_semantic and (semantic_score is not None):
        details["sem_score"] = float(semantic_score)
        if semantic_score >= semantic_threshold:
            details["semantic"] = True

    # Final decision: accept if any positive signal present
    on_topic = details["keyword"] or details["intent"] or details["semantic"]
    return bool(on_topic), details

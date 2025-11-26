"""
LLM adapter for optional OpenRouter integration.
This function is a small wrapper; the code expects OPENROUTER_API_KEY in the environment.
If no key is present, callers should use the retrieval fallback.
"""

import os
import requests

OPENROUTER_API = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_MODEL = "openrouter/auto"

def call_openrouter(prompt, temperature=0.12, max_tokens=150):
    key = os.getenv("OPENROUTER_API_KEY")
    if not key:
        return None
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    body = {
        "model": OPENROUTER_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    try:
        resp = requests.post(OPENROUTER_API, json=body, headers=headers, timeout=30)
        resp.raise_for_status()
        j = resp.json()
        # safe access
        return j.get("choices", [{}])[0].get("message", {}).get("content")
    except Exception as e:
        return None

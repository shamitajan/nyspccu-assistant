"""
nyspccu package - core interfaces for topic detection, retrieval, and LLM adapter.
"""

from .topic_detection import is_on_topic, contains_pii
from .retrieval import build_kb, retrieve_snippets
from .llm_adapter import call_openrouter

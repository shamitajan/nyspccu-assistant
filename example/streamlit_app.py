"""
Minimal Streamlit example that demonstrates the nyspccu package.
Run with: streamlit run examples/streamlit_app.py
"""

import streamlit as st
from nyspccu import is_on_topic, build_kb, retrieve_snippets, call_openrouter, contains_pii

st.set_page_config(page_title="NYSP CCU Assistant - Example", layout="wide")

st.title("NYSP CCU — Example Assistant (prototype)")
st.write("Informational only — not legal advice. Do not paste PII.")

if "corpus" not in st.session_state:
    st.session_state.corpus = build_kb()

q = st.text_input("Ask a cybersecurity question (e.g., 'How do I enable MFA?')")

if st.button("Send"):
    if not q:
        st.warning("Enter a question.")
    else:
        # check PII
        pii = contains_pii(q)
        if pii:
            st.error("Your message appears to contain sensitive personal data. Please remove PII and try again.")
        else:
            on_topic, details = is_on_topic(q)
            st.write("**On-topic decision:**", on_topic)
            st.write("**Decision details:**", details)
            if not on_topic:
                st.error("Refused: " + "I only answer cybersecurity-related questions.")
            else:
                corpus = st.session_state.corpus
                snippets = retrieve_snippets(q, corpus, k=2)
                ground = "\n\n".join([s["text"][:600] for s in snippets])
                # optional LLM
                prompt = f"Context:\n{ground}\n\nQuestion: {q}\nAnswer briefly (1-3 sentences)."
                answer = call_openrouter(prompt)
                if not answer:
                    answer = snippets[0]["text"].split(".")[0] + "."
                st.success(answer)

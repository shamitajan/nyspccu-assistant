# nyspccu-assistant  

**Short description**    
`nyspccu-assistant` is a prototype, retrieval-augmented, domain-restricted chatbot designed to provide concise informational guidance about cybercrime reporting and cyber hygiene, grounded in public materials from the New York State Police — Computer Crimes Unit (NYSP CCU).

**Status**    
Prototype. This repository contains a reusable Python package (`nyspccu`) and a simple Streamlit example.

## Quick start

1. Create and activate a Python 3.9+ virtual environment:  

  python -m venv .venv  
  source .venv/bin/activate   # macOS / Linux  
  .venv\Scripts\activate      # Windows (PowerShell)  

2. Install requirements:  
pip install -r requirements.txt

3. Run the example Streamlit app:  
streamlit run examples/streamlit_app.py

**Purpose and audience**  
This software is intended for researchers and engineers exploring domain-restricted conversational agents, safe RAG (retrieval-augmented generation) patterns, and prototypes for public-facing cybersecurity information systems. It is not an official NYSP service and should not be used to file reports or handle PII.

---
Title: "nyspccu-assistant: A domain-restricted retrieval-augmented chatbot for cybercrime awareness"
Authors:
  - Name: Shamita Jagarlamudi
    Affiliation: "1"  
  - Name: Soham Ghodake  
    Affiliation: "2"
Date: 26 November 2025
---

# Summary

nyspccu-assistant is a prototype software package that implements a domain-restricted conversational assistant for cybersecurity information and reporting guidance. The software connects a small curated knowledge base with a retrieval component and an optional LLM adapter to deliver concise and informational responses acquired from public materials from the New York State Police — Computer Crimes Unit (NYSP CCU). The package enforces strict topic constraints designed to refuse off-topic queries and avoid handling personal identifiable information (PII). The intended audience is researchers and practitioners exploring safe retrieval-augmented conversational systems for public-facing information services.

# Statement of need

Public-facing conversational systems that provide guidance about cybersecurity and reporting require strict safeguards to avoid offering legal advice or collecting PII. While general-purpose conversational agents are useful for many tasks, there is a need for lightweight, reproducible prototypes that demonstrate how domain restriction, retrieval-grounding, and optional LLM integration can be combined to produce safe, concise informational assistants. nyspccu-assistant provides a compact implementation of these design patterns, including: a multi-signal topic detection module, a simple retrieval pipeline, an optional LLM adapter, and a minimal example UI. The software is useful for researchers developing safe assistant designs, educators teaching RAG concepts, and practitioners prototyping public information tools.

# References

- New York State Police - Computer Crimes Unit. https://troopers.ny.gov/computer-crimes
- New York Penal Law Article 156 - Offenses Involving Computers. https://www.nycourts.gov/judges/cji/2-PenalLaw/156/156.05.pdf
- 18 U.S. Code § 1030 - Computer Fraud and Abuse Act (CFAA). https://law.cornell.edu/uscode/text/18/1030

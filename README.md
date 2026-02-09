Autonomous Insurance Claims Processing Agent

Overview

This project implements a lightweight autonomous agent that processes First Notice of Loss documents.

The system extracts key insurance fields, validates data completeness, applies deterministic routing rules, and produces a structured JSON decision output aligned with real world insurance workflows.

Architecture

1. Extractor module parses FNOL documents using deterministic pattern based extraction.
2. Router module applies business rules to classify and route claims.
3. Utility layer supports PDF ingestion and text normalization.
4. Main orchestrator coordinates the end-to-end processing pipeline.

Routing Logic

1. If any mandatory field is missing, the claim is routed to Manual Review.
2. If suspicious keywords such as fraud, inconsistent, or staged are detected, the claim is flagged for Investigation.
3. Injury related claims are routed to a Specialist Queue.
4. Claims with estimated damage below 25000 are Fast Tracked.
5. All other claims follow Standard Processing.

Prerequisites

Python 3.9 or higher
macOS or Windows

Setup and Execution

1. Open a terminal and navigate to the project root directory.

2. Create a virtual environment.
   python3 -m venv venv

3. Activate the virtual environment.
   source venv/bin/activate

4. Install dependencies.
   pip install PyPDF2

5. Run the agent using the sample FNOL document.
   python src/main.py

Output

The program prints a JSON object to the console containing:

Extracted insurance fields,
List of missing mandatory fields,
Recommended routing decision,
Clear reasoning for the decision.

Design Notes

This project intentionally uses deterministic extraction and rule based routing to ensure explainability, auditability, and compliance with insurance domain requirements. The modular structure allows easy extension to NLP based extraction, API integration, or workflow orchestration systems.


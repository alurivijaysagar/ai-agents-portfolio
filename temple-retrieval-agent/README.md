# Temple Retrieval Assistant
A retrieval-based AI assistant that answers questions about ancient temples 
using structured data and the Gemini API.

## Overview
This project implements a RAG-style (Retrieval Augmented Generation) workflow. 
Instead of relying solely on the AI's training data, it retrieves structured 
temple information from a local dataset and injects it into the model's context 
for accurate, grounded responses.

**Currently supports:**
- Sri Venkateswara Swamy Temple, Tirupati
- Meenakshi Sundareswarar Temple, Madurai

## Tech Stack
- Python
- Google Gemini API
- Retrieval Augmented Generation (RAG)
- Prompt Engineering

## How It Works
1. User asks a question about a temple
2. System searches structured data for a matching temple
3. Matched temple data is injected into the model's prompt
4. Gemini generates a response grounded in the retrieved data

## How to Run
1. Clone the repository
2. Install dependencies: `pip install google-generativeai`
3. Add your Gemini API key
4. Run: `python google_api_temple.py`

## Key Concepts Demonstrated
- Retrieval Augmented Generation (RAG)
- Function modularization
- Nested dictionary traversal
- Context injection into LLM prompts
- Failure handling for unmatched queries

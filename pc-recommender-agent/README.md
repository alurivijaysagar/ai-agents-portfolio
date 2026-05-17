# PC Recommender Multi-Agent System
A dual-agent AI system that recommends and refines PC builds based on 
user preferences, built using Python and the Gemini API.

## Overview
This project uses two specialized AI agents working in sequence to deliver 
high quality PC build recommendations.

**Agent Pipeline:**
- Recommender Agent → suggests PC builds based on budget and use case
- Reviewer Agent → critically evaluates and refines the recommendation

The reviewer agent checks for compatibility issues, pricing accuracy, 
and component balance before delivering the final answer.

## Tech Stack
- Python
- Google Gemini API
- Multi-Agent Workflow Design
- Prompt Engineering

## How It Works
1. User inputs budget, use case, and preferences
2. Agent 1 generates a detailed PC build recommendation
3. Agent 2 receives Agent 1's output and critically refines it
4. Final refined recommendation is delivered to the user

## How to Run
1. Clone the repository
2. Install dependencies: `pip install google-generativeai`
3. Add your Gemini API key
4. Run: `python google_api_multiple_agents.py`

## Key Concepts Demonstrated
- Multi-agent review pipeline
- Critical evaluation and refinement
- Context passing between agents
- Prompt engineering for specialized roles

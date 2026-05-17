# Multi-Agent Fitness Assistant
An AI-powered fitness planning system built using Python and the Gemini API, 
demonstrating a 3-stage multi-agent pipeline.

## Overview
This project implements a multi-agent AI workflow where three specialized 
agents collaborate to deliver personalized fitness guidance.

**Agent Pipeline:**
- Goal Analysis Agent → collects body metrics and fitness goals
- Workout Coach Agent → generates personalized training plans
- Dietician Agent → builds diet plans based on workout output

Each agent has a focused responsibility and automatically passes context 
to the next stage — no manual intervention required.

## Tech Stack
- Python
- Google Gemini API
- Prompt Engineering
- Multi-Agent Workflow Design

## How It Works
1. User inputs body metrics and fitness goals
2. Agent 1 analyzes the input and structures the goal
3. Agent 2 receives Agent 1's output and creates a workout plan
4. Agent 3 receives Agent 2's output and generates a diet plan

## How to Run
1. Clone the repository
2. Install dependencies: `pip install google-generativeai`
3. Add your Gemini API key
4. Run: `python google_api_workout_manager.py`

## Key Concepts Demonstrated
- Multi-agent orchestration
- Context passing between agents
- Prompt engineering for specialized roles
- API integration with Gemini

# Agentic AI System Evaluation Report

## Project Overview

This project implements a simple agentic AI system using:

- Python
- Gemini API
- Tool-based reasoning
- Langfuse observability

The agent decides which tool to use before answering a question.

Available tools:

- calculator
- search_knowledge
- current_time


## Agent Architecture

User Query
↓
Agent Controller
↓
LLM Decision
↓
Tool Selection
↓
Tool Execution
↓
Observation
↓
Final Answer


## Evaluation Method

To verify agent behavior, a dataset of test queries was created.

The dataset contains different categories:

Math Queries  
Knowledge Queries  
Time Queries  
Invalid / Adversarial Queries


Each query includes an **expected tool**.

The evaluation script runs the agent and compares:

expected_tool vs actual_tool


## Metrics Used

Tool Selection Accuracy

correct_tool_predictions / total_queries

Task Success Rate

successful_responses / total_queries

Failure Detection

cases where agent chose wrong tool


## Example Results

| Query | Expected Tool | Actual Tool | Success |
|------|------|------|------|
| what is 12*15 | calculator | calculator | True |
| explain docker | search_knowledge | search_knowledge | True |
| what time is it | current_time | current_time | True |
| calculate kubernetes | invalid | search_knowledge | False |


## Failure Cases Observed

Common failure scenarios:

- ambiguous queries
- nonsensical inputs
- tool misuse


Example:

Query:
calculate kubernetes

Expected:
invalid

Actual:
search_knowledge


## Improvements

Possible improvements include:

- better input validation
- improved tool selection prompts
- confidence scoring
- LLM-as-judge evaluation


## Conclusion

This evaluation framework helps verify that the agent follows the correct reasoning path.

It also enables statistical analysis of agent performance and detection of failure modes.

This approach aligns with modern evaluation techniques used in agentic AI systems.
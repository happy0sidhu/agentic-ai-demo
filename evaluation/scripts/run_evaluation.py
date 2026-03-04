import sys
import os
import csv

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(PROJECT_ROOT)

from agent.agent_controller import run_agent


INPUT_FILE = os.path.join(PROJECT_ROOT, "evaluation/dataset/test_queries.csv")
OUTPUT_FILE = os.path.join(PROJECT_ROOT, "evaluation/metrics/evaluation_results.csv")


def detect_tool_used(agent_output):
    """
    Very simple heuristic detection.
    In a real system you would parse tool logs or traces.
    """

    output = str(agent_output).lower()

    if any(x in output for x in ["*", "+", "-", "/", "result"]):
        return "calculator"

    if any(x in output for x in ["docker", "kubernetes", "api"]):
        return "search_knowledge"

    if "time" in output:
        return "current_time"

    return "unknown"


def run_evaluation():

    results = []

    with open(INPUT_FILE, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:

            query = row["query"]
            expected_tool = row["expected_tool"]

            print("\nRunning query:", query)

            answer = run_agent(query)

            actual_tool = detect_tool_used(answer)

            success = actual_tool == expected_tool

            results.append({
                "query": query,
                "expected_tool": expected_tool,
                "actual_tool": actual_tool,
                "success": success
            })

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:

        fieldnames = ["query", "expected_tool", "actual_tool", "success"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for r in results:
            writer.writerow(r)

    print("\nEvaluation complete.")
    print("Results saved to:", OUTPUT_FILE)


if __name__ == "__main__":
    run_evaluation()
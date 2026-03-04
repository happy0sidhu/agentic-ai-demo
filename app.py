from agent.agent_controller import run_agent

question = input("Ask the agent a question: ")

result = run_agent(question)

print("\nFinal Answer:")
print(result)
import json

from utils.llm_client import ask_llm
from utils.prompt_loader import load_agent_prompt
from agent.tools_registry import get_tool
from utils.langfuse_client import langfuse


def clean_llm_response(response: str):
    """
    Remove markdown wrappers from LLM JSON output.
    """

    cleaned = response.strip()

    if cleaned.startswith("```"):
        cleaned = cleaned.split("```")[1]

    if cleaned.startswith("json"):
        cleaned = cleaned[4:]

    cleaned = cleaned.strip()

    return cleaned


def run_agent(user_query):

    # log agent start
    langfuse.create_event(
        name="agent_start",
        input={"question": user_query},
    )

    base_prompt = load_agent_prompt()

    context = f"User question: {user_query}\n"

    while True:

        full_prompt = base_prompt + "\n" + context

        # log LLM prompt
        langfuse.create_event(
            name="llm_prompt",
            input=full_prompt,
        )

        response = ask_llm(full_prompt)

        print("\nLLM Response:")
        print(response)

        # log LLM response
        langfuse.create_event(
            name="llm_response",
            output=response,
        )

        clean_response = clean_llm_response(response)

        try:
            decision = json.loads(clean_response)
        except Exception as e:
            print("JSON parsing error:", e)
            return "Agent returned invalid JSON."

        action = decision.get("action")

        if action == "final":

            final_answer = decision.get("answer")

            # log final answer
            langfuse.create_event(
                name="agent_final_answer",
                output=final_answer,
            )

            return final_answer

        elif action == "tool":

            tool_name = decision.get("tool_name")
            tool_input = decision.get("tool_input")

            tool_function = get_tool(tool_name)

            if tool_function is None:
                return f"Unknown tool: {tool_name}"

            try:
                result = tool_function(tool_input)
            except TypeError:
                result = tool_function()

            print("\nTool Result:", result)

            # log tool usage
            langfuse.create_event(
                name="tool_execution",
                metadata={
                    "tool": tool_name,
                    "input": tool_input,
                    "result": result,
                },
            )

            context += f"\nTool used: {tool_name}\n"
            context += f"Tool input: {tool_input}\n"
            context += f"Tool result: {result}\n"

        else:
            return "Unknown agent action."
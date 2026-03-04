from agent.tools_registry import format_tool_descriptions


def load_agent_prompt():

    with open("prompts/agent_prompt.txt", "r") as file:
        prompt_template = file.read()

    tools_text = format_tool_descriptions()

    final_prompt = prompt_template.replace("{tools}", tools_text)

    return final_prompt



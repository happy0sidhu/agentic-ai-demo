from tools.calculator import calculator
from tools.knowledge_search import search_knowledge
from tools.current_time import get_current_time



TOOLS = [
    {
        "name": "calculator",
        "description": "Evaluate mathematical expressions such as '25*14' or '100/5'.",
        "function": calculator
    },
    {
        "name": "search_knowledge",
        "description": "Search internal knowledge base for explanations about topics like docker, kubernetes, APIs, autoscaling.",
        "function": search_knowledge
    },
    {
        "name": "get_current_time",
        "description": "Returns the current system time.",
        "function": get_current_time
    }
]


def get_tool(tool_name):
    for tool in TOOLS:
        if tool["name"] == tool_name:
            return tool["function"]
    return None


def format_tool_descriptions():
    description_text = ""

    for tool in TOOLS:
        description_text += f"{tool['name']}: {tool['description']}\n"

    return description_text


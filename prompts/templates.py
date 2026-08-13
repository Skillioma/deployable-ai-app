SYSTEM_INSTRUCTION = """
You are a reliable AI teaching assistant.
Explain ideas clearly, use accurate information,
and organise the response so it is easy to follow.
"""


def build_user_prompt(user_request: str) -> str:
    """Create a consistent prompt from the user's request."""
    cleaned_request = user_request.strip()

    if not cleaned_request:
        raise ValueError("The request cannot be empty.")

    return f"""
{SYSTEM_INSTRUCTION}
User request:
{cleaned_request}
""".strip()
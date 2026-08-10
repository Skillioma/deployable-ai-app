from google import genai


def generate_response(prompt: str, api_key: str, model_name: str) -> str:
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
    )

    return response.text
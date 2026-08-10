import os
from dataclasses import dataclass


MODEL_NAME = "gemini-2.0-flash"


@dataclass(frozen=True)
class Settings:
    gemini_api_key: str
    model_name: str = MODEL_NAME


def load_settings() -> Settings:
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not configured."
        )

    return Settings(gemini_api_key=api_key)
import pytest

from prompts.templates import build_user_prompt


def test_build_user_prompt_includes_request():
    request = "Explain solar energy."

    prepared_prompt = build_user_prompt(request)

    assert request in prepared_prompt


def test_build_user_prompt_rejects_empty_input():
    with pytest.raises(ValueError):
        build_user_prompt("   ")
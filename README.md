# Professional AI Application

## Overview

A Streamlit-based AI application that sends structured prompts to Gemini and displays the generated response through a simple user interface.

The application separates the user interface, AI service logic, and prompt construction to keep the code organized and maintainable.

## Features

- Streamlit-based user interface
- Gemini API integration
- Structured prompt construction
- Dedicated AI service layer
- Environment-based API key configuration
- Automated tests with pytest
- Separation of application logic from the user interface

## Project Structure

```text
professional_ai_app/
│
├── app.py
│
├── services/
│   └── ai_service.py
│
├── prompts/
│   └── templates.py
│
├── tests/
│   └── test_app.py
│
├── .streamlit/
│   └── secrets.toml
│
├── requirements.txt
├── .gitignore
└── README.md
```

### File and Folder Responsibilities

| File / Folder | Responsibility |
|---|---|
| `app.py` | Streamlit user interface and application entry point |
| `services/` | Application and AI service logic |
| `services/ai_service.py` | Handles communication with the Gemini API |
| `prompts/` | Stores prompt construction and templates |
| `prompts/templates.py` | Defines the application's structured prompt templates |
| `tests/` | Contains automated tests |
| `.streamlit/` | Local Streamlit configuration and secrets |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

## Setup

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Install the dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

The application requires a Gemini API key.

Set the following secret in your local environment:

```text
GEMINI_API_KEY=your_api_key_here
```

Set the value privately — **never place the real API key in the README or commit it to the repository.**

If using Streamlit secrets, store the key in:

```text
.streamlit/secrets.toml
```

Example:

```toml
GEMINI_API_KEY = "your_api_key_here"
```

The actual secret file should remain excluded from version control.

## Run the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```


## Run Tests

Run the automated tests with:

```bash
pytest
```

A successful test run confirms that the project's automated checks are passing.

## Security Notes

- Never commit API keys or other credentials to the repository.
- Never place the real `GEMINI_API_KEY` in `README.md`.
- Keep local secrets in the appropriate environment or Streamlit secrets configuration.
- Ensure secret files are included in `.gitignore`.
- Do not expose API credentials in source code, screenshots, or documentation.

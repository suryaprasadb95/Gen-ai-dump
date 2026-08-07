"""Run a sample Gemini prompt using the Google Generative AI Python client."""

import os
import sys

try:
    import google.generativeai as genai
except ImportError:
    raise ImportError(
        "google-generativeai is required. Install it with: python -m pip install google-generativeai"
    )


def main():
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Please set the GOOGLE_API_KEY environment variable.")
        sys.exit(1)

    genai.configure(api_key=api_key)

    # Initialize the model
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = (
        "Write a friendly welcome message for a developer who is starting a new Python project."
    )

    # Call generate_content on the model instance
    response = model.generate_content(prompt)

    print("=== Gemini Prompt ===")
    print(prompt)
    print("\n=== Gemini Response ===")
    print(response.text)


if __name__ == "__main__":
    main()
# pip install google-generativeai
# or pipx install google-generativeai --include-deps
# Set or replace the GOOGLE_API_KEY environment variable to your API key
# Run the script using python gem.py or ~/.local/share/pipx/venvs/google-generativeai/bin/python gem.py
# export GOOGLE_API_KEY="YOURAPIKEY"

import google.generativeai as genai
import os
import sys

try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
except KeyError:
    print("Error: API_KEY not set.")
    sys.exit(1)

default_model = "gemini-2.5-flash-preview-05-20"

try:
    model = genai.GenerativeModel(default_model)
    chat = model.start_chat(history=[])
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

while True:
    try:
        user_input = input(">")
        if user_input.lower() == 'exit':
            break
        response = chat.send_message(user_input)
        print(response.text)
    except Exception as e:
        print(f"Error: {e}")

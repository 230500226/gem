# pip install google-generativeai
# or pipx install google-generativeai --include-deps (arch)
# Replace YOURAPIKEY with yeah then
# Run the script using python gem.py 
import google.generativeai as genai
import os
import sys

genai.configure(api_key="YOURAPIKEY")

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

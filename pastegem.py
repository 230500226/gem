import google.generativeai as genai
import os
import sys

# Replace "YOURAPIKEY" with your actual Google API key
genai.configure(api_key="YOURAPIKEY")

default_model = "gemini-2.0-flash"

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

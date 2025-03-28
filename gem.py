# install generativeai package using pip
# pip install google-generativeai
# Set or replace the GOOGLE_API_KEY environment variable to your API key
# Run the script using python gem.py
# default model is 2, 2.0-flash

import google.generativeai as genai
import os
import sys

try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
except KeyError:
    print("Error: GOOGLE_API_KEY environment variable not set.")
    sys.exit(1)

model_options = {
    "1": "gemini-2.5-pro-exp-03-25",
    "2": "gemini-2.0-flash",
    "3": "gemini-2.0-flash-lite",
    "4": "gemini-1.5-flash",
    "5": "gemini-1.5-flash-8b",
    "6": "gemini-1.5-pro",
    "7": "gemini-embedding-exp",
    "8": "imagen-3.0-generate-002",
}

print("Available databases:")
for key, model_name in model_options.items():
    print(f"choose 1 to 8 default 2")

while True:
    choice = input("Enter the number of the model you want to use (or 'exit'): ")
    if choice.lower() == "exit":
        sys.exit(0)
    if choice in model_options:
        selected_model = model_options[choice]
        break
    else:
        print("Invalid choice. Please enter a number from the list.")

try:
    model = genai.GenerativeModel(selected_model)
    chat = model.start_chat(history=[])
except Exception as e:
    print(f"Error initializing model: {e}")
    sys.exit(1)

while True:
    try:
        user_input = input("ihr")
        if user_input.lower() == 'exit':
            break
        response = chat.send_message(user_input)
        print("res", response.text)
    except Exception as e:
        print(f"err: {e}")

print("conc.")

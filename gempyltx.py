import google.generativeai as genai
import os
import sys

def get_api_key():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not set in environment.")
        sys.exit(1)
    return api_key

def summarize_text(input_path, output_path, default_model="gemini-2.0-flash"):
    genai.configure(api_key=get_api_key())
    try:
        model = genai.GenerativeModel(default_model)
        chat = model.start_chat(history=[])
    except Exception as e:
        print(f"Error initializing Gemini: {e}")
        sys.exit(1)

    # Read input file
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        print(f"Error reading input file: {e}")
        sys.exit(1)

    # Ask Gemini to summarize, with ltxvideo prompt formatting
    prompt = (
        "Summarize the following transcript. "
        "Format the summary as a concise, direct prompt suitable for ltxvideo's video generation. "
        "Include clear scene descriptions, actions, and style, but do not reproduce full dialog. "
        "Transcript:\n" + text
    )

    try:
        response = chat.send_message(prompt)
        summary = response.text
    except Exception as e:
        print(f"Error communicating with Gemini: {e}")
        sys.exit(1)

    # Write summary to output file
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(summary)
        print(f"Summary written to {output_path}")
    except Exception as e:
        print(f"Error writing output file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python gemini.py input.txt output.txt")
        sys.exit(1)
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    summarize_text(input_path, output_path)

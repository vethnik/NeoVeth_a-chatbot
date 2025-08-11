import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load values from .env file

key = os.getenv("GEMINI_API_KEY")  # Get key from .env



# Configure Gemini
genai.configure(api_key=key)

# Store chat history
messages = []

# Choose the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

def completion(message):
    global messages
    messages.append({"role": "user", "parts": [message]})

    # Generate response
    chat = model.start_chat(history=messages)
    response = chat.send_message(message)

    # Save assistant's reply to history
    messages.append({"role": "model", "parts": [response.text]})

    print(f"NeoVeth: {response.text}")

if __name__ == "__main__":
    print("NeoVeth: hi i am NeoVeth ,a chatbot\n")
    while True:
        user_question = input("user: ")
        completion(user_question)

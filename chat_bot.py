# Chatbot Basic
# Description: Simple Python chatbot that responds to user input.

from datetime import datetime
import random

print("Hello! I'm Chatbot Basic 2.0 by Esen Tilenbaev.")
print("Type 'bye' to end the chat.\n")

responses = {
    "greeting": [
        "Hey there!",
        "Hello! How’s your day going?",
        "Hi! Nice to see you!",
        "Hey! What's up?"
    ],
    "how_are_you": [
        "I'm just code, but I'm doing great.",
        "Feeling good, thanks for asking.",
        "I’m fine. How about you?"
    ],
    "name": [
        "I'm Chatbot Basic, made by Esen.",
        "People call me Chatbot Basic."
    ],
    "weather": [
        "I'm not connected to weather APIs yet.",
        "Probably nice weather today."
    ],
    "time": [
        f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    ],
    "age": [
        "I'm ageless, but I was created in 2025.",
        "Time doesn’t affect me."
    ],
    "default": [
        "I don't quite understand.",
        "Can you say that differently?",
        "Interesting. Tell me more.",
        "I'm still learning."
    ]
}

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye! Have a nice day.")
        break

    elif any(word in user_input for word in ["hi", "hey", "hello", "hola", "sup"]):
        print("Chatbot:", random.choice(responses["greeting"]))

    elif "how are you" in user_input or "how r u" in user_input:
        print("Chatbot:", random.choice(responses["how_are_you"]))

    elif "your name" in user_input or "who are you" in user_input:
        print("Chatbot:", random.choice(responses["name"]))

    elif "weather" in user_input:
        print("Chatbot:", random.choice(responses["weather"]))

    elif "time" in user_input:
        print("Chatbot:", random.choice(responses["time"]))

    elif "age" in user_input or "old" in user_input:
        print("Chatbot:", random.choice(responses["age"]))

    else:
        print("Chatbot:", random.choice(responses["default"]))

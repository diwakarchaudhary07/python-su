import random

# Simple responses dictionary
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm doing great!", "Feeling awesome!", "I'm here to help you!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["Sorry, I didn't understand that.", "Can you rephrase?", "Hmm, interesting!"]
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

def main():
    print("🤖 AI Chatbot (Trend Project 2026)")
    print("Type 'bye' to exit.\n")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("Bot:", random.choice(responses["bye"]))
            break
        print("Bot:", chatbot_response(user_input))

if __name__ == "__main__":
    main()

def chatbot():
    print("=== BASIC CHATBOT ===")
    print("Type 'bye' to exit.")

    while True:
        user = input("You: ").lower().strip()

        if user == "hello" or user == "hi":
            print("Bot: Hi! How are you?")

        elif user == "how are you":
            print("Bot: I am fine, thank you!")

        elif user == "what is your name":
            print("Bot: I am a simple Python chatbot.")

        elif user == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")


chatbot()
import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm doing great! How about you?",]
    ],
    [
        r"sorry (.*)",
        ["No problem, please don't apologize.",]
    ],
    [
        r"quit",
        ["Bye! Take care. :)", "Goodbye! Have a great day!"]
    ],
]

# Create a Chatbot with pairs and reflections
def chatbot():
    print("Hi! I'm a simple chatbot. How can I assist you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()

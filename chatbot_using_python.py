# SYNC Interns - Task 4 - Build Your Own Chatbot Using Python 

import random
import nltk
from nltk.chat.util import Chat, reflections


patterns = [
    (r'hi|hello|hey', ['Hi there!', 'Hello!', 'Hey!', 'Hi! How can I help you?']),
    (r'bye|goodbye', ['Goodbye!', 'Bye!', 'See you later!']),
    (r'what is your name?', ['I am a chatbot.', 'You can call me Chatbot.', 'My name is Chatbot.']),
    (r'my name is (.*)', ['Nice to meet you, {}!', 'Hello, {}!', 'Hi, {}!']),
    (r'how are you?', ['I am good, thank you!', 'I am doing well.', 'I feel great!']),
    (r'(.*) (hungry|thirsty)', ['I am just a chatbot, so I do not get hungry or thirsty.']),
    (r'(.*) (love|like) (.*)', ['I am glad to hear that!', 'That is great!', 'Awesome!']),
    (r'(.*)', ["I'm sorry, but I can't understand that. Could you please rephrase?", 'I am not sure about that.', 'I am still learning.']),
]

chatbot = Chat(patterns, reflections)

def main():
    print("Chatbot: Hi there! I'm a simple chatbot. You can type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ").lower()
        if user_input == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()

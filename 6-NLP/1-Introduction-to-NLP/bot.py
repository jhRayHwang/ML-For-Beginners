import random

random_responses = ["That is quite interesting, please tell me more.",
                    "I see. Do go on.",
                    "Why do you say that?",
                    "Funny weather we've been having, isn't it?",
                    "Let's change the subject.",
                    "Did you catch the game last night?"]


#Print instructions advising the user how to interact with the bot
print("Hello! I am a simple chatbot. You can talk to me and I will respond with some generic phrases. Type 'exit' to end the conversation.")

#Starting a simple loop
while(True):
    #Accept user input
    user_input = input("You: ")
    
    #Check if the user wants to exit
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye! It was nice talking to you.")
        break
    
    #Process user input and determine response
    response = random.choice(random_responses)
    
    #Print response
    print("Chatbot:", response)

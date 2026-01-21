'''
Print instructions advising the user how to interact with the bot
Start loop
Accept user input
If user has asked to exit, then exit
Process user input and determine appropriate sentiment response
If a noun phrase is detected in the sentiment, pluralize it and ask for more input on that topic
Print response
loop back to step 2
'''

import random
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor                                  
extractor = ConllExtractor()


def main():
    print("Hello! I am a simple chatbot.")
    print("You can talk to me and I will respond with some generic phrases.")
    print("Type 'exit' to end the conversation.")

    #Starting a simple loop
    while(True):
        #Accept user input
        user_input = input("> ")
        
        #Check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! It was nice talking to you.")
            break

        else:
            user_input_blob = TextBlob(user_input, np_extractor=extractor)
            np = user_input_blob.noun_phrases  
            response = ""

            if user_input_blob.polarity <= -0.5:
                response = "Oh dear, that sounds bad. "
            elif user_input_blob.polarity <= 0:
                response = "Hmm, that's not great. "
            elif user_input_blob.polarity <= 0.5:
                response = "Well, that sounds positive. "
            elif user_input_blob.polarity <= 1:
                response = "Wow, that sounds great. "

            if len(np) != 0:
                # There was at least one noun phrase detected, so ask about that and pluralise it
                # e.g. cat -> cats or mouse -> mice
                response = response + "Can you tell me more about " + np[0].pluralize() + "?"
            else:
                response = response + "Can you tell me more?"

            print("Chatbot:", response)

    print("It was nice talking to you, goodbye!")

main()

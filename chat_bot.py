import random

responses={
    "hi":["Hello!","Hi how are you ?"," hey !"],
    "how are you":["I am fine","I am doing good","I am grate"],
    "what is your name":["I am chatbot","My name is chatbot","i dont have name you can call me bot"],
    "bye":["Bye","See you later","goodbye"],
    "default":["i cant understand","can you repeat it","can you rephrase it ?"]
    }
    
def chat_bot_response(user_input):
    user_input=user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
        return random.choice(responses['default'])    
        
def chat():
    print("Hi how are you,i am a chatbot,Type bye to exit")
    while True:
        user_input=input("You:")
        if user_input.lower()=='bye':
            print("ChatBot : Goodbye")
            break
        response=chat_bot_response(user_input)
        print(f"Chatbot :{response}")
        
chat()        
            

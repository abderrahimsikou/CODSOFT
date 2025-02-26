def chatbot(user_input):
    user_input = user_input.lower()
    
    if 'hello' in user_input or 'hi' in user_input:
        return 'hello! how can i help you today?'
    
    elif 'how are you doing?' in user_input:
        return 'am fine, thank you.what about you?'
    
    elif 'what is your age?' in user_input:
        return "I'm a compuetr progarm dude,seriously you are asking me this?"
    
    elif 'what is your name?' in user_input:
        return 'am simple chatbot, i can help you in simple question!'
    
    elif 'what is your best sport or game?' in user_input:
        return "i'm a very big fan of football"
    
    elif 'bye' in user_input or 'good bye' in user_input:
        return 'it was nice talking to you. see you soon'
    
    else:
        return "sorry, i don't understand your question.try again!"
    
while True:
    user_text = input('You:')
    if user_text.lower() in ['done']:
        print('thank you! good bye.')
    
    respone = chatbot(user_text)
    print('chatbot:',respone)
from flask import Flask, request, jsonify
from flask import Flask, render_template, request
import requests
from recommend import recommend_outlet
from text import give_intent
import aiml
import os
import nltk
from connection import insert_chat
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag

kernel = aiml.Kernel()
aiml_path = os.path.join(os.path.dirname(__file__), 'chatbot.aiml') 
kernel.learn(aiml_path)

app = Flask(__name__)

# Define the route handler for the root URL
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.form['message']
    sentences = sent_tokenize(user_message)

    imp_words = []
    for sentence in sentences:
        words = word_tokenize(sentence)
        tagged_words = pos_tag(words)
        named_entities = nltk.ne_chunk(tagged_words)
        for subtree in named_entities.subtrees():
            if subtree.label() == 'GPE':
                city = ' '.join([token[0] for token in subtree.leaves()])
                imp_words.append(city)
        
        for entity in named_entities:
            if hasattr(entity, 'label') and (entity.label() == 'PERSON' or entity.label() == 'CITY' ):
                imp_words.append(' '.join([leaf[0] for leaf in entity.leaves()]))

    new_input = give_intent(user_message)
    
    if len(imp_words)==0:
        chatbot_response = process_user_input(new_input)
    else:
        chatbot_response = process_user_input(new_input+" "+imp_words[0])
    if user_message and chatbot_response:
        if insert_chat(user_message,chatbot_response):
            print("success")
        else:
            print("try again")
    return chatbot_response

def process_user_input(user_input):
    if len(user_input)==0 :
        return "Don't feel like writing?"
    elif 'weather' in user_input:
        city=""
        for i in range(8,len(user_input)):
            city+=user_input[i]
        weather = get_weather(city)
        temp= weather["temp"]
        humidity = weather["humidity"]
        conditions = weather["conditions"]
        aiml_response = f"The Temperature in {city} is {temp}°C, humidity is {humidity}% and the conditions are {conditions}"
    elif 'recommend' in user_input:
        print('yo')
    else:
        aiml_response = kernel.respond(user_input)
    return aiml_response
    
def get_weather(city):
    api_key = 'e1e2b866e6b4202b06ab18c39542e37e'  # Replace with your OpenWeatherMap API key

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    weather = {
        'city': data['name'],
        'temp': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'conditions': data['weather'][0]['description']
    }

    return weather


if __name__ == '__main__':
    app.run()
app.debug = True
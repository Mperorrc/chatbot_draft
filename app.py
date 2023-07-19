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
from cities import get_cities

kernel = aiml.Kernel()
aiml_path = os.path.join(os.path.dirname(__file__), 'chatbot.aiml') 
kernel.learn(aiml_path)

app = Flask(__name__)
app.config["recommendation_system_on"]=0
app.config["recommend_system_values"]={
    "food_type":"",
    "food_style":"",
    "check":"",
    "location":"",
    "budget":"",
    "outlet_type":"",
}

# Define the route handler for the root URL
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.form['message']
    sentences = sent_tokenize(user_message)
    cities = get_cities(user_message)
    imp_words=[]
    for sentence in sentences:
        words = word_tokenize(sentence)
        tagged_words = pos_tag(words)
        named_entities = nltk.ne_chunk(tagged_words)
        
        for entity in named_entities:
            if hasattr(entity, 'label') and (entity.label() == 'PERSON' or entity.label() == 'CITY' ):
                imp_words.append(' '.join([leaf[0] for leaf in entity.leaves()]))
    new_input = give_intent(user_message)
    
    if (len(imp_words)==0 and len(cities)==0):
        chatbot_response = process_user_input(new_input)
    elif (not (app.config["recommendation_system_on"] and (new_input!="beverage" or new_input!="maggi" or new_input!="meals" or new_input!="fast-food" or new_input!="sandwich" or new_input!="maggi" or new_input!="cheap" or new_input!="expensive" or new_input!="vegetarian" or new_input!="non-vegetarian" or new_input!="mess-1" or new_input!="mess-2" or new_input!="academic-blocks" or new_input!="multiple" or new_input!="one" or new_input!="sit-down" or new_input!="takeaway"))):
        if (len(cities)>0 and new_input=='weather'):
            chatbot_response = process_user_input(new_input+" "+cities[0])
        elif len(imp_words)>0:    
            chatbot_response = process_user_input(new_input+" "+imp_words[0])
        else:
            chatbot_response = process_user_input(new_input)
    else:
        chatbot_response = process_user_input(new_input)
    if user_message and chatbot_response:
        if insert_chat(user_message,chatbot_response):
            print("success")
        else:
            print("try again")
    return chatbot_response

def process_user_input(user_input):
    if len(user_input)==0 :
        return "Don't feel like writing?"
    elif 'recommend' in user_input:
        if app.config["recommendation_system_on"]>0:
            aiml_response="Sure, I'm here to assist you with food recommendations. Could you please provide an answer to that question?"
        else:
            app.config["recommendation_system_on"]+=1
            aiml_response = kernel.respond(user_input)
    elif app.config["recommendation_system_on"]==1:
        if(("beverage" in user_input) or ("meals" in user_input) or ("maggi" in user_input) or ("fast-food" in user_input) or ("sandwich" in user_input )):
            print("hmm ok")
            app.config["recommend_system_values"]["food_style"] = user_input
            app.config["recommendation_system_on"]+=1
            aiml_response = kernel.respond(user_input)
        elif "exit":
            app.config["recommendation_system_on"]=0
            aiml_response = kernel.respond(user_input)
        else:
            aiml_response="Could you please provide an answer to the previous question?"
    elif app.config["recommendation_system_on"]==2:
        if(("cheap" in user_input) or ("expensive" in user_input)):
            app.config["recommend_system_values"]["budget"] = user_input
            app.config["recommendation_system_on"]+=1
            aiml_response = kernel.respond(user_input)
        elif "exit":
            app.config["recommendation_system_on"]=0
            aiml_response = kernel.respond(user_input)
        else:
            aiml_response="Could you please provide an answer to the previous question?"
    elif app.config["recommendation_system_on"]==3:
        if(("one" in user_input) or ("multiple" in user_input)):
            app.config["recommend_system_values"]["check"] = user_input
            app.config["recommendation_system_on"]+=1
            aiml_response = kernel.respond(user_input)
        elif "exit":
            app.config["recommendation_system_on"]=0
            aiml_response = kernel.respond(user_input)
        else:
            aiml_response="Could you please provide an answer to the previous question?"
    elif app.config["recommendation_system_on"]==4:
        if(app.config["recommend_system_values"]["check"]=="one" and (("mess-1" in user_input) or ("mess-2" in user_input) or ("academic-blocks" in user_input))):
            app.config["recommend_system_values"]["location"] = user_input
            app.config["recommendation_system_on"]+=1
            aiml_response = kernel.respond(user_input)
        elif(app.config["recommend_system_values"]["check"] == "multiple" and (("vegetarian" in user_input) or ("non-vegetarian" in user_input))):
            app.config["recommend_system_values"]["food_type"] = user_input
            app.config["recommendation_system_on"]+=1
            aiml_response = kernel.respond(user_input)
        elif "exit":
            app.config["recommendation_system_on"]=0
            aiml_response = kernel.respond(user_input)
        else:
            aiml_response="Could you please provide an answer to the previous question?"
    elif app.config["recommendation_system_on"]==5:
        if(app.config["recommend_system_values"]["check"]=="one" and (("vegetarian" in user_input) or ("non-vegetarian" in user_input))):
            app.config["recommend_system_values"]["food_type"] = user_input
            app.config["recommendation_system_on"]+=1
            aiml_response = kernel.respond(user_input)
        elif(app.config["recommend_system_values"]["check"] == "multiple" and (("sit-down" in user_input) or ("takeaway" in user_input))):
            app.config["recommend_system_values"]["outlet_type"] = user_input
            app.config["recommendation_system_on"]=0
            aiml_response = recommend_outlet(app.config["recommend_system_values"]["food_style"],app.config["recommend_system_values"]["location"],app.config["recommend_system_values"]["budget"],app.config["recommend_system_values"]["food_type"],app.config["recommend_system_values"]["outlet_type"],app.config["recommend_system_values"]["check"])
        elif "exit":
            app.config["recommendation_system_on"]=0
            aiml_response = kernel.respond(user_input)
        else:
            aiml_response="Could you please provide an answer to the previous question?"
    elif app.config["recommendation_system_on"]==6:
        if(app.config["recommend_system_values"]["check"]=="one" and (("sit-down" in user_input) or ("takeaway" in user_input))):
            app.config["recommend_system_values"]["outlet_type"] = user_input
            app.config["recommendation_system_on"]=0
            aiml_response = recommend_outlet(app.config["recommend_system_values"]["food_style"],app.config["recommend_system_values"]["location"],app.config["recommend_system_values"]["budget"],app.config["recommend_system_values"]["food_type"],app.config["recommend_system_values"]["outlet_type"],app.config["recommend_system_values"]["check"])
        elif "exit":
            app.config["recommendation_system_on"]=0
            aiml_response = kernel.respond(user_input)
        else:
            aiml_response="Could you please provide an answer to the previous question?"
    elif 'weather' in user_input:        
        if app.config["recommendation_system_on"]>0:
            app.config["recommendation_system_on"]=0
        city=""
        for i in range(8,len(user_input)):
            city+=user_input[i]
        weather = get_weather(city)
        temp= weather["temp"]
        humidity = weather["humidity"]
        conditions = weather["conditions"]
        aiml_response = f"The Temperature in {city} is {temp}°C, humidity is {humidity}% and the conditions are {conditions}"
    else:
        if app.config["recommendation_system_on"]>0:
            app.config["recommendation_system_on"]=0
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
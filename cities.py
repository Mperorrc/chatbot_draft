import pandas as pd

cities_df = pd.read_excel("C:\\Users\\aparn\\Desktop\\AI\\chatbot\\worldcities.xlsx")

def get_cities(user_input):
    str = user_input.lower()
    
    words=[]
    for city in cities_df['city_ascii']:
        if city.lower() in str:
            words.append(city)
    return words
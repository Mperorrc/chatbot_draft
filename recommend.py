from pyDatalog import pyDatalog
import datetime

# Define the facts and rules using pyDatalog syntax
pyDatalog.create_terms('X,outlet,Mess1,Mess2,acads,serves_veg,serves_non_veg,Beverages,Maggi,Meals,fast_food,sit_down,takeaway,sandwich,location,cheap,expensive,afternoon,evening,night')

# Define the rules
+outlet('Bitsian Pleasant') 
+outlet('Agra Chat')
+outlet('Fruitful')
+outlet('Hotspot')
+outlet('Amul')
+outlet('Vijay-Vahini')
+outlet('Yummpys')
+outlet('Diamond Eatery')
+outlet('Chipotle')
+outlet('Wich Please')
+outlet('SFC')
+outlet('Cafeteria')
+outlet('CCD')
+outlet('Mess 1 Juice shop')
+outlet('Mess 1 Burger shop')
+outlet('Mess 2 Juice shop')
+outlet('ANC-1')
+outlet('ANC-2')


# VEG OR NON_VEG
+serves_veg('Bitsian Pleasant') 
+serves_veg('Agra Chat')
+serves_veg('Fruitful')
+serves_veg('Hotspot')
+serves_veg('Amul')
+serves_veg('Vijay-Vahini')
+serves_veg('Yummpys')
+serves_veg('Diamond Eatery')
+serves_veg('Chipotle')
+serves_veg('Wich Please')
+serves_veg('SFC')
+serves_veg('Cafeteria')
+serves_veg('CCD')
+serves_veg('Mess 1 Juice shop')
+serves_veg('Mess 1 Burger shop')
+serves_veg('Mess 2 Juice shop')
+serves_veg('ANC-1')
+serves_veg('ANC-2')

+serves_non_veg('Bitsian Pleasant')
+serves_non_veg('Fruitful')
+serves_non_veg('Hotspot')
+serves_non_veg('Amul')
+serves_non_veg('Vijay-Vahini')
+serves_non_veg('Yummpys')
+serves_non_veg('Chipotle')
+serves_non_veg('SFC')
+serves_non_veg('Cafeteria')
+serves_non_veg('Mess 1 Burger Shop')
+serves_non_veg('ANC-1')
+serves_non_veg('ANC-2')

#FOOD TYPE
+Beverages('Amul')
+Beverages('Fruitful')
+Beverages('Mess 1 Juice shop')
+Beverages('Mess 2 Juice shop')
+Beverages('CCD')

+Maggi('Yummpys')
+Maggi('Hotspot')
+Maggi('Wich Please')

+Meals('Chipotle')
+Meals('Hotspot')
+Meals('ANC-1')
+Meals('ANC-2')
+Meals('Cafeteria')

+fast_food('SFC')
+fast_food('Fruitful')
+fast_food('Mess 1 Burger shop')
+fast_food('ANC-1')
+fast_food('ANC-2')

+sandwich('Wich Please')
+sandwich('Yummpys')
+sandwich('Cafeteria')

#location
+Mess1('Bitsian Pleasant') 
+Mess1('Agra Chat')
+Mess1('Fruitful')
+Mess1('Hotspot')
+Mess1('Amul')
+Mess1('Vijay-Vahini')
+Mess1('Yummpys')
+Mess1('Diamond Eatery')
+Mess1('Chipotle')
+Mess2('Wich Please')
+Mess2('SFC')
+acads('Cafeteria')
+acads('CCD')
+Mess1('Mess 1 Juice shop')
+Mess1('Mess 1 Burger shop')
+Mess2('Mess 2 Juice shop')
+Mess1('ANC-1')
+Mess2('ANC-2')

#Timings 
+evening('Bitsian Pleasant') 
+afternoon('Agra Chat')
+evening('Agra Chat')
+evening('Fruitful')
+afternoon('Fruitful')
+afternoon('Hotspot')
+evening('Hotspot')
+afternoon('Amul')
+evening('Amul')
+afternoon('Vijay-Vahini')
+evening('Vijay-Vahini')
+afternoon('Yummpys')
+evening('Yummpys')
+night('Yummpys')
+evening('Diamond Eatery')
+afternoon('Chipotle')
+evening('Chipotle')
+evening('Wich Please')
+night('Wich Please')
+evening('SFC')
+night('SFC')
+afternoon('Cafeteria')
+afternoon('CCD')
+afternoon('Mess 1 Juice shop')
+evening('Mess 1 Juice shop')
+night('Mess 1 Juice shop')
+evening('Mess 1 Burger shop')
+night('Mess 1 Burger shop')
+afternoon('Mess 2 Juice shop')
+evening('Mess 2 Juice shop')
+night('Mess 2 Juice shop')
+night('ANC-1')
+night('ANC-2')

#COST
+expensive('Bitsian Pleasant') 
+cheap('Agra Chat')
+expensive('Fruitful')
+cheap('Hotspot')
+cheap('Amul')
+cheap('Vijay-Vahini')
+cheap('Yummpys')
+expensive('Diamond Eatery')
+cheap('Chipotle')
+cheap('Wich Please')
+expensive('SFC')
+cheap('Cafeteria')
+expensive('CCD')
+cheap('Mess 1 Juice shop')
+cheap('Mess 1 Burger shop')
+cheap('Mess 2 Juice shop')
+cheap('ANC-1')
+cheap('ANC-2')

#SERVICE
+sit_down('Bitsian Pleasant') 
+takeaway('Bitsian Pleasant') 
+sit_down('Agra Chat')
+takeaway('Fruitful')
+sit_down('Hotspot')
+takeaway('Hotspot')
+takeaway('Amul')
+sit_down('Vijay-Vahini')
+takeaway('Vijay-Vahini')
+sit_down('Yummpys')
+takeaway('Yummpys')
+takeaway('Diamond Eatery')
+sit_down('Chipotle')
+takeaway('Chipotle')
+sit_down('Wich Please')
+takeaway('Wich Please')
+sit_down('SFC')
+takeaway('SFC')
+sit_down('Cafeteria')
+takeaway('CCD')
+takeaway('Mess 1 Juice shop')
+sit_down('Mess 1 Burger shop')
+takeaway('Mess 2 Juice shop')
+sit_down('ANC-1')
+takeaway('ANC-1')
+sit_down('ANC-2')
+takeaway('ANC-2')

def recommend_outlet(food_style,location,budget,food_type,outlet_type,check):
    results = outlet(X)
    current_hour = datetime.datetime.now().hour

    if (current_hour >=2 and current_hour < 11):
        return "Sorry, No restaurants are open currently"
    elif (current_hour>=2 and current_hour<17):
        results = results & afternoon(X)
    elif (current_hour>=17 and current_hour<23):
        results = results & evening(X)
    else:
        results = results & night(X)

    if food_style == 'Beverage':
        results = results & Beverages(X)
    elif food_style == 'Maggi' :
        results = results & Maggi(X)
    elif food_style == 'Meals' :
        results = results & Meals(X)
    elif food_style == 'fast-food' :
        results = results & fast_food(X)
    elif food_style == 'sandwich' :
        results = results & sandwich(X)
    else:
        return "Sorry, I couldn't find a restaurant matching your preferences."
        
    
    if len(results)==0:
        return "Sorry, I couldn't find a restaurant matching your preferences."
        
    if budget == 'cheap':
        results = results & cheap(X)
    elif budget == 'expensive' :
        results = results & expensive(X)
    else:
        return "No such outlets Found"
    
    if len(results)==0:
        return "Sorry, I couldn't find a restaurant matching your preferences."
        
    if (check=="multiple" and food_style == "Beverage"):
        recommendations = f"I recommend Restaurant(s) :"
        for i in range(len(results)):
            recommendations += f" {i+1}. {results[i][0]}, "
        return recommendations   
    
    if check=='one':
        if location == 'Mess-1':
            results = results & Mess1(X)
        elif location == 'Mess-2' :
            results = results & Mess2(X)
        elif location == 'academic-blocks':
            results = results & acads(X)
        else:
            return "Sorry, I couldn't find a restaurant matching your preferences."
             

    if len(results)==0:
        return "Sorry, I couldn't find a restaurant matching your preferences."

    if food_type == "Vegetarian":
        results = results & serves_veg(X)
    elif food_type == "Non-Vegetarian" :
        results = results & serves_non_veg(X)
    else:
        return "Sorry, I couldn't find a restaurant matching your preferences."
        

    if len(results)==0:
        return "Sorry, I couldn't find a restaurant matching your preferences."
        
    if outlet_type == "sit-down":
        results = results & sit_down(X)
    elif outlet_type == "takeaway" :
        results = results & takeaway(X)
    else:
        return "Sorry, I couldn't find a restaurant matching your preferences."
        

    if len(results)==0:
        return "Sorry, I couldn't find a restaurant matching your preferences."
        

    if check=='multiple':
        recommendations = f"I recommend Restaurant(s) :"
        for i in range(len(results)):
            recommendations += f" {i+1}. {results[i][0]}, "
        return recommendations
    
    return f"I recommend Restaurant {results[0][0]}"


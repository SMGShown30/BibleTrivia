import requests
import openai
from password import weatherapi, openaiKey

openai.api_key = openaiKey

def run_program():
    event = input("What is the event? ")
    event_location = input("Where is the event? ")
    
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': event_location,
        'appid': weatherapi,
        'units': 'imperial',  # Specify units as Fahrenheit
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    
    print(f"The weather is {weather_description} and the temperature is {temperature}°F.")
    
    outfit_suggestion = generate_outfit_suggestion(weather_description, temperature, event)
    
    while True:
        print("Outfit Suggestion:", outfit_suggestion)
        feedback = input("Do you like this outfit suggestion? (yes/no): ")
        
        if feedback.lower() == "yes":
            print("Great! Enjoy your event!")
            break
        elif feedback.lower() == "no":
            print("Generating another outfit suggestion...")
            outfit_suggestion = generate_outfit_suggestion(weather_description, temperature, event)
        else:
            print("Invalid input. Please respond with 'yes' or 'no'.")

def generate_outfit_suggestion(weather_description, temperature, event):
    prompt = f"Given that the weather is {weather_description} and the temperature is {temperature}°F, " \
             f"what would be a suitable outfit for {event}?"
    
    response = openai.Completion.create(
        engine="text-davinci-003",  
        prompt=prompt,
        max_tokens=50
    )
    
    outfit_suggestion = response.choices[0].text.strip()
    return outfit_suggestion

run_program()
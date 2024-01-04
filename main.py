from tkinter import *
import requests
import json
from datetime import datetime


root = Tk()

root.geometry("400x400")
root.resizable(0,0)
root.title("Weather App")


city_value = StringVar()


def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

# Function to show weather.
def showWeather():

    # API key from the weather app
    api_key = "dece89b39d96c68b97e31b945fc82386"

    city_name = city_value.get()

    weather_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=" + api_key

    response = requests.get(weather_url)

    weather_info = response.json()

    tfield.delete("1.0", "end")


    if weather_info["cod"] == 200:
        kelvin = 273

        temp = int(weather_info['main']['temp'] - kelvin)    #converting default kelvin value to Celcius
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)

        weather = f"\nWeather of: {city_name}\nTemperature (celcius): {temp}\nWind Speed: {wind_speed}\nFeels like in (Celsius): {feels_like_temp}\nPressure: {pressure} hPa\nHumidity: {humidity}\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"Weather for '{city_name}' not found!" 

    tfield.insert(INSERT, weather)

    #------------------Frontend of the code - Interface ---------------------------

city_head = Label(root, text= "Enter city name", font = "Arial 12 bold").pack(pady=10)

inp_city = Entry(root, textvariable= city_value, width=24, font="Arial 14 bold").pack()


Button(root, command = showWeather, text = "Check Weather", font = "Arial 10", bg="lightblue", fg="black", activebackground="teal", padx=5, pady=5).pack(pady=20)

weather_now = Label(root, text= "The Weather is:", font= "arial 12 bold").pack(pady=10)


tfield = Text(root, width=46, height=10)
tfield.pack()


root.mainloop()

 
    # Error: the api call shows a error 401. could not find what.
    


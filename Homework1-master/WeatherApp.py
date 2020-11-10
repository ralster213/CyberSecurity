#WeatherApp.py
#Name:
#Date:
#Assignment:

import WeatherInfo

#Set your key
WeatherInfo.setKey("486ed41a7132cb68475ad7bf69cc3261")

#Ask the user for their city
city = str(input("Name a City: "))
WeatherInfo.setCity(city)
print("1")
#Update the weather with the given city
WeatherInfo.updateWeather()
#Request any data you need from the WeatherInfo API
print("2")
#Process the data
#convert temperature to fahrenheit,
#determine wind speed in words
#decide jacket and umbrella status

#Report to the user the weather of their city

#Ask user if they would like another weather report
#If yes, loop to the top of your program where they are asked for a city.
#If no, end with a goodbye statement of some sort.

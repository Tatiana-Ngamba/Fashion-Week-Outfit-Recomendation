""" 01. GET API RESPONSE"""  # Pprinting weather data from API URL using my API key
import requests  # using this module to request data from API

import random

from datetime import datetime  # importing the date module for the date format

from pprint import pprint  # importing this module to print the weather nicely

# # Creating two lists to store the key cities and key dates to fetch data
cities = ["London", "Milan", "Paris", "New York"]
dates = ["2023-09-15", "2023-09-19", "2023-09-25", "2023-09-07"]

"""
# creating a function takes each city as an input and sends a request to the OpenWeatherMap API with specified
# parameters including the city name and API key, and returns the JSON response containing weather information if the
# request is successful """


def fetch_weather_data(city_data, date_data):
    endpoint = "http://api.openweathermap.org/data/2.5/weather"  # Using the weather URL
    API_key = "bd58aba1faf9ee29b70b75372dc3e1d6"  # Using my generated API Key from openweather.I used the link
    # provided by CFG and made an account and then navigated to the Api Keys screen and generated a new key for this
    # assignment.

    params = {
        "q": city_data,
        "date": date_data,
        "appid": API_key,
        "units": "metric"
    }

    response = requests.get(endpoint, params=params)

    # Using if. else statement and comparison operator to ensure the correct response is == 200
    if response.status_code == 200:
        data_response = response.json()
        pprint(data_response)  # printing the response data nicely
        return response.json()

    else:
        print("Failed to get data details for {}. Error code: {}".format(city, response.status_code))
        return None


""" 02. EXTRACTING SPECIFIC DATA """  # Extracting weather data from the response and write it to a file

# # Creating a file name to store specific weather details that I will need for each city.
file_name = "weather_data_details.txt"
with open(file_name, "a") as file:  # using append mode to add details to the file as it is being requested
    # getting weather data for each city using start and end date
    for city, date in zip(cities, dates):
        data = fetch_weather_data(city, date)

        if data:
            # Extract weather data for the current city
            city_name = data['name']
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            country = data['sys']['country']

            # Converting the timestamps to a readable date and time
            sunrise_time = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')
            sunset_time = datetime.fromtimestamp(data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')
            # Writing into the file specific data that I want to see.
            file.write("\nWeather data for {}:\n".format(city_name))
            file.write("\nDescription: {}".format(weather_description))
            file.write("\nTemperature: {}°C".format(temperature))
            file.write("\nFeels_like: {}°C".format(feels_like))
            file.write("\nHumidity: {}%".format(humidity))
            file.write("\nWind Speed: {} m/s".format(wind_speed))
            file.write("\nSunrise Time: {}".format(sunrise_time))
            file.write("\nSunset Time: {}".format(sunset_time))
            file.write("\ncountry: {}\n".format(country))

            print("The weather data for {} has been added to {}".format(city, file_name))

print("All weather data has been added to {}".format(file_name))

""" 03. CREATING A FUNCTION TO GENERATING OUTFIT FOR THE USER """


# Creating a Function to generate outfit recommendations based on weather data
def generate_outfit(weather_data2):
    temperature2 = weather_data2['main']['temp']
    # Use string slicing to remove leading and trailing whitespace
    weather_description2 = weather_data2['weather'][0]['description'].strip().lower()
    cloud_coverage = weather_data2['clouds']['all']
    # Using a list to store outfits options for the user.
    outfits = {
        "hot": ["Wear a ribbed silk tank top,cropped wide-leg pants,suede sandals and sunglasses.Don't forget "
                "sunscreen!", "wear mustard yellow draped silk-chiffon maxi dress, sunglasses and heels sandals.",
                " Wear a printed satin-jacquard maxi skirt & shirt"],
        "mild": ["Wear a relaxed tailored blazer & trousers with t-shirt, heels and sunglasses.",
                 "Wear a T-shirt and jeans and a statement blazer.", " Wear a knitwear top and midi skirt with boots",
                 " Wear a dress with a trench coat and a pair of boots"],
        "cold": ["Dress warmly with a heavy coat, gloves, and a scarf.",
                 "Layer up with a knitwear jumper, denim skirt and high knee boots.",
                 "high neck jersey top, tailored leggings and layered up with an oversize wool blazer",
                 " Wear a tailored wool coat, a black dress and a pair of boots"],
        "rainy": ["Wear a pair of boots, knitwear dress and a waterproof jacket and dont' forget to bring an umbrella.",
                  "Wear a high-rise wide-leg jeans,fitted knit jumper and textured-leather coat and dont' forget to "
                  "bring an umbrella"]
    }

    # Using if...else statements and boolean conditions are used to determine
    # the weather description and temperature conditions.
    # use 'random.choice' to generate outfits and printing specific details for the user.
    if temperature2 > 30:
        outfit_rec = random.choice(outfits["hot"])
        weather_details2 = f"Hot weather, Temperature: {temperature}°C, Clouds: {cloud_coverage}%," \
                           f" {get_readable_sunrise(weather_data2)} sunrise, {get_readable_sunset(weather_data2)} sunset"
    elif temperature2 > 10:
        if "rain" in weather_description2:
            outfit_rec = random.choice(outfits["rainy"])
            weather_details2 = f"Rainy weather, Temperature: {temperature}°C, Clouds: {cloud_coverage}%, " \
                               f"{get_readable_sunrise(weather_data2)} sunrise, {get_readable_sunset(weather_data2)} sunset"
        else:
            outfit_rec = random.choice(outfits["mild"])
            weather_details2 = f"Mild weather, Temperature: {temperature}°C, Clouds: {cloud_coverage}%," \
                               f" {get_readable_sunrise(weather_data2)} sunrise, {get_readable_sunset(weather_data2)} sunset"
    else:
        outfit_rec = random.choice(outfits["cold"])
        weather_details2 = f"Cold weather, Temperature: {temperature}°C, Clouds: {cloud_coverage}%, " \
                           f"{get_readable_sunrise(weather_data2)} sunrise, {get_readable_sunset(weather_data2)} sunset"
    # Returning outfit recommendation and weather details as a tuple
    return outfit_rec, weather_details2


""" 04. CREATING A FUNCTION FOR THE DIFFERENT FASHION SHOWS """


# Creating a function for the fashion show details
def get_fashion_show_details(show_date):
    # Creating a dictionary to represent a schedule of fashion shows.
    fashion_shows = {
        "2023-09-07": "New York - Hanifa",
        "2023-09-08": "New York - Laquan Smith",
        "2023-09-15": "London - Dilara",
        "2023-09-16": "London - Simone Rocha",
        "2023-09-17": "London - David Koma",
        "2023-09-25": "Paris - Balmain",
        "2023-09-26": "Paris - Chanel",
        "2023-09-27": "Paris - Alexander McQueen",
        "2023-09-19": "Milan - Prada",
        "2023-09-20": "Milan - Versace"
    }

    return fashion_shows.get(show_date, "No fashion show on this date")


""" 05. CREATING FUNCTIONS FOR A READABLE SUNSET & SUNRISE """


# creating a function to get readable sunrise time
def get_readable_sunrise(weather_data3):
    sunrise_timestamp = weather_data3['sys']['sunrise']
    return datetime.utcfromtimestamp(sunrise_timestamp).strftime('%H:%M:%S')


# creating a function to get readable sunset time
def get_readable_sunset(weather_data4):
    sunset_timestamp = weather_data4['sys']['sunset']
    return datetime.utcfromtimestamp(sunset_timestamp).strftime('%H:%M:%S')


""" 06. USER INPUT USING EXCEPTION HANDLING ERROR """
# Main program
if __name__ == "__main__":
    # Ask the user for fashion week date and city
    date = input("Enter the fashion week date (DD/MM/YYYY): ")

    # Using an exception handling method to convert the input date to the desired format (YYYY-MM-DD)
    try:
        input_date = datetime.strptime(date, "%d/%m/%Y")
        date = input_date.strftime("%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use DD/MM/YYYY format.")
        exit()

    city = input("Enter your current city: ")

    """ 07. PRINTING THE OUTFIT RECOMMENDATION BASED ON THE USER INPUT """
    # Fetch weather data for the specified city
    weather_data = fetch_weather_data(city, date)

    if weather_data:
        outfit, weather_details = generate_outfit(weather_data)
        show_details = get_fashion_show_details(date)

        # Printing outfit recommendation
        print("Your outfit recommendation for {} is: {}".format(show_details, outfit))
        print("Weather Details: {}".format(weather_details))

        """ 08. WRITING THE FINAL RESULTS INTO THE FILE """

        # Recording and saving the inputted data & outfit recommendation in a file
        with open("Outfit_Recommendations.txt", "a") as text_file:
            text_file.write("Date: {}, City: {}\n".format(date, city.upper()))
            text_file.write("Show Details: {}\n".format(show_details))
            text_file.write("Outfit recommendation: {}\n".format(outfit))
            text_file.write("Weather details: {}\n".format(weather_details))
            text_file.write("  - Description: {}\n".format(weather_data['weather'][0]['description']))
            text_file.write("  - Humidity: {}%\n".format(weather_data['main']['humidity']))
            text_file.write("  - Wind Speed: {} m/s\n".format(weather_data['wind']['speed']))
            text_file.write("-" * 50 + "\n")  # Adding a separator line to print the data nicely
            print("The details have been recorded and saved in the text file.")
    else:
        print("No fashion show on {} in {}.".format(date, city))

""" NOTE - The program will still recommend a random outfit choice depending on the weather even with no fashion show"""

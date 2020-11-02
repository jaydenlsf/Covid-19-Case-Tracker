import requests
import json

url = "https://api.covid19api.com/summary"
# Send a request to the url and return the response as string
response = requests.get(url).text

# Convert the response from string to a json object
response_info = json.loads(response)

country = input('Enter the country code (e.g US for United States): ')

world_new_cases = response_info['Global']['NewConfirmed']
world_total_cases = response_info['Global']['TotalConfirmed']

for countries in response_info['Countries']:
    country_name = countries['Country']
    new_cases = countries['NewConfirmed']
    total_case = countries['TotalConfirmed']
    total_deaths = countries['TotalDeaths']
    last_update = countries['Date']

    if countries['CountryCode'] == country.upper():
        print(f"""
        || Covid-19 Stats for {country_name} ||

        New Confirmed Cases: {new_cases}
        Total Confirmed Cases: {total_case}
        Total Deaths: {total_deaths}


        || Global Stats ||
        New Cases: {world_new_cases}
        Total Cases: {world_total_cases}


        Last Update: {last_update}
        """)
        break
else:
    print('Please enter a valid country code.')

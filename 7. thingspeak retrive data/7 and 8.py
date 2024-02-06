import requests
import json

# ThingSpeak Channel ID and Read API Key
channel_id = '2414340'
api_key = 'JB3VRHR493C1DC0Q'

# Number of results to retrieve
results_count = 10  # Adjust this based on your needs

# ThingSpeak API URL
url = f'https://api.thingspeak.com/channels/{channel_id}/feeds.json?api_key={api_key}&results={results_count}'

try:
    # Make a GET request to ThingSpeak API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = json.loads(response.text)

        # Extract and print temperature and humidity from each entry
        for entry in data['feeds']:
            temperature = float(entry['field1'])
            humidity = float(entry['field2'])
            timestamp = entry['created_at']

            print(f'Timestamp: {timestamp}, Temperature: {temperature} °C, Humidity: {humidity} %')

    else:
        print(f'Error: Unable to retrieve data. Status code: {response.status_code}')

except Exception as e:
    print(f'Error: {e}')

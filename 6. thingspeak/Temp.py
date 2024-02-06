import Adafruit_DHT
import requests
import time

# ThingSpeak API Key and Channel ID
api_key = 'JB3VRHR493C1DC0Q'
channel_id = '2414340'

# DHT11 sensor setup
sensor = Adafruit_DHT.DHT11
pin = 4  # GPIO 4 (pin 7) where the DHT11 sensor is connected

def read_dht11_data():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return humidity, temperature

def send_to_thingspeak(temp, hum):
    url = f'https://api.thingspeak.com/update?api_key={api_key}&field1={temp}&field2={hum}'
    response = requests.get(url)
    print(f'ThingSpeak response: {response.status_code}')

def main():
    try:
        while True:
            humidity, temperature = read_dht11_data()
            if humidity is not None and temperature is not None:
                print(f'Temperature: {temperature}°C, Humidity: {humidity}%')
                send_to_thingspeak(temperature, humidity)
            else:
                print('Failed to retrieve DHT11 data.')

            time.sleep(15)  # Send data every 15 seconds (adjust as needed)

    except KeyboardInterrupt:
        print('Program terminated by user.')

if __name__ == "__main__":
    main()

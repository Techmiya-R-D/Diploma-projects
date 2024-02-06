import time
import board
import adafruit_dht
import requests

api_key = 'JB3VRHR493C1DC0Q'
channel_id = '2414340'
# Sensor data pin is connected to GPIO 4
sensor = adafruit_dht.DHT11(board.D4)
# Uncomment for DHT11
#sensor = adafruit_dht.DHT11(board.D4)


def send_to_thingspeak(temp, hum):
    url = f'https://api.thingspeak.com/update?api_key={api_key}&field1={temp}&field2={hum}'
    response = requests.get(url)
    print(f'ThingSpeak response: {response.status_code}')
    
    
    
while True:
    try:
        # Print the values to the serial port
        temperature_c = sensor.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = sensor.humidity
        print("Temp={0:0.1f}ºC, Temp={1:0.1f}ºF, Humidity={2:0.1f}%".format(temperature_c, temperature_f, humidity))
        send_to_thingspeak(temperature_c, humidity)
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error

    time.sleep(3.0)

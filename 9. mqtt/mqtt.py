import paho.mqtt.client as mqtt
import Adafruit_DHT
import time

# DHT11 sensor setup
sensor = Adafruit_DHT.DHT11
pin = 4  # GPIO pin where the DHT11 sensor is connected

# MQTT broker settings
broker_address = "192.168.0.151"  # Replace with your broker's address
broker_port = 1883
topic = "temperature"

def read_temperature():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return temperature

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def main():
    client = mqtt.Client()
    client.on_connect = on_connect

    client.connect(broker_address, broker_port, 60)
    client.loop_start()

    try:
        while True:
            temperature = read_temperature()
            print("Temperature:", temperature)

            # Publish temperature to MQTT broker
            client.publish(topic, temperature)
            
            time.sleep(5)  # Delay between readings (adjust as needed)

    except KeyboardInterrupt:
        print("Program terminated by user.")
        client.disconnect()

if __name__ == "__main__":
    main()

import socket
import Adafruit_DHT
import time

# DHT11 sensor setup
sensor = Adafruit_DHT.DHT11
pin = 4  # GPIO pin where the DHT11 sensor is connected

# UDP server settings
host = '0.0.0.0'
port = 12345

def read_humidity():
    humidity, _ = Adafruit_DHT.read_retry(sensor, pin)
    return humidity

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print(f"UDP Server listening on {host}:{port}")

    try:
        while True:
            data, client_address = server_socket.recvfrom(1024)
            if data.decode("utf-8") == "request_humidity":
                humidity = read_humidity()
                response = f"Humidity: {humidity}%"
                server_socket.sendto(response.encode("utf-8"), client_address)
                time.sleep(2)
    except KeyboardInterrupt:
        print("Program terminated by user.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()

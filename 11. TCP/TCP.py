import socket
import Adafruit_DHT
import time

# DHT11 sensor setup
sensor = Adafruit_DHT.DHT11
pin = 4  # GPIO pin where the DHT11 sensor is connected

# TCP server settings
host = '0.0.0.0'
port = 12345

def read_humidity():
    humidity, _ = Adafruit_DHT.read_retry(sensor, pin)
    return humidity

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Listen for only one connection

    print(f"TCP Server listening on {host}:{port}")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")

            try:
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break

                    if data.decode("utf-8") == "request_humidity":
                        humidity = read_humidity()
                        response = f"Humidity: {humidity}%"
                        client_socket.send(response.encode("utf-8"))

            except ConnectionResetError:
                print("Connection reset by client")

            finally:
                client_socket.close()

    except KeyboardInterrupt:
        print("Program terminated by user.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()

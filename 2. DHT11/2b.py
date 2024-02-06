import time
import board
import busio
import digitalio
import adafruit_dht
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)
sensor = adafruit_dht.DHT11(board.D21)

# Display Parameters
WIDTH = 128
HEIGHT = 32
BORDER = 5

# Display Refresh
LOOPTIME = 1

# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

# Create blank image for drawing.
# Make sure to create an image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on the image.
draw = ImageDraw.Draw(image)

# Draw a white background
draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

font = ImageFont.truetype('PixelOperator.ttf', 16)

while True:
    try:
        # Print the values to the serial port
        temperature_c = sensor.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = sensor.humidity
        print("Temp={0:0.1f}ºC, Temp={1:0.1f}ºF, Humidity={2:0.1f}%".format(temperature_c, temperature_f, humidity))
        
        # Clear the display
        draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

        # Display temperature and humidity on OLED
        draw.text((0, 0), "Temperature: {0:0.1f}ºC".format(temperature_c), font=font, fill=255)
        draw.text((0, 16), "Humidity: {0:0.1f}%".format(humidity), font=font, fill=255)

        oled.image(image)
        oled.show()
        time.sleep(LOOPTIME)

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error
    
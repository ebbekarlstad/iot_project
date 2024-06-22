## How to build a temperature and humidity sensor!

*This report was written by Ebbe Karlstad (ekk224ev).*

This tutorial will hopefully give you the necessary knowledge for how to build a temperature and humidity sensor using a Raspberry Pi Pico, a DHT11 sensor, and Adafruit.

*Approximated time of completion: ~ 5 hours*


## Objective

I chose to do this project mostly to learn about IoT. The Internet of Things was a very new subject for me when starting this course, so I wanted to make a simpler project that would make me learn more about the subject. Also, the DHT11 sensor was one of the only sensors included in the [Starter Kit](https://www.electrokit.com/lnu-starter) that I bought, so making a humidity and temperature sensor made much sense to me.

## Material

| Component | Purpose | Price and link |
|--|--|--|
| Raspberyy Pi Pico | A microcontroller for the project | [Pico - electrokit](https://www.electrokit.com/raspberry-pi-pico-wh) 109kr |
| DHT11 Sensor | Sensor for humidity and temperature | [DHT11 - electrokit](https://www.electrokit.com/digital-temperatur-och-fuktsensor-dht11) 49kr |
| Breadboard | Used to connect the jumper cables to the Pico | [Breadboard - electrokit](https://www.electrokit.com/kopplingsdack-400-anslutningar) 49kr |
| M-M jumper cables | Used to connect different components together | [Cables - electrokit](https://www.electrokit.com/labbsladd-20-pin-15cm-hane/hane) 29kr |
| USB Cable | Connects the Pico to a laptop | [USB Cable - electrokit](https://www.electrokit.com/usb-kabel-a-hane-micro-b-hane-60cm) 28kr |


## Computer Setup

I chose to use Thonny IDE for this project. My initial plan was to use VS Code with the PyMakr plugin, but due to many issues with the plugin and with VS Code, I instead opted for Thonny, which turned out to be very easy to use.

1. Install Python using the official download link: https://www.python.org/downloads/ 
2. Install Thonny IDE: https://thonny.org/
3.  Install Micropython. This will allow us to program our microcontroller: https://micropython.org/download/RPI_PICO_W/
4. While holding down the "BOOTSEL" button on your microcontroller, plug it in via USB to your laptop. Release the button and open up the new drive that appeared. Copy and paste the uf2 file from your downloads into this drive. This will make it disappear, which means it is now working with Micropython.

## Putting everything together

This is a pretty simple circuit diagram that shows how everything is connected. Blue cable sends data from the sensor, red cable gives it power and brown cable is ground.
![Circuit diagram](https://raw.githubusercontent.com/ebbekarlstad/iot_project/main/temp_hum_sketch.jpg)
Simply power everything as shown in the image, and you're done with the physical part!
## Platform

I chose to use the platform Adafruit. It is free and rather easy to use, and straightforward. It allows users to visualise their data in a user-friendly way. They have a lot of tutorials on their website, which I found to be very usefeul. An example is this one right here: https://learn.adafruit.com/adafruit-io/mqtt-api
By connecting my micropython files to Adafruit, and creating two seperate "feeds", I was able to graph out the temperature and humidity, you can see a small test I did of it in the *presenting the data* section.

## Code

For this project, I've written 4 different scripts, all in the python programming language. These are: *boot.py, main.py, credentials.py, mqtt.py*. These are functioning as follows:

**boot.py:** This file contains information about what happens on startup. In our case, that is connecting to our wifi, using a function called *connect()*:

    def connect():
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        wlan.active(True)
        wlan.config(pm=0xa11140)
        # This is changed in credentials.py
        wlan.connect(credentials['ssid'], credentials['pw'])
        while not wlan.isconnected():
            pass  # Wait until connection is established
    return wlan.ifconfig()[0]
**main.py:** This script is the main file where operations are happening. It reads the data from the DHT11 sensor, and also publishes this to the Adafruit feeds. It contains many different variables, and a function called *main()*, which you can see here:

    def main():
    client = connect_mqtt()
    print("Connected to MQTT broker")

    last_publish_time = time()

    while True:
        if (time() - last_publish_time) >= PUBLISH_INTERVAL:
            internalLED.toggle()
            
            temperature, humidity = get_sensor_readings()
            print(f"Temperature: {temperature}, Humidity: {humidity}")

            client.publish(AIO_HUMIDITY_FEED, str(humidity))
            client.publish(AIO_TEMPERATURE_FEED, str(temperature))
            print("Published data to MQTT broker")

            internalLED.toggle()
            last_publish_time = time()
        
        sleep(1)
**credentials.py and mqtt.py:** Both these scripts live inside the *lib* directory, meaning they are libraries. credentials.py simply contains information about the wifi you want to connect to, and mqtt.py has functionality for connecting to a MQTT broker (which can be seen as an entity that enables MQTT clients to connect).


*Note that there is more code in the files mentioned than shown in this document.* 
## Connectivity

Data was transferred via Wifi and MQTT. MQTT was something new for me when starting this porject, but it is essentially the standard for IoT messaging, and it works in a publish-subscribe manner. The data is sent every ten seconds, something that we can change by altering this line of code in the main.py script:

    PUBLISH_INTERVAL = 10  # Publish interval in seconds
This means that every ten seconds, there will be an update in the Adafruit feed.

## Presenting the data

The data presentation is simply what Adafruit gave me, meaning no additional stylistic tweaking has been done. It is currently presented using two line graphs, one for temperature and one for humidity (see images below). The data is stored for 30 days due to Adafruit's own policies.

Humidity feed:
![Humidity](https://raw.githubusercontent.com/ebbekarlstad/iot_project/main/humidity_screen.png)

Temperature feed:
![Temperature](https://raw.githubusercontent.com/ebbekarlstad/iot_project/main/temperature_screen.png)

## Finalizing the design

The final design of the project can be seen in the picture below! This was a very exciting course fore me, I learnt so many new cool things about IoT, circuits, data transmitting and more. Before this course, I had very limited knowledge about IoT, and I can now say that I feel like I've at least scraped the tip of the iceberg. :blush:
Overall, I think the project went good, I picked an easier project just because I wanted to fully learn everything I was doing and not just get overwhelmed with information, which worked out great in the end. Of course, a project is never perfect and done, but for a first IoT project, I'm rather happy!
![Final Project](https://raw.githubusercontent.com/ebbekarlstad/iot_project/main/final.jpg)

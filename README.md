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
By connecting my micropython files to Adafruit, and creating two seperate "feeds", I was able to graph out the temperature and humidity, you can see a small test I did of it here:
![Humidity](https://raw.githubusercontent.com/ebbekarlstad/iot_project/main/humidity_screen.png)
![Temperature](https://raw.githubusercontent.com/ebbekarlstad/iot_project/main/temperature_screen.png)

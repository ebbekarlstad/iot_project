from machine import Pin, reset
from time import sleep, time
import dht
import ubinascii
from mqtt import MQTTClient
import machine

# Configuration
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "username"
AIO_KEY = "aio_SsYV94knMgPwcyS1TR6i48jQXX0n"
AIO_HUMIDITY_FEED = "username/feeds/humidity_feed_name"
AIO_TEMPERATURE_FEED = "username/feeds/temperature_feed_name"
PUBLISH_INTERVAL = 10  # Publish interval in seconds

# Sensor and MQTT setup
sensor = dht.DHT11(Pin(28))
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id()).decode('utf-8')
internalLED = Pin(2, Pin.OUT)

def get_sensor_readings():
    sensor.measure()
    return sensor.temperature(), sensor.humidity()

def connect_mqtt():
    client = MQTTClient(AIO_CLIENT_ID, AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY, keepalive=60)
    client.connect()
    return client

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

if __name__ == "__main__":
    while True:
        main()
        sleep(5)
        reset()

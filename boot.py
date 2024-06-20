import network
import socket
import time
from credentials import credentials

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

def http_get(url='http://detectportal.operagx.com/'):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    with socket.socket() as s:
        s.connect(addr)
        s.send(bytes(f'GET /{path} HTTP/1.0\r\nHost: {host}\r\n\r\n', 'utf8'))
        time.sleep(1)

if __name__ == "__main__":
    # WiFi connection
    try:
        ip = connect()
        print(f"Connected to WiFi, IP address: {ip}")
    except KeyboardInterrupt:
        print("Keyboard interrupt")
    except Exception as e:
        print(f"Failed to connect to WiFi: {e}")

    # HTTP request
    try:
        http_get()
        print("HTTP request sent successfully")
    except Exception as e:
        print(f"Exception occurred during HTTP request: {e}")

#!/usr/bin/python3

import sys
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 17
max_retry = 10


while True:
    i = 0
    while i < max_retry:
        i += 1
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            #TODO: do something
            print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
            break

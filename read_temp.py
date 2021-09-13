#!/usr/bin/python3

import sys
import Adafruit_DHT
import time
import requests
from datetime import datetime
import pytz

sensor = Adafruit_DHT.DHT11
pin = 17
max_retry = 10
room = "living room"
SAMPLE_INTERVAL_SECONDS = 60 * 30

def get_sensor_data():
    i = 0
    while i < max_retry:
        time.sleep(0.5)
        i += 1
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            print(getTime())
            print(room + ': Temp={0:0.1f}*  Humidity={1:0.1f}% \n\n'.format(temperature, humidity))
            return humidity, temperature
    return None, None

def telegram_bot_sendtext(msg="test"):

    bot_token = '1524838585:AAGulzveycgvC7yb7xytHE4UAwtUNfsZfZI'
    bot_chatID = '681732338'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + msg

    response = requests.get(send_text)

    return response.json()

def getTime():
    PST = pytz.timezone('America/Los_Angeles')
    datetime_pst = datetime.now(PST)
    # return datetime_pst.strftime('%Y:%m:%d %H:%M:%S %Z %z')
    return datetime_pst.strftime('%Y-%m-%d %H:%M:%S')


while True:
    humidity, temperature = get_sensor_data()
    if humidity is not None and temperature is not None:
        msg = getTime() + "\n" + room
        msg += ": T: {}C, H: {}%".format(temperature, humidity)
        telegram_bot_sendtext(msg)
    time.sleep(60*SAMPLE_INTERVAL_SECONDS)



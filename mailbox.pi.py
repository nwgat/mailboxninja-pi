import RPi.GPIO as GPIO
import time
from pushover import Client

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    if GPIO.input(14):
      #print("you got mail")
      # pushover
      client = Client("userkey", api_token="apikey")
      client.send_message("You Got Mail, Motherfucker!", title="Mailbox")
      time.sleep(300)

    if GPIO.input(14) == False:
      print("no mail")
      time.sleep(1)

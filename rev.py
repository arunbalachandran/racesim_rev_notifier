from time import sleep
import urllib2, json, sys
import RPi.GPIO as GPIO
r1, r2, r3 = 5, 6, 13
GPIO.setmode(GPIO.BCM)
# always set the yellow lights to be in the active state because you are always accelerating?
GPIO.setup(r1, GPIO.OUT)
GPIO.setup(r2, GPIO.OUT)
GPIO.setup(r3, GPIO.OUT)

# this needs to be looped and done every 10 ms?
url = 'http://192.168.1.94:8080/crest/v1/api?carState=true'
try:
     while (True):
         response = urllib2.urlopen(url).read()
         data = json.loads(response.decode('windows-1252'))
         if (0.925*data["carState"]["mMaxRPM"] <= data["carState"]["mRpm"] <= 0.975*data["carState"]["mMaxRPM"]):
             GPIO.output(r1, False)
             GPIO.output(r2, True)
             GPIO.output(r3, False) 
         elif (data["carState"]["mRpm"] > 0.975*data["carState"]["mMaxRPM"]):
             GPIO.output(r1, False)
             GPIO.output(r2, False)
             GPIO.output(r3, True)
         else:
       	     GPIO.output(r1, True)
             GPIO.output(r2, False)
             GPIO.output(r3, False)
         sleep(0.01)
except:
     GPIO.cleanup()

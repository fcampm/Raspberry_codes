import RPi.GPIO as GPIO
import time
import requests

dweetIO= "https://dweet.io/dweet/for/"
myName = "helloSensor_op"
myKey = "measure_distance"

while True:
    
    GPIO.setmode(GPIO.BCM)

    TRIG = 17
    ECHO = 18

    print("Distance Measurement In Progress")

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    GPIO.output(TRIG, False)
    print("Waiting For Sensor To Settle")
    time.sleep(0.5)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
        
    distance = pulse_duration * 17150
    
    distance = round(distance, 2)

    dist =distance
    rqsString = dweetIO+myName+'?'+myKey+'='+str(dist)
    print(rqsString)
    rqs = requests.get(rqsString)
    print (rqs.status_code)
    print (rqs.headers)
    print (rqs.content)

    GPIO.cleanup()

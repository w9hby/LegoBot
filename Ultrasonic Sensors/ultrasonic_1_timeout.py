import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 23
GPIO_ECHO    = 24
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  
GPIO.setup(GPIO_ECHO,GPIO.IN)    

print "Ultrasonic Measurement"

GPIO.output(GPIO_TRIGGER, False)
time.sleep(0.5)
# Send 10us pulse to trigger
GPIO.output(GPIO_TRIGGER, True)
time.sleep(0.00001)
GPIO.output(GPIO_TRIGGER, False)
start = time.time()

timeout = False
timeout_init = time.time()

while GPIO.input(GPIO_ECHO)==0:
	start = time.time()
	timeout_count = start - timeout_init
	if timeout_count > 0.06:
		timeout = True
		break

while GPIO.input(GPIO_ECHO)==1:
	stop = time.time()
	if timeout_count > 0.06:
		timeout = True
		break

if timeout == False:
	elapsed = stop-start  
	distance = elapsed * 34300
	distance = distance / 2
	print "Distance : %.1f" % distance
else:
	print "Timeout"

GPIO.cleanup()

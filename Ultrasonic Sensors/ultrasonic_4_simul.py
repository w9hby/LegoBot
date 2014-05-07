# ultrasonic_2.py
# Measure distance using two ultrasonic modules
#
# Author : Mostafa Wahby
# Date   : 29.03.2014


import time
import RPi.GPIO as GPIO
import threading
GPIO.setmode(GPIO.BCM)


GPIO_TRIGGER_L = 23
GPIO_ECHO_L    = 24
GPIO_TRIGGER_R = 17
GPIO_ECHO_R    = 27
GPIO_TRIGGER_F = 9
GPIO_ECHO_F    = 11
GPIO_TRIGGER_B = 8
GPIO_ECHO_B    = 7

print "Ultrasonic four sensors Measurement"

GPIO.setup(GPIO_TRIGGER_L,GPIO.OUT)  # Trigger1
GPIO.setup(GPIO_ECHO_L,GPIO.IN)      # Echo1
GPIO.setup(GPIO_TRIGGER_R,GPIO.OUT)  # Trigger2
GPIO.setup(GPIO_ECHO_R,GPIO.IN)      # Echo2
GPIO.setup(GPIO_TRIGGER_F,GPIO.OUT)  # Trigger3
GPIO.setup(GPIO_ECHO_F,GPIO.IN)      # Echo3
GPIO.setup(GPIO_TRIGGER_B,GPIO.OUT)  # Trigger4
GPIO.setup(GPIO_ECHO_B,GPIO.IN)      # Echo4
GPIO.output(GPIO_TRIGGER_L, False)
GPIO.output(GPIO_TRIGGER_R, False)
GPIO.output(GPIO_TRIGGER_F, False)
GPIO.output(GPIO_TRIGGER_B, False)

time.sleep(0.5)

class Trig(threading.Thread):
	def __init__(self,trigger,echo,number):
		super(Trig, self).__init__()
		self.trigger=trigger
		self.echo=echo
	self.number=number

	def run(self):
		GPIO.output(self.trigger, True)
		time.sleep(0.00001)
		GPIO.output(self.trigger, False)
		start = time.time()

		timeout = False
		timeout_init = time.time()

		while GPIO.input(self.echo)==0:
			start = time.time()
			timeout_count = start - timeout_init
			if timeout_count > 0.06:
				timeout = True
				break

		while GPIO.input(self.echo)==1:
   	    stop = time.time()
  	    timeout_count = stop - timeout_init
 	    if timeout_count > 0.06:
			timeout = True
			break

		if timeout == False:
			elapsed = stop-start
			distance = elapsed * 34300
			distance = distance / 2
            print "Distance from Sensor ", self.number, " : %.1f" % distance
			time.sleep(0.06 - timeout_count)
		else:
			print "Sensor ", self.number, " Timeout"


print time.time()

for num in range(0,4):
	thread1 = Trig(GPIO_TRIGGER_L, GPIO_ECHO_L, "L")
	thread2 = Trig(GPIO_TRIGGER_F, GPIO_ECHO_F, "F")
	thread3 = Trig(GPIO_TRIGGER_R, GPIO_ECHO_R, "R")
	thread4 = Trig(GPIO_TRIGGER_B, GPIO_ECHO_B, "B")
	thread1.start()
	thread2.start()
	thread3.start()
	thread4.start()
	thread1.join()
	thread2.join()
	thread3.join()
	thread4.join()
 print "---------"

print time.time()
GPIO.cleanup()

from RPIO import PWM
import RPi.GPIO as GPIO
import time
import curses

GPIO.setmode(GPIO.BOARD)

servo = PWM.Servo()
servoPin = 18
dcPin1 = 15
dcPin2 = 19

GPIO.setup(dcPin1, GPIO.OUT)
GPIO.setup(dcPin2, GPIO.OUT)
servo.set_servo(servoPin, 1450)

def Backward():
    GPIO.output(dcPin1, True)
    GPIO.output(dcPin2, False)

def Forward():
    GPIO.output(dcPin1, False)
    GPIO.output(dcPin2, True)

def Stop():
    GPIO.output(dcPin1, False)
    GPIO.output(dcPin2, False)

pos = 4

screen = curses.initscr()
curses.noecho()
screen.keypad(True)
screen.addstr(0, 0, 'Press the Arrow Keys to control the robot, (S) to stop or (Q) to quit')

try:
    while True:
	screen.clear()
	screen.addstr(0, 0, 'Press the Arrow Keys to control the robot, (S) to stop or (Q) to quit')
        char = screen.getch()
	
        if char == ord('q'): 
            break
        elif char == curses.KEY_RIGHT and pos < 7:  
        	if pos == 1: 
        	     servo.set_servo(servoPin, 750)    #this will send 4.0 ms pulse
        	elif pos == 2: 
        	     servo.set_servo(servoPin, 1100)    #this will send 7.5 ms pulse
        	elif pos == 3: 
        	     servo.set_servo(servoPin, 1450)    #this will send 11.0 ms pulse
        	elif pos == 4: 
        	     servo.set_servo(servoPin, 1800)    #this will send 14.5 ms pulse
        	elif pos == 5: 
        	     servo.set_servo(servoPin, 2150)    #this will send 18.8 ms pulse
        	elif pos == 6: 
        	     servo.set_servo(servoPin, 2500)    #this will send 21.5 ms pulse
		pos += 1
        elif char == curses.KEY_LEFT and pos > 1:  
        	if pos == 2: 
        	     servo.set_servo(servoPin, 400)    #this will send 7.5 ms pulse
        	elif pos == 3: 
        	     servo.set_servo(servoPin, 750)    #this will send 11.0 ms pulse
        	elif pos == 4: 
        	     servo.set_servo(servoPin, 1100)    #this will send 14.5 ms pulse
        	elif pos == 5: 
        	     servo.set_servo(servoPin, 1450)    #this will send 18.8 ms pulse
        	elif pos == 6: 
        	     servo.set_servo(servoPin, 1800)    #this will send 21.5 ms pulse
        	elif pos == 7: 
        	     servo.set_servo(servoPin, 2150)    #this will send 25.0 ms pulse
		pos -= 1
        elif char == curses.KEY_UP:
            screen.addstr(4, 0, 'UP   ')  
	    Forward()      
        elif char == curses.KEY_DOWN:
            screen.addstr(4, 0, 'DOWN ')
	    Backward()
	elif char == ord('s'): 
            screen.addstr(4, 0, 'Stop ')
	    Stop()
	
except KeyboardInterrupt:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    servo.stop_servo(servoPin)
finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    servo.stop_servo(servoPin)




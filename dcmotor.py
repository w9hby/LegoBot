import RPi.GPIO as GPIO
import time
import curses

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

def Backward():
    GPIO.output(15, True)
    GPIO.output(19, False)

def Forward():
    GPIO.output(15, False)
    GPIO.output(19, True)

def Stop():
    GPIO.output(15, False)
    GPIO.output(19, False)


screen = curses.initscr()
curses.noecho()
screen.keypad(True)
screen.addstr(0, 0, 'Press UP to move Forward, DOWN to move Backward, S to Stop or Q to quit')

try:
    while True:
        char = screen.getch()
	screen.addstr(0, 0, 'Press UP to move Forward, DOWN to move Backward, S to Stop or Q to quit')
        if char == ord('q'): 
            break      
        elif char == curses.KEY_UP:
            screen.addstr(4, 0, 'UP   ')  
	    Forward()      
        elif char == curses.KEY_DOWN:
            screen.addstr(4, 0, 'DOWN ')
	    Backward()
	elif char == ord('s'): 
            screen.addstr(4, 0, 'Stop ')
	    Stop()
finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()

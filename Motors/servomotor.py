from RPIO import PWM
import time
import curses

servo = PWM.Servo()
Pin = 18
servo.set_servo(Pin, 1500)    #this will send 15 ms pulse

screen = curses.initscr()
curses.noecho()
screen.keypad(True)
screen.addstr(0, 0, 'Enter 1 - 7 or Q to quit')

try:
    while True:
	screen.clear()
	screen.addstr(0, 0, 'Enter 1 - 7 or Q to quit')
        char = screen.getch()
        if char == ord('q'): 
            break   
        elif char == ord('1'): 
             servo.set_servo(Pin, 600)    #this will send 6.0 ms pulse
        elif char == ord('2'): 
             servo.set_servo(Pin, 900)    #this will send 9.0 ms pulse
        elif char == ord('3'): 
             servo.set_servo(Pin, 1200)    #this will send 12.0 ms pulse
        elif char == ord('4'): 
             servo.set_servo(Pin, 1500)    #this will send 15 ms pulse
        elif char == ord('5'): 
             servo.set_servo(Pin, 1800)    #this will send 18.0 ms pulse
        elif char == ord('6'): 
             servo.set_servo(Pin, 2100)    #this will send 21.0 ms pulse
        elif char == ord('7'): 
             servo.set_servo(Pin, 2400)    #this will send 24.0 ms pulse
finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    servo.stop_servo(Pin)

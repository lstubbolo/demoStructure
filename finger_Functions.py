import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)    # Set GPIO usage
GPIO.setup(32, GPIO.OUT)    # Set up pin 32 for GPIO usage
pwm = GPIO.PWM(32, 50)      # Set up pwm on pin 32
pwm.start(0)                # Set initial pwm of 0
GPIO.setwarnings(False)     # Disable GPIO warnings

#####    Moves finger to starting, retracted position with value of 1
def startPos():
    dutyStart = 1 / 18 + 2
    GPIO.output(32, True)
    pwm.ChangeDutyCycle(dutyStart)
    sleep(0.3)
    GPIO.output(32, False)
    pwm.ChangeDutyCycle(0)
    
#####    Moves finger to the press position with value of 50
def pressPos():
    dutyPress = 50 / 18 + 2
    GPIO.output(32, True)
    pwm.ChangeDutyCycle(dutyPress)
    sleep(0.3)
    GPIO.output(32, False)
    pwm.ChangeDutyCycle(0)
 
#GPIO.cleanup()     ##  May or may not need this line after sequence of execution(s) depending on other GPIO setup
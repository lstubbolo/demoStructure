import RPi.GPIO as GPIO
from time import sleep

#####    Moves finger to starting, retracted position with value of 1
def startPos():
    print("print statement")
    GPIO.setmode(GPIO.BOARD) # Set GPIO usage
    GPIO.setup(32, GPIO.OUT)  # Set up pin 32 for GPIO usage
    pwm=GPIO.PWM(32, 50)      # Set up pwm on pin 32
    pwm.start(0)             # Set initial pwm of 0
    GPIO.setwarnings(False)  # Disable GPIO warnings
    GPIO.output(32, True)
    pwm.ChangeDutyCycle(2.055)
    sleep(0.5)
    GPIO.output(32, False)
    pwm.ChangeDutyCycle(0)
    GPIO.cleanup()
    
#####    Moves finger to the press position with value of 50
def pressPos():
    print("print statement")
    GPIO.setmode(GPIO.BOARD) # Set GPIO usage
    GPIO.setup(32, GPIO.OUT)  # Set up pin 32 for GPIO usage
    pwm=GPIO.PWM(32, 50)      # Set up pwm on pin 32
    pwm.start(0)             # Set initial pwm of 0
    GPIO.setwarnings(False)  # Disable GPIO warnings
    GPIO.output(32, True)
    pwm.ChangeDutyCycle(4.777)
    sleep(0.5)
    GPIO.output(32, False)
    pwm.ChangeDutyCycle(0)
    GPIO.cleanup()

startPos()
pressPos()
startPos()
pressPos()
startPos()
pressPos()
startPos()
    
  ##  May or may not need this line after sequence of execution(s) depending on other GPIO setup
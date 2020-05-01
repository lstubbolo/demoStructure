from time import sleep

try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    print('GPIO Library Cannot Be Used On This System')

try:
    print("the code below me is attempting to execute")
    GPIO.setmode(GPIO.BOARD)    # Set GPIO usage
    GPIO.setup(32, GPIO.OUT)    # Set up pin 32 for GPIO usage
    pwm = GPIO.PWM(32, 50)      # Set up pwm on pin 32
    pwm.start(0)                # Set initial pwm of 0
    GPIO.setwarnings(False)     # Disable GPIO warnings
    print("the code above me just executed")
except NameError:
    print('GPIO Library Cannot Be Used On This System')

#####    Moves finger to starting, retracted position with value of 1
def startPos():
    try:
        dutyStart = 1 / 18 + 2
        GPIO.output(32, True)
        pwm.ChangeDutyCycle(dutyStart)
        sleep(0.3)
        GPIO.output(32, False)
        pwm.ChangeDutyCycle(0)
    except NameError:
        print("*Finger-Move-Start*")
    
#####    Moves finger to the press position with value of 50
def pressPos():
    try:
        dutyPress = 50 / 18 + 2
        GPIO.output(32, True)
        pwm.ChangeDutyCycle(dutyPress)
        sleep(0.3)
        GPIO.output(32, False)
        pwm.ChangeDutyCycle(0)
    except NameError:
        print("*Finger-Move-End*")


#GPIO.cleanup()     ##  May or may not need this line after sequence of execution(s) depending on other GPIO setup
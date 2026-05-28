## JADE ARM - SIMPLE TEST CODE 
## RASBERRY PI 4B - PYTHON 

''' This code just simply moves the arm by shouelder , elbow , opens and closeds claw 
     Makes the arm wave '''

# Libraries

import time
import RPi.GPIO as GPIO

# GPIO Mode 

GPIO.setmode(GPIO.BCM)

## MOTORS CONNECTIONS 

# Shoulder Motor 
SHOULDER_RPWM = 18
SHOULDER_LPWM = 19

# ELBOW MOTOR
ELBOW_RPWM = 12
ELBOW_LPWM = 13

# SERVO PIN
CLAW_SERVO = 17

# SETUP OUTPIUTS

GPIO.setup(SHOULDER_RPWM, GPIO.OUT)
GPIO.setup(SHOULDER_LPWM, GPIO.OUT)

GPIO.setup(ELBOW_RPWM, GPIO.OUT)
GPIO.setup(ELBOW_LPWM, GPIO.OUT)

GPIO.setup(CLAW_SERVO, GPIO.OUT)

## pwm SETUP

shoulder_r = GPIO.PWM(SHOULDER_RPWM, 1000)
shoulder_l = GPIO.PWM(SHOULDER_LPWM, 1000)
elbow_r = GPIO.PWM(ELBOW_RPWM, 1000)
elbow_l = GPIO.PWM(ELBOW_LPWM, 1000)
claw = GPIO.PWM(CLAW_SERVO, 50)

shoulder_r.start(0)
shoulder_l.start(0)
elbow_r.start(0)
elbow_l.start(0)

claw.start(0)

## FUNCTIONS

def stop_all():
     shoulder_r.ChangeDutyCycle(0)
     shoulder_l.ChangeDutyCycle(0)

     elbow_r.ChangeDutyCycle(0)
     elbow_l.ChangeDutyCycle(0)

def shoulder_forward(speed):
     shoulder_r.ChangeDutyCycle(speed)
     shoulder_l.ChangeDutyCycle(0)

def shoulder_backward(speed):
     shoulder_r.ChangeDutyCycle(0)
     shoulder_l.ChangeDutyCycle(speed)

def elbow_forward(speed):
     elbow_r.ChangeDutyCycle(speed)
     elbow_l.ChangeDutyCycle(0)

# Claw Function 

def set_claw(angle):
     duty = 2 + (angle / 18)
     claw.ChangeDutyCycle(duty)

     time.sleep(0.3)
     claw.ChangeDutyCycle(0)


## MAIN MOVEMENT

try:
    print("Starting JADE ARM...")

     # Open Claw
    set_claw(20)
    
    # Left Shoulder
    print("Moving shoulder up")
    shoulder_forward(45)

    time.sleep(1.5)
    stop_all()

    time.sleep(1)

    # Move Elbow
    print("Moving Elbow")
    elbow_forward(45)
    time.sleep(1.5)
    stop_all()
    time.sleep(1)
    
    # Close Claw 
    print("Closing Claw")
    set_claw(90)

    time.sleep(1)

    # Small Dance Movement :)
    print("Dancing...")
    for i in range(3):
        shoulder_forward(50)
        time.sleep(0.3)

        shoulder_backward(50)
        time.sleep(0.3)

    stop_all()
    print("DONEE XD !")
    

# Wxit

except KeyboardInterrupt:
    print("Stopping JADE ARM...")
finally:
    stop_all()
    claw.stop()
    GPIO.cleanup()

# Made By Sarthak Tripathi 

# Libraries
import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
GPIO_TRIGGER = 4
GPIO_ECHO = 27
GPIO_GREENLIGHT = 18
GPIO_REDLIGHT = 22

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_GREENLIGHT, GPIO.OUT)
GPIO.setup(GPIO_REDLIGHT, GPIO.OUT)


def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance


# Turning led's on and off


while True:
    if distance() >= 10:
        GPIO.output(GPIO_REDLIGHT, False)
        time.sleep(.1)
        GPIO.output(GPIO_GREENLIGHT, True)
        time.sleep(.1)
    elif distance() < 10:
        time.sleep(.1)
        GPIO.output(GPIO_GREENLIGHT, False)
        time.sleep(.1)
        GPIO.output(GPIO_REDLIGHT, True)
        time.sleep(.1)
    else:
        break

# Display the distance
try:
    while True:
        dist = distance()
        print("Measured Distance = %.1f cm" % dist)
        time.sleep(1)




# Reset by pressing CTRL + C
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()


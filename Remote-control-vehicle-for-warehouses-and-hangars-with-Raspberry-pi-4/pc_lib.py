import RPi.GPIO as GPIO
from getch import getch

# Disable warnings (optional)

def calisma():
    
    GPIO.setwarnings(False)

    ENA = 27    
    ENB = 25
    IN1 = 17
    IN2 = 22
    IN3 = 23
    IN4 = 24

    # Set up the GPIO pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ENA, GPIO.OUT)
    GPIO.setup(ENB, GPIO.OUT)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)

    # Set up the PWM objects to control the motor speeds
    motor1 = GPIO.PWM(ENA, 100)
    motor2 = GPIO.PWM(ENB, 100)

    # Start the motors
    motor1.start(0)
    motor2.start(0)        
    
    try:
        while True:
         
            # Wait for the user to press a key
            key = getch()
            if key == '\x1b':  # Escape key
                key = getch()
                if key == '[':
                    key = getch()
                    if key == 'A':  # Up arrow key
                        # Set the motors to move forward and set the speed
                        GPIO.output(IN1, GPIO.HIGH)
                        GPIO.output(IN2, GPIO.LOW)
                        GPIO.output(IN3, GPIO.HIGH)
                        GPIO.output(IN4, GPIO.LOW)
                        motor1.ChangeDutyCycle(100)
                        motor2.ChangeDutyCycle(100)
                    elif key == 'B':  # Down arrow key
                        # Set the motors to move reverse and set the speed
                        GPIO.output(IN1, GPIO.LOW)
                        GPIO.output(IN2, GPIO.HIGH)
                        GPIO.output(IN3, GPIO.LOW)
                        GPIO.output(IN4, GPIO.HIGH)
                        motor1.ChangeDutyCycle(100)
                        motor2.ChangeDutyCycle(100)
                    elif key == 'D':  # Left arrow key
                        # Set the motors to turn left and set the speed
                        GPIO.output(IN1, GPIO.HIGH)
                        GPIO.output(IN2, GPIO.LOW)
                        GPIO.output(IN3, GPIO.LOW)
                        GPIO.output(IN4, GPIO.HIGH)
                        motor1.ChangeDutyCycle(100)
                        motor2.ChangeDutyCycle(100)
                    elif key == 'C':  # Right arrow 
                        # Set the motors to turn right and set the speed
                        GPIO.output(IN1, GPIO.LOW)
                        GPIO.output(IN2, GPIO.HIGH)
                        GPIO.output(IN3, GPIO.HIGH)
                        GPIO.output(IN4, GPIO.LOW)
                        motor1.ChangeDutyCycle(100)
                        motor2.ChangeDutyCycle(100)
            else:
                # Stop the motors
                GPIO.output(IN1, GPIO.LOW)
                GPIO.output(IN2, GPIO.LOW)
                GPIO.output(IN3, GPIO.LOW)
                GPIO.output(IN4, GPIO.LOW)
                motor1.ChangeDutyCycle(0)
                motor2.ChangeDutyCycle(0)

    except KeyboardInterrupt:
        # Stop the motors and clean up the GPIO pins when the user presses Ctrl+C
        motor1.stop()
        motor2.stop()
        GPIO.cleanup()
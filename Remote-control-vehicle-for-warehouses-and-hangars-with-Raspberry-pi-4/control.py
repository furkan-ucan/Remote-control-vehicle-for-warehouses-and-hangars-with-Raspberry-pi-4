import RPi.GPIO as GPIO
from flask import Flask, render_template
from time import sleep
from gpiozero import LED
from pc_lib import calisma

soru = int(input("Web Kontrol için 1 Pc Kontrolü için 2 giriniz: "))

if soru == 1:
    # Disable warnings (optional)
    GPIO.setwarnings(False)

    # Select GPIO mode
    GPIO.setmode(GPIO.BCM)
    led= LED(2)A

    # Set buzzer - pin 21 as output
    buzzer = 21 
    GPIO.setup(buzzer,GPIO.OUT)

    # Set motor driver inputs
    ENA = 27
    ENB = 25
    IN1 = 17
    IN2 = 22
    IN3 = 23
    IN4 = 24

    GPIO.setup(ENA, GPIO.OUT)
    GPIO.setup(ENB, GPIO.OUT)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)

    # Set the speed of motor 1
    motor1 = GPIO.PWM(ENA, 100)
    # Set the speed of motor 2
    motor2 = GPIO.PWM(ENB, 100)

    # Start motor 1
    motor1.start(0)
    # Start motor 2
    motor2.start(0)

    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/forward/<speed>')
    def forward(speed):
        # Turn the motors forward
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)

        # Set the speed of the motors
        motor1.ChangeDutyCycle(int(speed))
        motor2.ChangeDutyCycle(int(speed))
        
        # Set the car_moving_reverse variable to False
        global car_moving_reverse
        car_moving_reverse = False

    
        
        
        return "Moving forward at speed {}".format(speed)

    @app.route('/reverse/<speed>')
    def reverse(speed):
        # Turn the motors in reverse
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)

        # Set the speed of the motors
        motor1.ChangeDutyCycle(int(speed))
        motor2.ChangeDutyCycle(int(speed))

        # Set the flag variable to True
        global car_moving_reverse
        car_moving_reverse = True

        # Run the buzzer loop
        while car_moving_reverse:
            # Turn on the buzzer
            GPIO.output(buzzer,GPIO.HIGH)
            led.on()
            # Wait for a short amount of time
            sleep(0.5)
            # Turn off the buzzer
            GPIO.output(buzzer,GPIO.LOW)
            led.off()
            # Wait for a short amount of time
            sleep(0.5)
        
        return "Moving in reverse at speed {}".format(speed)




    @app.route('/left/<speed>')
    def left(speed):
        # Turn the motors left
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)
        # Set the speed of the motors
        motor1.ChangeDutyCycle(int(speed))
        motor2.ChangeDutyCycle(int(speed))
        # Set the car_moving_reverse variable to False
        global car_moving_reverse
        car_moving_reverse = False
        

        
        

        return "Turning left at speed {}".format(speed)

    @app.route('/right/<speed>')
    def right(speed):
        # Turn the motors right
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)
        # Set the speed of the motors
        motor1.ChangeDutyCycle(int(speed))
        motor2.ChangeDutyCycle(int(speed))
        # Set the car_moving_reverse variable to False
        global car_moving_reverse
        car_moving_reverse = False

        
        
        
        return "Turning right at speed {}".format(speed)

    @app.route('/stop')
    def stop():
        # Stop the motors
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)
        
        # Set the car_moving_reverse variable to False
        global car_moving_reverse
        car_moving_reverse = False

        
        
        
        return "Stopping"
    if __name__ == '__main__':
        app.run(host = '192.168.43.188', port= 5000, threaded=True)
else:
    calisma()




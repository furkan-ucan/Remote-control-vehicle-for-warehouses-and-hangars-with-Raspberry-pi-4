import threading

def func1():
    import RPi.GPIO as GPIO
    import time
    from gpiozero import LED

    led= LED(2) #2 numaralı GPIO pinini lede tanımla

    GPIO.setmode(GPIO.BCM)

    FLAME_PIN = 19
    MQ_PIN = 16
    BUZZER_PIN = 21

    GPIO.setup(FLAME_PIN, GPIO.IN)
    GPIO.setup(MQ_PIN, GPIO.IN)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)

    def read_flame():
        return GPIO.input(FLAME_PIN)

    def read_mq():
        return GPIO.input(MQ_PIN)

    while True:
        if read_flame() == 0:  
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            led.on()
            print("Yangın Var!!!")

        elif read_mq() == 0:
            
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            led.on()
            print("Gaz Kaçağı Var!!!")
        else:
            GPIO.output(BUZZER_PIN, GPIO.LOW)
            led.off()
        time.sleep(0)
        
def func2():
    import RPi.GPIO as GPIO
    import dht11
    import time
    import datetime

    # GPIO tipini tanımlı
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)

    # 4 numaralı pin veriyi oku
    instance = dht11.DHT11(pin=4)

    try:
        while True:
            result = instance.read()
            if result.is_valid():
                print("Last valid input: " + str(datetime.datetime.now()))

                print("Temperature: %-3.1f C" % result.temperature)
                print("Humidity: %-3.1f %%" % result.humidity)

            time.sleep(4)

    except KeyboardInterrupt:
        print("Cleanup")
        GPIO.cleanup()
        
def func3():
    import cv2

        # Kamerayı aç
    camera = cv2.VideoCapture(0)

    while True:
            # Kameradan bir görüntü yakalayın
        _, image = camera.read()
            
        

            # Resmi göster
        cv2.imshow("Camera", image)

            # Kullanıcının bir tuşa basmasını bekleyin
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

        # Kamera ve tüm pencereleri kapat
    camera.release()
    cv2.destroyAllWindows()
    
thread1=threading.Thread(target=func1)
thread2=threading.Thread(target=func2)
thread3=threading.Thread(target=func3)

thread1.start()
thread2.start()
thread3.start()

    
    


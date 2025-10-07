from gpiozero import Servo
from time import sleep
servo = Servo(17,min_pulse_width=0.5/1000,max_pulse_width=2.5/1000)
try:
    while True:
        servo.min() # 0°
        sleep(1)
        servo.mid() # 90°
        sleep(1)
        servo.max() # 180°
        sleep(1)
except KeyboardInterrupt:
    servo.mid()
    sleep(0.5)
    servo.detatch()

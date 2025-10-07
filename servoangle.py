from gpiozero import Servo
from time import sleep
servo = Servo(17,min_pulse_width=0.5/1000,max_pulse_width=2.5/1000)

try:
    while True:
        for angle in range(0, 181, 5):
            servo.value = (angle - 90) / 90.0
            sleep(0.01)
        for angle in range(180, -1, -5):
            servo.value = (angle - 90) / 90.0
            sleep(0.01)
except KeyboardInterrupt:
    servo.value = 0
    sleep(0.5)
    servo.detach()
    servo.close()

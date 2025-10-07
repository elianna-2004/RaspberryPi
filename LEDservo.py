from gpiozero import PWMLED, Servo
from time import sleep
led = PWMLED(18)
servo =Servo(17,min_pulse_width=0.5/1000,max_pulse_width=2.5/1000)
try:
    while True:
        servo.min(); led.value = 0.2; sleep(1)
        servo.mid(); led.value = 0.5; sleep(1)
        servo.max(); led.value = 1.0; sleep(1)
except KeyboardInterrupt:
    servo.mid() # park servo at neutral (≈90°)
    led.off() # turn LED off
    sleep(0.5)
    servo.detach()

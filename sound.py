import ASUS.GPIO as GPIO
import time

gpio_pin = 188

GPIO.setwarnings(False)
GPIO.setmode(GPIO.ASUS)
GPIO.setup(gpio_pin, GPIO.OUT)
p = GPIO.PWM(gpio_pin, 1400)

scales = [2400]

try:
  p.start(100)
  for i in scales:
    p.ChangeFrequency(i)
    time.sleep(0.1)
  p.stop()
finally:
  GPIO.cleanup()

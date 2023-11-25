from gpiozero import LED
from time import sleep
import psutil

led = LED(14)

while True:
    cpu = psutil.cpu_percent()
    print(cpu)
    if (cpu > 30):
        led.on()
    else:
        led.off()
    sleep(.2)
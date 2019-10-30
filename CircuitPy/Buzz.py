import time
import board
import digitalio

led = digitalio.DigitalInOut(board.D2)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    print('on')
    time.sleep(0.75)
    led.value = False
    time.sleep(0.75)
    print('off')
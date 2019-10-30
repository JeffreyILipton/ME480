import time
import board
from digitalio import DigitalInOut, Direction, Pull

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

while True:
    returned = input("LED? [Y/N]")
    if returned in 'yY':
        led.value = True
    else:
        led.value = False

    time.sleep(0.01)  # debounce delay
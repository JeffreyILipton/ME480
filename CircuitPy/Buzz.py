import time
import board
import digitalio

buzzer = digitalio.DigitalInOut(board.D2)
buzzer.direction = digitalio.Direction.OUTPUT

while True:
    buzzer.value = True
    time.sleep(0.75)
    buzzer.value = False
    time.sleep(0.75)
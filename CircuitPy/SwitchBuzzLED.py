import time
import board
import digitalio

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

buzzer = digitalio.DigitalInOut(board.D2)
buzzer.direction = digitalio.Direction.OUTPUT


switch = digitalio.DigitalInOut(board.D3)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

while True:
    if switch.value:
        led.value = True
        buzzer.value = False
        print('on')
    else:
        led.value = False
        buzzer.value = True
        print('off')
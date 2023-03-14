import machine
import neopixel



ledCount = 256
pin = 15


matrix = neopixel.NeoPixel(machine.Pin(pin), ledCount)
matrix[0] = (1, 0, 0)

from microbit import *
import am2320

i2c.init(sda=pin15, scl=pin13)
sensor = am2320.AM2320(i2c)

tempReadings = []
currTemp = 0

while True:
    if button_a.is_pressed():
        sensor.measure()
        currTemp = str(sensor.temperature())
        display.scroll(str(currTemp+"c"))
        tempReadings.append(currTemp)
    if button_b.is_pressed():
        sensor.measure()
        display.scroll(str(sensor.humidity()) + "%")
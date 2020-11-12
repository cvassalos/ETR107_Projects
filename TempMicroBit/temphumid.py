from microbit import *
import am2320

i2c.init(sda=pin15, scl=pin13)
sensor = am2320.AM2320(i2c)

tempReadings = []
currTemp = 0


def tempCompare():
    """Compares the temperature readings of the MicroBit and AM232"""
    am2320_temp = 0
    microBit_temp = 0

    sensor.measure()
    am2320 = sensor.temperature()
    microBit_temp = temperature()

    if am2320_temp > microBit_temp:
        display.scroll("AM2320 reads a higher temperature")
    if am2320_temp < microBit_temp:
        display.scroll("MicroBit reads a higher temperature")
    else:
        display.scroll("The sensors read the same temperature")


def showSavedTemps():
    """Displays recorded temperatures"""
    for i in tempReadings:
        display.scroll(i + "   ")

def recordTemp():
    """Records temperature every hour"""
    if running_time() == 3600000:
        tempReadings.append(currTemp)


while True:
    if button_a.is_pressed():
        sensor.measure()
        currTemp = str(sensor.temperature())
        currHumidity = str(sensor.humidity())
        display.scroll("Temp = " + str(currTemp+"c     ") + "Humidity = " + currHumidity)
        tempReadings.append(currTemp)

    if button_b.is_pressed():
        tempRecordings()

        recordTemp()

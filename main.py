import gpiozero
from time import sleep

DELAY_UPPER = 10
DELAY_LOWER = 20
DELAY = 2

PUMP_UPPER_PIN = 13
PUMP_LOWER_PIN = 26

PUMP_UPPER = gpiozero.DigitalOutputDevice(PUMP_UPPER_PIN, active_high = False)
PUMP_LOWER = gpiozero.DigitalOutputDevice(PUMP_LOWER_PIN, active_high = False)

LED_UPPER_PIN = 21
LED_LOWER_PIN = 20

LED_UPPER = gpiozero.LED(LED_UPPER_PIN)
LED_LOWER = gpiozero.LED(LED_LOWER_PIN)

def pump_on(pump):
    print("Pump ON pin {}".format(pump.pin))
    pump.on()

def pump_off(pump):
    pump.off()
    print("Pump OFF pin {}".format(pump.pin))

def upper_pump():
    LED_UPPER.blink()
    pump_on(PUMP_UPPER)
    sleep(DELAY_UPPER)
    pump_off(PUMP_UPPER)
    LED_UPPER.off()

def lower_pump():
    LED_LOWER.blink()
    pump_on(PUMP_LOWER)
    sleep(DELAY_LOWER)
    pump_off(PUMP_LOWER)
    LED_LOWER.off()

while True:
    upper_pump()
    sleep(DELAY)
    lower_pump()
    sleep(DELAY)










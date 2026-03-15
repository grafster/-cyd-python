import st7789_base, st7789_ext as st7789
from machine import freq, Pin, SPI

def getDisplay():
    display = st7789.ST7789(
        SPI(1, baudrate=40000000, phase=0, polarity=0),
        480, 320,
        reset=Pin(1, Pin.OUT),
        dc=Pin(2, Pin.OUT),
        cs=Pin(15, Pin.OUT),
    )

    display.init(landscape=True,mirror_y=False,inversion=False)
    backlight = Pin(27,Pin.OUT)
    backlight.on()

   # display.fill(display.color(255,0,0))
    #display.fill(display.color(0,255,0))
    #display.fill(display.color(0,0,255))
    return display
def RED():
    global range2
    range2 = strip.range(0, 1)
    range2.show_color(neopixel.colors(NeoPixelColors.RED))
def GREEN():
    global range2
    range2 = strip.range(2, 1)
    range2.show_color(neopixel.colors(NeoPixelColors.GREEN))
def OFF():
    global range2
    range2 = strip.range(0, 1)
    range2.show_color(neopixel.colors(NeoPixelColors.BLACK))
    range2 = strip.range(1, 1)
    range2.show_color(neopixel.colors(NeoPixelColors.BLACK))
    range2 = strip.range(2, 1)
    range2.show_color(neopixel.colors(NeoPixelColors.BLACK))
    range2 = strip.range(2, 1)
    range2.show_color(neopixel.colors(NeoPixelColors.BLACK))
def YELLOW():
    global range2
    range2 = strip.range(1, 1)
    range2.show_color(neopixel.colors(NeoPixelColors.YELLOW))
distance = 0
range2: neopixel.Strip = None
strip: neopixel.Strip = None
basic.show_icon(IconNames.YES)
strip = neopixel.create(DigitalPin.P0, 3, NeoPixelMode.RGB)
strip.set_brightness(225)

def on_forever():
    global distance
    pins.digital_write_pin(DigitalPin.P1, 0)
    control.wait_micros(2)
    pins.digital_write_pin(DigitalPin.P1, 1)
    control.wait_micros(10)
    pins.digital_write_pin(DigitalPin.P1, 0)
    distance = pins.pulse_in(DigitalPin.P2, PulseValue.HIGH) / 58
    basic.pause(2000)
basic.forever(on_forever)

def on_forever2():
    RED()
    basic.pause(5000)
    OFF()
    basic.pause(5000)
    YELLOW()
    basic.pause(1000)
    OFF()
    basic.pause(1000)
    GREEN()
    basic.pause(10000)
    OFF()
    basic.pause(2000)
basic.forever(on_forever2)

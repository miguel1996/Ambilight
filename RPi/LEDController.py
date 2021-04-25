from rpi_ws281x import *


class LEDController:
    LED_COUNT = 30
    LED_PIN = 18
    LED_FREQ_HZ = 800000
    LED_DMA = 10
    LED_BRIGHTNESS = 200
    LED_INVERT = False
    LED_CHANNEL = 0
    _strip = None

    def __init__(self):
        self._strip = Adafruit_NeoPixel(self.LED_COUNT, self.LED_PIN, self.LED_FREQ_HZ,
                                        self.LED_DMA, self.LED_INVERT, self.LED_BRIGHTNESS, self.LED_CHANNEL)
        self._strip.begin()

    def update_leds(self, color):
        for x in range(0, self.LED_COUNT):
            self._strip.setPixelColor(x, color)

        self._strip.show()

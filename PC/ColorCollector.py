from PIL import ImageGrab


class Modes:
    screen = 0
    keyboard = 1
    static = 2


class ColorCollector:
    _sampleRes = None
    _color = (255, 0, 0)
    _counter = 0
    _factor = 20
    _width = 1920
    _height = 1080

    def __init__(self, sample_width, sample_height):
        self.set_sample(sample_width, sample_height)

    @classmethod
    def set_sample(cls, width, height):
        if not cls._sampleRes:
            cls._width = width
            cls._height = height
            cls._sampleRes = (int(width * 0.4), int(height * 0.4), int(width * 0.8), int(height * 0.8))

    @classmethod
    def update_color(cls, mode=0):
        if mode == Modes.screen:
            cls._color = cls.__screen_color()
        elif mode == Modes.keyboard:
            cls._color = cls.__keyboard_color()
        elif mode == Modes.static:
            cls._color = cls.__static_color()
        else:
            cls._color = cls.__error_color()

    @classmethod
    def get_color(cls):
        return cls._color

    @classmethod
    def __screen_color(cls):
        image = ImageGrab.grab(bbox=cls._sampleRes).resize((cls._factor, int(cls._factor / (cls._width/cls._height))))
        color = image.quantize(1).convert("RGB").getpixel((0, 0))

        return color

    @staticmethod
    def __keyboard_color():
        raise NotImplementedError

    @staticmethod
    def __static_color():
        raise NotImplementedError

    @staticmethod
    def __error_color(error_color=(255, 0, 0)):
        return error_color

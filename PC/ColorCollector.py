from PIL import ImageGrab, Image


class Modes:
    screen = 0
    keyboard = 1
    static = 2


class ColorCollector:
    _sampleRes = None
    _color = (255, 0, 0)
    _counter = 0

    def __init__(self, sample_width, sample_height):
        self.set_sample(sample_width, sample_height)

    @classmethod
    def set_sample(cls, width, height):
        if not cls._sampleRes:
            cls._sampleRes = (0, 0, width, height)

    @classmethod
    def update_color(cls, mode=-1):
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
    def __screen_color(cls, sensitivity=10):
        image = ImageGrab.grab(bbox=cls._sampleRes)

        temp_palette = image.convert('P', palette=Image.ADAPTIVE, colors=sensitivity)
        palette = temp_palette.getpalette()

        ColorCollector._previous_palette = palette
        color_counts = sorted(temp_palette.getcolors(), reverse=True)
        colors = list()

        try:
            for i in range(sensitivity):
                palette_index = color_counts[i][1]
                dominant_color = palette[palette_index * 3:palette_index * 3 + 3]
                colors.append(tuple(dominant_color))

        except IndexError:
            return (255, 255, 255)

        return colors[0]

    @staticmethod
    def __keyboard_color():
        raise NotImplementedError

    @staticmethod
    def __static_color():
        raise NotImplementedError

    @staticmethod
    def __error_color(error_color=(255, 0, 0)):
        return error_color

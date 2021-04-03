from PIL import ImageGrab, Image


class Modes:
    screen = 0
    keyboard = 1
    static = 2


class ColorCollector:

    @classmethod
    def get_updated_color(cls, mode=0):
        if mode == Modes.screen:
            color = cls.__screen_color()
        elif mode == Modes.keyboard:
            color = cls.__keyboard_color()
        elif mode == Modes.static:
            color = cls.__static_color()
        else:
            color = cls.__error_color()

        return color

    @staticmethod
    def __screen_color(sensitivity=10):
        image = ImageGrab.grab()
        temp_palette = image.convert('P', palette=Image.ADAPTIVE, colors=sensitivity)

        palette = temp_palette.getpalette()
        color_counts = sorted(temp_palette.getcolors(), reverse=True)
        colors = list()
        for i in range(sensitivity):
            palette_index = color_counts[i][1]
            dominant_color = palette[palette_index * 3:palette_index * 3 + 3]
            colors.append(tuple(dominant_color))

        return colors[0]

    @staticmethod
    def __keyboard_color():
        raise NotImplementedError

    @staticmethod
    def __static_color():
        raise NotImplementedError

    @staticmethod
    def __error_color():
        raise NotImplementedError

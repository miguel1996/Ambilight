from PIL import ImageGrab


class DataCollector:
    _color = ""
    _stepX = 200
    _stepY = 200

    @staticmethod
    def get_color():
        return DataCollector._color

    @staticmethod
    def update_color():
        while True:
            image = ImageGrab.grab()
            x_max, y_max = image.size
            color = [0, 0, 0]
            counter = 0
            for y in range(0, y_max - DataCollector._stepY, DataCollector._stepY):
                for x in range(0, x_max - DataCollector._stepX, DataCollector._stepX):
                    pixel = list(image.getpixel((x, y)))
                    color = list(map(lambda a, b: a + b, color, pixel))
                    counter += 1

            DataCollector._color = str(list(map(lambda value: round(value / counter), color)))
            print("Average color: %s" % DataCollector._color)

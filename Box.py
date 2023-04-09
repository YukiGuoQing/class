class Box:
    def __init__(self, length, width, height):
        """
        """
        self._length = length
        self._width = width
        self._height = height

    def Volume(self):
        """

        :return:
        """
        return self._length * self._width * self._height

    def surface_area(self):
        """

        :return:
        """
        return (self._length * self._width + self._width * self._height + self._length * self._height)*2

tesseract = Box(8, 9, 10)
print(tesseract.Volume())
print(tesseract.surface_area())
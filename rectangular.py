class Rec:
    """

    """
    def __init__(self, wid, height):
        """

        :param wid:
        :param het:
        :return:
        """
        self._wid = wid
        self._height = height

    def area(self):
        """

        :return:
        """
        return self._wid * self._height

    def perimeter(self):
        """

        :return:
        """
        return self._wid*2 + self._height*2


rec_1 = Rec(328, 127)
print(rec_1.perimeter())
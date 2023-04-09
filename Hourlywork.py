class HourlyWorker:
    """

    """
    def __init__(self, name, ID, wage):
        """

        :param name:
        :param ID:
        :param wage:
        """
        self._name = name
        self._ID = ID
        self._wage = wage

facebook = HourlyWorker("Mark", 77777, .0004)
girlswhocode = HourlyWorker("Reshma", 424242, 108.13)
print(facebook._name)
print(girlswhocode._wage)
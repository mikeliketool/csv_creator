class LineBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._line = ""

    @property
    def line(self):
        return self._line

    def add_date(self, date_as_string):
        pass

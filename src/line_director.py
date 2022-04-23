from line_builder import LineBuilder


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence.
    """

    def __init__(self):
        self._builder = self.reset_builder()

    def reset_builder(self):
        self._builder = LineBuilder()

    def build_csv_line(self):
        pass

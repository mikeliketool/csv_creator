from line_builder import LineBuilder
from line_processor import LineProcessor


class LineDirector:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence.
    """

    def __init__(self):
        self.builder = self.reset_builder()
        self.line_processor = LineProcessor()

    def reset_builder(self):
        self.builder = LineBuilder()

    def build_csv_line(self, line):
        return line

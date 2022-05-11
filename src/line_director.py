from line_builder import LineBuilder
from line_processor import LineProcessor


class LineDirector:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence.
    """

    def __init__(self):
        self.reset_builder()

    def reset_builder(self):
        self.builder = LineBuilder()

    def build_csv_line(self, line):
        self.reset_builder()
        line_processor = LineProcessor(line)
        date = line_processor.get_date_from_line()
        self.builder.add_date(date)
        date = line_processor.get_payment_identifier_from_line()
        self.builder.add_transaction_value('')

from line_builder import LineBuilder
from line_processor import LineProcessor


import json


class LineDirector:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence.
    """

    def __init__(self):
        self.reset_builder()
        with open('payment_identifiers.json') as json_file:
            self.payment_identifiers = json.load(json_file)

    def reset_builder(self):
        self.builder = LineBuilder()

    def build_csv_line(self, line):
        self.reset_builder()
        line_processor = LineProcessor(line, self.payment_identifiers)
        line_processor.remove_quotes_from_line()
        print(line_processor.line)
        date = line_processor.get_date_from_line()
        self.builder.add_date(date)
        payment_identifier = line_processor.get_payment_identifier_from_line()
        self.builder.add_payment_identifier(payment_identifier)
        self.builder.add_transaction_value('')

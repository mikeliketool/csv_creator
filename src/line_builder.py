class LineBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._line = ""

    @property
    def line(self):
        return self._line

    def _add_string_to_line(self, input_string):
        if isinstance(input_string, str) and len(input_string) > 0:
            self._line += f"{input_string},"

    def add_date(self, date_as_string):
        self._add_string_to_line(date_as_string)

    def add_payment_identifier(self, payment_identifier):
        self._add_string_to_line(payment_identifier)

    def add_transaction_value(self, transaction_value):
        if len(transaction_value) > 0:
            self._line += "transaction_value"
        if len(self._line) > 0:
            self._line += "\n"

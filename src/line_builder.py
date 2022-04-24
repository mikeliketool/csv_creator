class LineBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._line = ""

    @property
    def line(self):
        return self._line

    def add_date(self, date_as_string):
        if len(date_as_string) > 0:
            self._line += f"{date_as_string},"

    def add_transaction_value(self, transaction_value):
        if len(transaction_value) > 0:
            self._line += "transaction_value"
        if len(self._line) > 0:
            self._line += "\n"

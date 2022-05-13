class LineProcessor:
    def __init__(self, line, payment_identifiers={}):
        self.line = line
        self.acceptable_month_values = {'Jan': None, 'Feb': None, 'Mar': None, 'Apr': None, 'May': None, 'Jun': None,
                                        'Jul': None, 'Aug': None, 'Sep': None, 'Oct': None, 'Nov': None, 'Dec': None}
        self.acceptable_day_values = dict((i, None) for i in range(1, 32))
        self.payment_identifiers = payment_identifiers

    def get_date_from_line(self):
        date = ''
        if isinstance(self.line, str):
            month = self.line[1:4]
            day = self.line[5:7]

        try:
            if str(month) in self.acceptable_month_values and int(day) in self.acceptable_day_values:
                date = f"{month} {day}"
        except Exception:
            print('Could not process the date for this line')

        return date

    def get_payment_identifier_from_line(self):
        for payment_identifier in self.payment_identifiers:
            if payment_identifier in self.line:
                return payment_identifier
        return ''

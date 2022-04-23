class LineProcessor:
    def __init__(self, line):
        self.line = line
        self.acceptable_month_values = {'Jan': None, 'Feb': None, 'Mar': None, 'Apr': None, 'May': None, 'Jun': None,
                                        'Jul': None, 'Aug': None, 'Sep': None, 'Oct': None, 'Nov': None, 'Dec': None}
        self.acceptable_day_values = dict((i, None) for i in range(1, 32))

    def extract_date_from_line(self):
        date = ''
        if isinstance(self.line, str):
            month = self.line[1:4]
            day = self.line[5:7]

        if month in self.acceptable_month_values:
            date = f"{month} "
        if int(day) in self.acceptable_day_values:
            date += day

        return date

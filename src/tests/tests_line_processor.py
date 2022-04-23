from line_processor import LineProcessor


class TestsLineProcessor:
    def test_dates_as_expected(self):
        line = '"Mar 14 somemore data"'
        line_processor = LineProcessor(line)
        assert line_processor.extract_date_from_line() == "Mar 14"

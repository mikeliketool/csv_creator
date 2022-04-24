import pytest

from line_processor import LineProcessor


class TestsLineProcessor:
    def test_dates_as_expected(self):
        line = '"Mar 14 somemore data"'
        line_processor = LineProcessor(line)
        assert line_processor.extract_date_from_line() == "Mar 14"

    @pytest.mark.parametrize(
        'month',
        ['MMM', 123, None, 'adfafadsfasdfaf']
    )
    def test_month_invalid(self, month):
        line = f'"{month} 14 somemore data"'
        line_processor = LineProcessor(line)
        assert line_processor.extract_date_from_line() == ""

    @pytest.mark.parametrize(
        'day',
        ['MMM', 0, None, 'adfafadsfasdfaf', 32]
    )
    def test_day_invalid(self, day):
        line = f'"Mar {day} somemore data"'
        line_processor = LineProcessor(line)
        assert line_processor.extract_date_from_line() == ""

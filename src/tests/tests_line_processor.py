import pytest

from line_processor import LineProcessor


mock_date = "Mar 14"
highway_identifier = "HIGHWAY 407-ETR"


class TestsLineProcessorExtractDateFromLine:
    def test_dates_as_expected(self):
        line = f'{mock_date} somemore data'
        line_processor = LineProcessor(line)
        assert line_processor.get_date_from_line() == mock_date

    @pytest.mark.parametrize(
        'month',
        ['MMM', 123, None, 'adfafadsfasdfaf']
    )
    def test_month_invalid(self, month):
        line = f'{month} 14 somemore data'
        line_processor = LineProcessor(line)
        assert line_processor.get_date_from_line() == ""

    @pytest.mark.parametrize(
        'day',
        ['MMM', 0, None, 'adfafadsfasdfaf', 32]
    )
    def test_day_invalid(self, day):
        line = f'Mar {day} somemore data'
        line_processor = LineProcessor(line)
        assert line_processor.get_date_from_line() == ""


class TestsLineProcessorExtractPaymentIdentifierFromLine:
    mock_line = f'{mock_date} {highway_identifier}'

    def test_json_is_none(self):
        line_processor = LineProcessor(self.mock_line)
        assert line_processor.get_payment_identifier_from_line() == ""

    def test_json_has_a_match(self):
        line_processor = LineProcessor(self.mock_line, {highway_identifier: highway_identifier})
        assert line_processor.get_payment_identifier_from_line() == highway_identifier

    def test_json_does_not_have_a_match(self):
        line_processor = LineProcessor(self.mock_line, {"Test": "Test"})
        assert line_processor.get_payment_identifier_from_line() == ''


class TestsLineProcessorRemoveQuotesFromLine:
    def test_line_starts_and_ends_in_quotes(self):
        line = f'"{mock_date} 1234"'
        line_processor = LineProcessor(line)
        line_processor.remove_quotes_from_line()
        assert line_processor.line == f'{mock_date} 1234'

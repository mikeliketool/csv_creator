from line_builder import LineBuilder

mock_date = "Mar 14"


class TestsLineBuilder:
    def test_line_empty_by_default(self):
        assert LineBuilder().line == ''

    def test_date_is_cleared_if_payment_identifier_is_empty(self):
        line_builder = LineBuilder()
        line_builder.add_date(mock_date)
        assert line_builder.line == f'{mock_date},'
        line_builder.add_payment_identifier('')
        assert line_builder.line == ''


class TestLineBuilderAddDate:
    def test_when_none(self):
        line_builder = LineBuilder()
        line_builder.add_date(None)
        assert line_builder.line == ''

    def test_not_string(self):
        line_builder = LineBuilder()
        line_builder.add_date(1234)
        assert line_builder.line == ''

    def test_is_string(self):
        line_builder = LineBuilder()
        line_builder.add_date(mock_date)
        assert line_builder.line == f'{mock_date},'


class TestLineBuilderAddPaymentIdentifier:
    def test_when_none(self):
        line_builder = LineBuilder()
        line_builder.add_payment_identifier(None)
        assert line_builder.line == ''

    def test_not_string(self):
        line_builder = LineBuilder()
        line_builder.add_payment_identifier(1234)
        assert line_builder.line == ''

    def test_is_string(self):
        payment_identifier = "HIGHWAY 407"
        line_builder = LineBuilder()
        line_builder.add_payment_identifier(payment_identifier)
        assert line_builder.line == f'{payment_identifier},'

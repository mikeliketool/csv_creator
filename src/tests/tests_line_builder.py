from line_builder import LineBuilder


class TestsLineBuilder:
    def test_line_empty_by_default(self):
        assert LineBuilder().line == ''


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
        date = "Mar 14"
        line_builder = LineBuilder()
        line_builder.add_date(date)
        assert line_builder.line == f'{date},'


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

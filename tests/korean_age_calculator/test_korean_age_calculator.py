import sys
import korean_age_calculator


def test_ping():
    sys.argv = ['foo', '10']
    korean_age_calculator.ping()


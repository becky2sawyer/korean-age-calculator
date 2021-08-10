import korean_age_calculator as kac


def test_how_korean_age():
    korean_age = kac.how_korean_age(year_of_birth=1999, current_year=2021)
    assert korean_age == 23

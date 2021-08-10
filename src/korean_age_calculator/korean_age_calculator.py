"""korean_age_calculator 모듈.

한국 나이의 단위는 ``살``입니다. 한국 사람들은 태어나면 바로 1살이 됩니다.
이를 기반으로 당신이 태어난 연도를 알려주시면 한국 사람들이 갖고 있는 한국식 나이를 알려드립니다.

The unit of Korean age is 'sal'. Koreans turn 1 year old right after they are born.
Based on this, if you tell me the year you were born, I will tell you the Korean age that Koreans have.

Example:
    ``korean_age_calculator`` 사용법은 아래와 같습니다.

        $ pip install korean-age-calculator
        $ korean-age-calculator 1988
        >>> Born in 1988, you are 34 살(years old) in Korean style.

"""
import sys
import datetime


def how_korean_age(year_of_birth: int, current_year=datetime.datetime.now().year) -> int:
    """태어는 연도를 입력하면 한국 나이를 계산하여 알려드립니다.

    Args:
        year_of_birth: 태어난 연도
        current_year: 기준년도 - 입력하지 않으면 현 연도(datetime.datetime.now().year)

    Returns:
        한국 나이
    """
    korean_age = current_year - year_of_birth + 1
    return korean_age


def main():
    try:
        year_of_birth = int(sys.argv[1])
        korean_age = how_korean_age(year_of_birth)
        print(f'Born in {year_of_birth}, you are {korean_age} 살(years old) in Korean style.')
    except (ValueError, IndexError) as e:
        print("please enter your year of birth:", e)


if __name__ == "__main__":
    main()

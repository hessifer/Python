from datetime import date


class Birthday:
    """
    The Birthday class provides behaviors for dealing with a person's
    birthday.
    """
    gregorian_cal = date.fromisoformat("1582-10-15")

    def __init__(self, birth_yyyy: str, birth_mm: str, birth_dd: str):
        self.current_date = date.today()
        if int(birth_yyyy) > self.current_date.year:
            raise ValueError("Birth year cannot be greater than current year.")

        self.bdate = date.fromisoformat(f"{birth_yyyy}-{birth_mm}-{birth_dd}")
        if self.bdate < Birthday.gregorian_cal:
            raise ValueError("Only birth years since Gregorian calendar are"
                             "supported.")

        self.birth_year = birth_yyyy
        self.birth_month = birth_mm
        self.birth_day = birth_dd

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """These extra days occur in each year which is an integer
        multiple of 4 (except for years evenly divisible by 100,
        which are not leap years unless evenly divisible by 400
        """
        if year % 4 == 0:
            if year % 100 == 0 and not year % 400 == 0:
                return False
        else:
            return False

    def days_since_birth(self) -> int:
        timedelta = self.current_date - self.bdate
        total_leap_days = 0

        for year in range(int(self.birth_year), self.current_date.year + 1):
            if Birthday.is_leap_year(year):
                total_leap_days += 1
        return timedelta.days + total_leap_days


if __name__ == '__main__':
    bob = Birthday('1983', '11', '06')
    sally = Birthday('1968', '02', '03')
    print(f"Bob, it has been {bob.days_since_birth():,} days since "
          f"your were born.")
    print(f"Sally, it has been {sally.days_since_birth():,} days "
          f"since your were born.")
    # raise an error
    # fail = Birthday('2022', '11', '04')
    # print(f"Fail, it has been {fail.days_since_birth():,} days since "
    #      f"your were born.")

    # raise an error
    # fail2 = Birthday('1580', '09', '05')
    # print(f"Fail2, it has been {fail2.days_since_birth():,} days "
    #       f"since your were born.")

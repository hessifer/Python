def days_in_month(year, month):
    return 30


def next_day(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < days_in_month(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year +1, 1, 1
        else:
            return year, month +1, 1


if __name__ == '__main__':
    def test():
        # test with 30-day months
        assert daysBetweenDates(2013, 1, 1, 2013, 1, 1) == 0
        assert daysBetweenDates(2013, 1, 1, 2013, 1, 2) == 1
        assert nextDay(2013, 1, 1) == (2013, 1, 2)
        assert nextDay(2013, 4, 30) == (2013, 5, 1)
        assert nextDay(2012, 12, 31) == (2013, 1, 1)
        print("Tests finished.")

test()
class Mathematician:
    def square_nums(self, nums):
        """Returns list of squared numbers"""
        return [num ** 2 for num in nums]

    def remove_positives(self, nums):
        """Returns list without positive numbers"""
        return [num for num in nums if num <= 0]

    def filter_leaps(self, years):
        """Returns only leap years from the list"""

        def is_leap(year):
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

        return [year for year in years if is_leap(year)]


# Тестування
m = Mathematician()
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
import unittest


def is_happy(number: int) -> bool:
    """Tells if `number` is happy"""

    if number == 1:
        return True

    elif number ** 2 < 10:
        return False

    else:

        digits = []
        digit = 0
        i = 10

        while True:

            digit = int((number - int(number / i) * i - digit) / (i / 10))

            if number - int(i / 10) < 0:
                break

            digits.append(digit)
            i *= 10

        squared_digits = [d ** 2 for d in digits]

        return is_happy(sum(squared_digits))


class HappyNumberSpec(unittest.TestCase):

    def test_happy_numbers(self):
        some_happy_numbers = [1, 7, 49, 97, 130, 10]
        for n in some_happy_numbers:
            self.assertTrue(is_happy(n), f'{n} is happy!')

    def test_not_happy_numbers(self):
        some_happy_numbers = [2, 11]
        for n in some_happy_numbers:
            self.assertFalse(is_happy(n), f'{n} is not happy!')

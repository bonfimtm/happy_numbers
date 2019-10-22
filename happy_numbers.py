import unittest
from typing import List


def separate_digits(number: int) -> List[int]:
    i = 1
    digits = []
    while True:
        a = int(number / i)
        i *= 10
        b = int(number / i) * 10
        digit = a - b
        if a == 0:
            break
        digits.append(digit)
    digits.reverse()
    return digits


def is_happy(number: int) -> bool:
    """Tells if `number` is happy"""
    if number == 1:
        return True
    elif number ** 2 < 10:
        return False
    else:
        digits = separate_digits(number)
        squared_digits = [d ** 2 for d in digits]
        return is_happy(sum(squared_digits))


class HappyNumbersSpec(unittest.TestCase):

    def test_separate_digits(self):
        self.assertEqual([1, 2, 3], separate_digits(123))

    def test_separate_digits_with_zero_digit(self):
        self.assertEqual([9, 0, 8, 0], separate_digits(9080))

    def test_happy_numbers(self):
        some_happy_numbers = [1, 7, 49, 97, 130, 10]
        for n in some_happy_numbers:
            self.assertTrue(is_happy(n), f'{n} is happy!')

    def test_not_happy_numbers(self):
        some_happy_numbers = [2, 11]
        for n in some_happy_numbers:
            self.assertFalse(is_happy(n), f'{n} is not happy!')


if __name__ == '__main__':
    unittest.main()

import unittest

from sol import *

class TestPhoneNumberValidation(unittest.TestCase):

    def test_valid_phone_numbers(self):
        valid_numbers = [
            "+123456789012345",
            "1234567890",
            "+1987654321",
            "9876543210"
        ]
        for number in valid_numbers:
            self.assertTrue(is_valid_phone_number(number))

    def test_invalid_phone_numbers(self):
        invalid_numbers = [
            "+012345678901234",  # начинается с 0
            "12345678901234567890",  # слишком длинный
            "abcd1234567",  # не цифровой
            "+12345abc678"  # содержит буквы
        ]
        for number in invalid_numbers:
            print(number)
            self.assertFalse(is_valid_phone_number(number))

if __name__ == '__main__':
    unittest.main()


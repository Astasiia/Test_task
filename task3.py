import unittest

# for test
class TestSumDigits(unittest.TestCase):

    def test_sum_digits1(self):
        valueEx1 = 2347623
        sumEx1 = eval('2+3+4+7+6+2+3')
        result = sumDigits(valueEx1)
        self.assertEqual(result, sumEx1)

    def test_sum_digits2(self):
        valueEx2 = 1903610
        sumEx2 = eval('1+9+0+3+6+1+0')
        result = sumDigits(valueEx2)
        self.assertEqual(result, sumEx2)


# function "sumDigits"
def sumDigits(value):
    if (value // 10) == 0:
        return value
    else:
        return (value % 10) + sumDigits(value // 10)


if __name__ == '__main__':
    unittest.main()
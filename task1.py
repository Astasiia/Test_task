import unittest

# for test
class TestPriceCheck(unittest.TestCase):

    def test_price_check1(self):
        productsEx1 = ['rice', 'sugar', 'wheat', 'cheese']
        productPricesEx1 = [16.89, 56.92, 20.89, 345.99]
        productSoldEx1 = ['rice', 'cheese']
        soldPriceEx1 = [18.99, 400.89]
        result = priceCheck(productsEx1, productPricesEx1, productSoldEx1, soldPriceEx1)
        # print(result)
        self.assertEqual(result, 2)

    def test_price_check2(self):
        productsEx2 = ['eggs', 'milk', 'cheese']
        productPricesEx2 = [2.89, 3.29, 5.79]
        productSoldEx2 = ['eggs', 'eggs', 'cheese', 'milk']
        soldPriceEx2 = [2.89, 2.99, 5.97, 3.29]
        result = priceCheck(productsEx2, productPricesEx2, productSoldEx2, soldPriceEx2)
        # print(result)
        self.assertEqual(result, 2)


# function "priceCheck"
def priceCheck(products, productPrices, productSold, soldPrice):
    countError = 0
    dictionary = dict(zip(products, productPrices))
    for i, name in enumerate(productSold):
        diff = float(dictionary.get(name)) - soldPrice[i]
        if diff != 0:
            countError = countError + 1
    return countError    


if __name__ == '__main__':
    unittest.main()


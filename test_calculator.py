"""
    Testing the calculator functionalities.
"""


import calculator


class TestCalculator:


    def test_addition(self):
        assert 4 == calculator.add(2, 2)


    def test_subtraction(self):
        assert 2 == calculator.subtract(5, 3)


    def test_multiplication(self):
        assert 10 == calculator.multiplication(5, 2)


    def test_division(self):
        assert 2 == calculator.division(10, 5)



    def test_division(self):
        assert 4 == calculator.division(12, 3)


import pytest

from src.calculations import *
class TestCalculations:

    calc = Calculations()
    def test_add(self):
        res = self.calc.add(n1=10,n2=5)
        assert res == 15, 'Addition Err'

    def test_sub(self):
        res = self.calc.sub( n1=10, n2=5)
        assert res == 5, 'Sub Err'

    def test_mul(self):
        res = self.calc.mul( n1=10, n2=5)
        assert res == 50, 'mul Err'

    def test_div(self):
        res = self.calc.div( n1=10, n2=5)
        assert res == 2, 'div Err'

    @pytest.mark.skip()
    def test_ne(self):
        res = self.calc.ne(n1=10, n2=10)
        assert  res==True, 'ne Err'

    def test_driver(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(n1=10,n2=0)
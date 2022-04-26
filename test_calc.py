import pytest
from pythoncode.calcilator import Calculator
class TestCalc:
    def setup_class(self):
        self.calc=Calculator()
        print("开始计算")
    def teardown_class(self):
        print("计算结束")
    @pytest.mark.parametrize("a,b,expect",[
        (1,2,3),
        (2,4,7)
    ])
    def test_add(self,a,b,expect):
        assert expect==self.calc.add(a,b)

    @pytest.mark.parametrize("a,b,expect", [
        (1, 2, 3),
        (2, 4, 7)
    ])
    def test_sup(self,a,b,expect):
        assert expect==self.calc.sub(a,b)

    @pytest.mark.parametrize("a,b,expect", [
        (1, 2, 3),
        (2, 4, 7)
    ])
    def test_mul(self,a,b,expect):
        assert expect==self.calc.mul(a,b)

    @pytest.mark.parametrize("a,b,expect", [
        (1, 2, 3),
        (2, 4, 7)
    ])
    def test_div(self,a,b,expect):
        assert expect==self.calc.div(a,b)

if __name__ == '__main__':
    pytest.main()
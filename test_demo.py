import pytest
class Test_demo():
    def test_one(self):
        a=5
        b=1
        assert a!=b
        print("这是我的第一个测试用例")
    @pytest.mark.parametrize("a,b",[
        (10,10),
        (12,12),
        (2,5)
    ],ids=["first","second","third"]) #ids给参数取别名
    def test_tow(self,a,b):
        assert a==b
        print("这是我的第二个测试用例")

if __name__ == '__main__':
    pytest.main()


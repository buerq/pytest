import pytest
def setup_module():
    print("setu：整个test_setup_teardown模块只执行一次")
def teardown_module():
    print("teardown：整个test_setup_teardown模块只执行一次")
class TestClass():
    def setup_class(self):
        print("setup:类里面的所有用例都开始执行")
    def setup_method(self):
        print("setup:每个用例开始都执行")
    def teardown_method(self):
        print("teardown:每个用例结束都执行")
    def test_one(self):
        print("这是第一个测试用例")
    def test_two(self):
        print("这是第二个测试用例")
    def teardown_class(self):
        print("teardown:类里面的所有用例都结束执行")
def setup_function():
    print("setup:不在类中的测试用例开始的时候都会执行")
def teardown_function():
    print("teardown:不在类中的测试用例结束的时候都会执行")
def test_three():
    print("test_three")

if __name__ == '__main__':
    pytest.main()
import pytest

def function1(var1):
    return var1 + 1

def function2(var2):
    return var2 * 2

def functionTrue():
    return True

def functionFalse():
    return False

#subclass
class MyTest(pytest.TestCase):
    def test(self):
        self.assertEqual(function1(3), 4)

    def test2(self):
        self.assertEqual(function2(2), 4)

    def test3(self):
        self.assertFalse(functionFalse())

    def test4(self):
        self.assertTrue(functionTrue())

    def test6(self):
        self.assertRaises(functionTrue())

if __name__ == '__main__':
    pytest.main()

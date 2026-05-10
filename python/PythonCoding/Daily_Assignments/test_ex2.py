import unittest


# 1. Basic Test Case
class TestMath(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(2 + 3, 5)


# 2. Setup and Teardown
class TestList(unittest.TestCase):

    def setUp(self):
        self.my_list = [1, 2, 3]

    def tearDown(self):
        print("Test completed")

    def test_list_length(self):
        self.assertEqual(len(self.my_list), 3)


# 3. Multiple Assertions
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual("hello".upper(), "HELLO")

    def test_isupper(self):
        self.assertFalse("hello".isupper())


# 4. Exception Testing
class TestException(unittest.TestCase):

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            result = 10 / 0


# 5. Test Suite Execution
class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(5 + 5, 10)


class TestSubtract(unittest.TestCase):

    def test_subtract(self):
        self.assertEqual(10 - 5, 5)


# Creating Test Suite
suite = unittest.TestSuite()

suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAdd))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSubtract))

# Running the Suite
runner = unittest.TextTestRunner()
runner.run(suite)


# Main Execution
if __name__ == "__main__":
    unittest.main()
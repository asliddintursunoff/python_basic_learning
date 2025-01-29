import unittest
import main
class Testing(unittest.TestCase):
    def test_multiply(self):
        param = 1
        result = main.multiply(param)
        self.assertEqual(result , 5)
    def test_string(self):
        param2 = "hello"
        answer2 = main.multiply(param2)
        self.assertTrue(isinstance(answer2,ValueError))
    def test_none(self):
        param = None
        answer = main.multiply(param)
        self.assertEqual(answer,"enter true number")

if __name__ == '__main__':
    unittest.main()

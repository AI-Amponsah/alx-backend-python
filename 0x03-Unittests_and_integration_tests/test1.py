import unittest

def summation(a, b):

    return a + b


class Test1(unittest.TestCase):
    def setUp(self):
        #Arrange
        self.a = 12
        self.b = 7
    def test_funct1(self):
        #act
        result = summation(self.a, self.b)
        #assert
        self.assertEqual(result, self.a + self.b)

    def test_funct2(self):
        #act
        result = summation(self.b, self.a)
        #assert
        self.assertEqual(result, self.a + self.b)




if __name__ == "__main__":
    unittest.main()
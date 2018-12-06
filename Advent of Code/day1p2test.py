import unittest
import day1p2

class TestStringMethods(unittest.TestCase):

    def test_simplecase(self):
        simple_list = [+3, +3, +4, -2, -4]*2
        expected = 10
        actual = day1p2.find_duplicate(simple_list)        
        
        self.assertEqual(expected, actual)        

if __name__ == '__main__':
    unittest.main()

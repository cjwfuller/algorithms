import unittest
import lis

class TestLis(unittest.TestCase):
    def test_basic(self):
        l = lis.Lis()
        answer = [[0, 4, 6, 9, 13, 15], [0, 2, 6, 9, 13, 15], [0, 4, 6, 9, 11, 15], [0, 2, 6, 9, 11, 15]]
        self.assertEquals(answer, l.lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))

if __name__ == '__main__':
    unittest.main()
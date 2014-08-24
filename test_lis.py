import unittest
import lis

class TestLis(unittest.TestCase):

    def test_empty_sequence_is_lis(self):
        """The empty sequence is the only LIS"""
        answer = [[]]

        self.assertEquals(answer, lis.lis([]))

    def test_single_element_is_lis(self):
        """A single element sequence is the only LIS"""
        answer = [[10]]

        self.assertEquals(answer, lis.lis([10]))

    def test_itself_is_lis(self):
        """When there is an array that is itself the only LIS, it's returned"""
        answer = [[1, 2, 3, 4]]

        self.assertEquals(answer, lis.lis([1, 2, 3, 4]))

    def test_single_lis(self):
        """When there is one LIS, it is returned"""
        answer = [[0, 1, 8, 9]]

        self.assertEquals(answer, lis.lis([0, 10, 1, 8, 9]))

    def test_multiple_lis(self):
        """When there is more than one LIS, all LISs are returned"""
        answer = [
            [0, 4, 6, 9, 13, 15],
            [0, 2, 6, 9, 13, 15],
            [0, 4, 6, 9, 11, 15],
            [0, 2, 6, 9, 11, 15]
        ]

        self.assertEquals(answer, lis.lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))

    def test_larger_element_before_single_lis(self):
        """When there is a large element before a single LIS, LIS is returned"""
        answer = [[1, 8, 9]]

        self.assertEquals(answer, lis.lis([11, 10, 1, 8, 9]))

if __name__ == '__main__':
    unittest.main()
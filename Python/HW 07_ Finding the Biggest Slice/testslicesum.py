import unittest
from slicesum import prefix, suffix
from slicesum import slicesum as slicesum

class TestSliceSum(unittest.TestCase):
    def testprefix1(self):
        L = [-1,-1,1,1,1,-1]
        self.assertEqual(prefix(L), (1, 5))

    def testprefix2(self):
        L = [1,1,1,-3,1,-2]
        self.assertEqual(prefix(L), (3, 3))

    def testprefixallnegative(self):
        L = [-1, -1, -1]
        self.assertEqual(prefix(L), (0, 0))

    def testprefixempty(self):
        L = [-1, -1, -1, 1, 1]
        self.assertEqual(prefix(L), (0, 0))

    def testprefixall(self):
        L = [1,-2,1,1,1]
        self.assertEqual(prefix(L), (2, 5))

    def testprefixtiegoestolongest(self):
        L = [-1, 1, 2, -2, 1, 1, -3]
        self.assertEqual(prefix(L), (2, 6))

    def testsuffix1(self):
        L = [-1,1,1,1,-1,-1]
        self.assertEqual(suffix(L), (1, 1))

    def testsuffix2(self):
        L = [1,-1,-3,1,1,1]
        self.assertEqual(suffix(L), (3, 3))

    def testsuffixallnegative(self):
        L = [-1,-1,-1]
        self.assertEqual(suffix(L), (0, 3))

    def testsuffixempty(self):
        L = [1,1,-3]
        self.assertEqual(suffix(L), (0, 3))

    def testsuffixall(self):
        L = [2,2,2,-2,2,2]
        self.assertEqual(suffix(L), (8, 0))

    def testsuffixtiegoestolongest(self):
        L = [-5, 1, -1, 2, -2, 3, -3]
        self.assertEqual(suffix(L), (0,1))

    def testslicesum1(self):
        L = [-1] * 100
        self.assertEqual(slicesum(L), (0, 0, 0))
        L[20] = 5
        self.assertEqual(slicesum(L), (5, 20, 21))
        L[22] = 5
        self.assertEqual(slicesum(L), (9, 20, 23))

    def testslicesum2(self):
        L = [1, 0, -2, 3, 4, 0, 0, -2, 3, -4]
        self.assertEqual(slicesum(L), (8, 3, 9))

    def testslicesumtiegoestolongest(self):
        L = [-10, 1, -1, 5, -1, 1, -10]
        self.assertEqual(slicesum(L), (5, 1, 6))

    def testslicesumtiegoestolongest2(self):
        L = [3, -100, 1, 1, 1]
        self.assertEqual(slicesum(L), (3, 2, 5))

    def testslicesumtiegoestoleftest(self):
        L = [-10, 1, 1, 1, -100, 1, 1, 1, -10]
        self.assertEqual(slicesum(L), (3, 1, 4))

    def testslicesumbiginstance(self):
        n = 10000
        L = [1] * n
        self.assertEqual(slicesum(L), (n, 0, n))

if __name__ == '__main__':
    unittest.main()

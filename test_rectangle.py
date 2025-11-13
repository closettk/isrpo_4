import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_1(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_2(self):
        res = area(10, 5)
        self.assertEqual(res, 50)

    def test_3(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_4(self):
        res = perimeter(10, 5)
        self.assertEqual(res, 30)

    def test_5(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)


if __name__ == "__main__":
    unittest.main()

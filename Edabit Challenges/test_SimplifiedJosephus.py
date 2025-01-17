import unittest
from SimplifiedJosephus import simplified_josephus

class TestSimplifiedJosephus(unittest.TestCase):
    def test_single_person(self):
        self.assertEqual(simplified_josephus(1), 1)

    def test_eight_people(self):
        self.assertEqual(simplified_josephus(8), 1)

    def test_forty_one_people(self):
        self.assertEqual(simplified_josephus(41), 19)

    def test_five_people(self):
        self.assertEqual(simplified_josephus(5), 3)

    def test_ten_people(self):
        self.assertEqual(simplified_josephus(10), 5)

    def test_twenty_people(self):
        self.assertEqual(simplified_josephus(20), 9)

if __name__ == "__main__":
    unittest.main()
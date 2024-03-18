import unittest
from guitar import Guitar


class GuitarTest(unittest.TestCase):
    def setUp(self):
        self.guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
        self.guitar2 = Guitar("Another Guitar", 2013, 1000.00)

    def test_get_age(self):
        self.assertEqual(self.guitar1.get_age(2022), 100)
        self.assertEqual(self.guitar2.get_age(2022), 9)

    def test_is_vintage(self):
        self.assertTrue(self.guitar1.is_vintage(2022))
        self.assertFalse(self.guitar2.is_vintage(2022))


if __name__ == "__main__":
    unittest.main()

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_read_csv(self):
        self.assertIsNotNone(utils.read_csv)

    def test_write_csv(self):
        self.assertIsNotNone(utils.write_csv)

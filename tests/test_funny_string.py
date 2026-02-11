import unittest
from funny_string import funny_string

class TestFunnyString(unittest.TestCase):
  def test_funny(self):
        self.assertEqual(funny_string("acxz"), "Funny")
  def test_not_funny(self):
        self.assertEqual(funny_string("bcxz"), "Not Funny")

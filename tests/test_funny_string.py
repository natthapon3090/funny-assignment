import unittest
from funny_string import funny_string

class TestFunnyString(unittest.TestCase):
  def test_funny(self):
        self.assertEqual(funny_string("acxz"), "Funny")
  def test_not_funny(self):
        self.assertEqual(funny_string("bcxz"), "Not Funny")

  def test_single_character(self):
          self.assertEqual(funny_string("a"), "Funny")
    
  def test_two_characters(self):
          self.assertEqual(funny_string("aa"), "Funny")
    
  def test_repeated_characters(self):
        self.assertEqual(funny_string("aaa"), "Funny")

  def test_long_not_funny(self):
        self.assertEqual(funny_string("abcdba"), "Not Funny")

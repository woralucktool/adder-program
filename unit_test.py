import unittest

def add_numbers(a, b):
  """Adds two numbers and returns the sum."""
  return a + b

class AddNumbersTest(unittest.TestCase):
  def test_add_positive_numbers(self):
    result = add_numbers(5, 3)
    self.assertEqual(8, result)

  def test_add_negative_numbers(self):
    result = add_numbers(-2, -4)
    self.assertEqual(-6, result)

  def test_add_zero(self):
    result = add_numbers(10, 0)
    self.assertEqual(10, result)

if __name__ == "__main__":
  unittest.main()

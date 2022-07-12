import unittest

class UnitTestLearningTests(unittest.TestCase):

  def setUp(self):
    self.a = 2

  def tearDown(self):
    self.a = 22

  @unittest.skip("demonstrating skipping")
  def test_nothing(self):
    self.fail("shouldn't happen")

  @unittest.expectedFailure
  def test_fail(self):
    self.assertEqual(1, 0, "broken")

  def test_skipIfCondition(self):
    """
    Test that a is 2 as set in setup()
    """
    self.assertLess(self.a, 20, "something is wrong")
    if self.a == 22:
      self.skipTest("external resource not available")

  def test_isEven(self):
    with self.subTest("a = {0}".format(self.a)):
      self.assertEqual(self.a % 2, 0)

  def test_split(self):
    s = 'hello world'
    self.assertEqual(s.split(), ['hello', 'world'])
    # check that s.split fails when the separator is not a string
    with self.assertRaises(TypeError):
      s.split(2)

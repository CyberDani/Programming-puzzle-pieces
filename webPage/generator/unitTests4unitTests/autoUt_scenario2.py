from modules.unitTests.autoUnitTest import AutoUnitTest

class Tests2UsingAutoUnitTest(AutoUnitTest):

  def test_quickPass1(self):
    self.assertTrue(True)

  def test_quickPass2(self):
    self.assertEqual(2, 2)

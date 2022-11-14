from modules.unitTests.autoUnitTest import AutoUnitTest

class Tests1UsingAutoUnitTest(AutoUnitTest):

  def test_quickPass1(self):
    self.assertTrue(True)

  def test_quickPass2(self):
    self.assertEqual(2, 2)

  def test_quickPass3(self):
    self.assertIsNone(None)

  def test_quickFail1(self):
    self.assertFalse(True)

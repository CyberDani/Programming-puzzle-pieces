import unittest
import sys

sys.path.append('..')

from modules import counter

class CounterTests(unittest.TestCase):

  def test_getNextInt(self):
    count = counter.SimpleCounter(4)
    val = count.getNextInt()
    self.assertEqual(val, 4)
    self.assertEqual(count.getNextInt(), 5)
    self.assertEqual(count.getNextInt(), 6)
    self.assertEqual(count.getNextInt(), 7)
    self.assertEqual(count.getNextInt(), 8)
    self.assertEqual(count.getNextInt(), 9)
    self.assertEqual(count.getNextInt(), 10)
    val = count.getNextInt()
    self.assertEqual(val, 11)

  def test_getNextMessage(self):
    count = counter.SimpleCounter(0)
    with self.assertRaises(Exception):
      count.getNextMessage(123)
    strVal = count.getNextMessage("Hello")
    self.assertEqual(strVal, "[0] Hello")
    self.assertEqual(count.getNextMessage("Bye"), "[1] Bye")
    self.assertEqual(count.getNextMessage("hey"), "[2] hey")
    self.assertEqual(count.getNextMessage("just a sumple string"), "[3] just a sumple string")

  def test_getNextIntAndMessage(self):
    count = counter.SimpleCounter(55)
    self.assertEqual(count.getNextMessage("random string here"), "[55] random string here")
    self.assertEqual(count.getNextInt(), 56)
    self.assertEqual(count.getNextInt(), 57)
    self.assertEqual(count.getNextMessage("random string here"), "[58] random string here")
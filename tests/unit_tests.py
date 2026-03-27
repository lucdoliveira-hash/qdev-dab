import unittest
from dab.account import *

class checkWithdrawalUnitTests(unittest.TestCase):
  def test_checkWithdrawal(self):
    self.assertEqual(checkWithdrawal(500,5), True)
    self.assertEqual(checkWithdrawal(300,500), False)
    self.assertEqual(checkWithdrawal(600,501), False)
    self.assertEqual(checkWithdrawal(600,-5), False)

if __name__ == '__main__':
  unittest.main()

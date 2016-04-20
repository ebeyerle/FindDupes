import unittest
import os, sys
sys.path.append("..")
# import stack
import findDupes

class TestFindDupes(unittest.TestCase):
  def setUp(self):
    self.find = findDupes.FindDupes()
    self.find.walk("..")
#    self.find = findDupes.walk(os.listdir("../folder"))

  def tearDown(self):
    while not self.find.files.empty():
      self.find.files.pop()
    while not self.find.dirs.empty():
      self.find.dirs.pop()
    while not self.find.dupes.empty():
      self.find.dupes.pop()

  def testWalk(self):
#    self.walk(os.listdir("../folder"))
    self.assertEqual(self.find.files.empty(), False)

#  def testDupes(self):
#    self.assertFalse(self.find.empty(), True)

if __name__ == "__main__":
  unittest.main()  

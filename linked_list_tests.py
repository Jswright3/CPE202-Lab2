"""
LAB2
CPE 202
John Wright
"""
import unittest
from linked_list import *


class TestCase(unittest.TestCase):


   def test_insert(self):
      lst = Node(3, Node(4, Node(5, None)))
      lst3 = None
      newlst = insert(lst, 3, 1)
      newlst2 = insert(lst, 2, 2)
      newlst3 = insert(lst3, 0, 0)
      self.assertAlmostEqual(newlst, Node(3, Node(3, Node(4, Node(5, None)))))
      self.assertAlmostEqual(newlst, Node(3, Node(4, Node(2, Node(5, None)))))
      self.assertAlmostEqual(newlst3, Node(0, None))

   def test_size(self):
      lst = Node(3, Node(4, Node(5, None)))
      lst2 = Node(3, None)
      self.assertAlmostEqual(size(lst), 3)
      self.assertAlmostEqual(size(lst2), 1)

   def test_get(self):
      lst = Node(3, Node(4, Node(5, None)))
      self.assertRaises(IndexError, get, lst, 6)
      num = get(lst, 2)
      self.assertAlmostEqual(num, 5)
      num2 = get(lst, 1)
      self.assertAlmostEqual(num2, 4)
      num3 = get(lst, 0)
      self.assertAlmostEqual(num3, 3)

   def test_contains(self):
      lst = Node(3, Node(4, Node(5, None)))
      self.assertTrue(contains(lst, 3))
      self.assertFalse(contains(lst, 8))

   def test_search(self):
      lst = Node(3, Node(4, Node(5, None)))
      self.assertAlmostEqual(search(lst, 5), 2)
      self.assertAlmostEqual(search(lst, 3), 0)

   def test_remove(self):
      lst = Node(3, Node(4, Node(5, None)))
      newlst = remove(lst, 3)
      self.assertAlmostEqual(newlst, Node(4, Node(5, None)))

   def test_pop(self):
      lst = Node(3, Node(4, Node(5, None)))
      newlst = remove(lst, 3)
      self.assertAlmostEqual(newlst, Node(4, Node(5, None)))
      self.assertRaises(IndexError, pop, lst, -1)



def main():
   # execute unit tests
   unittest.main()


if __name__ == '__main__':
   # execute main() function
   main()

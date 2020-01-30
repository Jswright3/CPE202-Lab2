"""
LAB2
CPE 202
John Wright
"""
import unittest
from array_list import *


class TestCase(unittest.TestCase):
   def test_enlarge(self):
      lst = ArrayList(2,0,[None,None])
      newlst = enlarge(lst)
      self.assertEqual(newlst.capacity,4)
      lst2 = ArrayList(4, 0, [None, None, None, None])
      newlst2 = enlarge(lst2)
      self.assertEqual(newlst2.capacity, 8)

   def test_shrink(self):
      lst = ArrayList(2, 0, [None, None])
      newlst = shrink(lst)
      self.assertEqual(newlst.capacity, 1)
      lst2 = ArrayList(8, 0, [None, None, None, None, None, None, None, None])
      newlst2 = shrink(lst2)
      self.assertEqual(newlst2.capacity, 4)

   def test_insert(self):
      lst = ArrayList(2, 1, [1, None])
      newlst = insert(lst, 3, 1)
      self.assertEqual(newlst, ArrayList(2, 2, [1, 3]))
      lst2 = ArrayList(4, 4, [1, 2, 3, 4])
      newlst2 = insert(lst2, 4, 2)
      self.assertEqual(newlst2, ArrayList(8, 5, [1, 2, 4, 3, 4, None, None, None]))

   def test_get(self):
      lst = ArrayList(4, 3, [1, 2, 3, None])
      self.assertRaises(IndexError, get, lst, 6)
      num = get(lst, 2)
      self.assertEqual(num, 3)
      num2 = get(lst, 1)
      self.assertEqual(num2, 2)

   def test_contains(self):
      lst2 = ArrayList(4, 3, [1, 2, 3, None])
      self.assertTrue(contains(lst2, 3))
      self.assertFalse(contains(lst2, 4))
      lst = ArrayList()
      for i in range(10):
         lst = insert(lst, i, 0)
      self.assertTrue(contains(lst, 0))

   def test_search(self):
      lst = ArrayList(4, 3, [1, 2, 3, None])
      self.assertEqual(search(lst, 3), 2)
      self.assertEqual(search(lst, 1), 0)
      self.assertEqual(search(lst, 2), 1)
      self.assertIsNone(search(lst, 4))

   def test_remove(self):
      lst = ArrayList(4, 3, [1, 2, 3, None])
      newlst = remove(lst, 2)
      newlst2 = remove(lst, 1)
      self.assertEqual(newlst.arr, [1, 3, 3, None])
      self.assertEqual(newlst2.arr, [2, 2, 3, None])

   def test_pop(self):
      lst = ArrayList(4, 3, [1, 2, 3, None])
      newlst = pop(lst, 1)
      newlst = newlst[0]
      newlst2 = pop(lst, 0)
      newlst2 = newlst2[0]
      self.assertEqual(newlst.arr, [1, 3, 3, None])
      self.assertEqual(newlst2.arr, [2, 2, 3, None])
      self.assertRaises(IndexError, pop, lst, -1)

   def test_size(self):
      lst = ArrayList(4, 3, [1, 2, 3, None])
      self.assertAlmostEqual(size(lst), 3)


def main():
   # execute unit tests
   unittest.main()

if __name__ == '__main__':
   # execute main() function
   main()

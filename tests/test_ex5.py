# coding: UTF-8

from unittest import TestCase
from ex5 import unique

class Ex5Test(TestCase):
    def test_unique(self):
        self.assertEqual([1,2,3,4,5], unique([1,2,3,3,3,4,5,5,5]))

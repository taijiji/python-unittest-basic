# coding: UTF-8

from unittest import TestCase
from ex1 import sum

class Ex1Test(TestCase):
    def test_sum(self):
        self.assertEqual(55, sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

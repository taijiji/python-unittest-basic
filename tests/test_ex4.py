# coding: UTF-8

from unittest import TestCase
from ex4 import mod

class Ex4Test(TestCase):
    def test_mod(self):
        self.assertEqual(1, mod(5,4))

# coding: UTF-8

from unittest import TestCase
from ex6 import count

class Ex6Test(TestCase):
    def test_count(self):
        self.assertEqual( '1(3) 3(3)', count('1 3 1 1 3 3') )

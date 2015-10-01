# coding: UTF-8

from unittest import TestCase
from ex2 import reverse


class Ex2Test(TestCase):
    def test_reverse(self):
        self.assertEqual('gnirts', reverse('string'))

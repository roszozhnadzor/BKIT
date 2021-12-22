# -*- coding: utf-8 -*-

import unittest
from main import user, reg


class Testing(unittest.TestCase):
    def setUp(self):
        self.user = user()
        self.reg = reg()

    def test_tel(self):
        self.user.tel_user = 79893003090
        self.reg.tel.set()
        self.assertEqual(self.user.tel_user, 79893003090)

    def test_name(self):
        self.user.name_user = "мария"
        self.reg.name.set()
        self.assertEqual(self.user.name_user, "мария")

    def test_surname(self):
        self.user.fname_user = "гурова"
        self.reg.fname.set()
        self.assertEqual(self.user.fname_user, "гурова")


if __name__ == "__main__":
    unittest.main()
import unittest

from python.calc import Calc


class Testcalc(unittest.TestCase):
    def test_add_1(self):
        self.calc=Calc()
        result=self.calc.add(1,2)
        print(result)
        self.assertEqual(3,result)




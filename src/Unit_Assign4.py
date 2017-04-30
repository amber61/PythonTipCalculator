'''
 File Name: Unit_Assign4.py
 Author Name: Zhe Huang
 Date: 2017-03-24
 Description: This file is used to test new added functions in assign3.
'''
import unittest
# import class Application from Assign4.py file
from Assign4 import Application
from Assign4 import IInterface

# class to do unittest
class UnitAssign4(unittest.TestCase):
    #Test Assign4.py

    # test each person total expense
    def test_sum_person(self):
        app = Application()
        L = [2, 3]
        self.assertEqual(app.sum_person(L), 5)

    # test constructor of IInterface
    def test_method(self):
        inter = IInterface()
        self.assertEqual(inter.__init__(), None)

# main entry
if __name__ == '__main__':
    unittest.main()
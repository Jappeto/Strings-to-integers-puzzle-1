#Test_StrToInt2.py
#Jacob Reppeto

import unittest
import strToInt2

class Test_StrToInt(unittest.TestCase):

    def test_strToInt2(self):
        self.assertEqual(strToInt2.strToInt2("phonetw3oneighty"), 1318)
        self.assertEqual(strToInt2.strToInt2("onxonbexighnte"), None)
        self.assertEqual(strToInt2.strToInt2("tw3xo4n5sio8nxe"), 3458)
        self.assertEqual(strToInt2.strToInt2("onxonbeightwo"), 82)
        self.assertEqual(strToInt2.strToInt2(""), None)
        self.assertEqual(strToInt2.strToInt2("twoneighthree"), 2183)
        self.assertEqual(strToInt2.strToInt2("nineighthreighte"), 988)


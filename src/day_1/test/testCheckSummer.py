import unittest
from collections import Counter
import checkSummer

class testBoxNRepeat(unittest.TestCase):

    def setUp(self):
        self.emptyString = Counter(list(""))
        self.norepeat = Counter(list("no"))
        self.repeat2n = Counter(list("non"))
        self.repeat3n = Counter(list("nonn"))
    
    def test_EmptyString(self):
        self.assertFalse(checkSummer.box_has_n_repeat(0, self.emptyString))
    
    def test_NoRepeat(self):
        self.assertFalse(checkSummer.box_has_n_repeat(2, self.norepeat))

    def test_Repeat2n(self):
        self.assertTrue(checkSummer.box_has_n_repeat(2, self.repeat2n))
    
    def test_Repeat3n(self):
        self.assertTrue(checkSummer.box_has_n_repeat(3, self.repeat3n))

class testBox32Repeat(unittest.TestCase):

    def setUp(self):
        self.emptyString = Counter(list(""))
        self.norepeat = Counter(list("no"))
        self.repeat2n = Counter(list("non"))
        self.repeat3n = Counter(list("nonn"))
        self.repeat3n2o = Counter(list("nonno"))

        self.zerozero = {2:0, 3:0}
        self.zero_2_n_3 = {2:0, 3:1}
        self.n_2_zero_3 = {2:1, 3:0}
        self.o_2_n_3 = {2:1, 3:1}
    
    def test_EmptyString(self):
        self.assertEqual( self.zerozero, checkSummer.box_2_3_counts(self.emptyString))
    
    def test_NoRepeat(self):
        self.assertEqual(self.zerozero, checkSummer.box_2_3_counts(self.norepeat))

    def test_Repeat2n(self):
        self.assertEqual(self.n_2_zero_3,checkSummer.box_2_3_counts(self.repeat2n))
    
    def test_Repeat3n(self):
        self.assertEqual(self.zero_2_n_3, checkSummer.box_2_3_counts(self.repeat3n))
    
    def test_Repeat3n2o(self):
        self.assertEqual(self.o_2_n_3, checkSummer.box_2_3_counts(self.repeat3n2o))

class TestdictAdder(unittest.TestCase):

    def setUp(self):
        self.zerozero = {2:0, 3:0}
        self.zero_2_n_3 = {2:0, 3:1}
        self.n_2_zero_3 = {2:1, 3:0}
        self.o_2_n_3 = {2:1, 3:1}
    
    def testZero(self):
        self.assertEqual(self.zerozero, checkSummer.dict_adder(self.zerozero, self.zerozero))
    
    def test2_1_3_0(self):
        self.assertEqual(self.n_2_zero_3, checkSummer.dict_adder(self.zerozero, self.n_2_zero_3))

if __name__ == '__main__':
    unittest.main()
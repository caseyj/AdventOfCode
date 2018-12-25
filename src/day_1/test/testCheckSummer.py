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
        self.assertTrue(checkSummer.box_has_n_repeat(2, self.repeat3n))

if __name__ == '__main__':
    unittest.main()
import unittest 
import frequency

class testDetectOperation(unittest.TestCase):

    def setUp(self):
        self.test_0_empty = "" #raise typeError
        self.test_1_add = "+" #add enum
        self.test_2_sub = "-" #sub enum
        self.test_3_wrong_type = "should be wrong" #raise typeerror
    
    def testEmpty(self):
        with self.assertRaises(TypeError):
            frequency.detect_operation(self.test_0_empty)
    
    def testWrongType(self):
        with self.assertRaises(TypeError):
            frequency.detect_operation(self.test_3_wrong_type)
    
    def testAdd(self):
        self.assertEqual(frequency.Operation.add, frequency.detect_operation(self.test_1_add))
    
    def testSub(self):
        self.assertEqual(frequency.Operation.sub, frequency.detect_operation(self.test_2_sub))




if __name__ == '__main__':
    unittest.main()
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

class testDetectInteger(unittest.TestCase):

    def setUp(self):
        self.test_empty = "" #raise typeerror
        self.test_positive_1 = "1"
        self.test_letter = "asdasda" #raise typeerror

    def testEmpty(self):
        with self.assertRaises(TypeError):
            frequency.detect_integer(self.test_empty)
    
    def testPositive1(self):
        self.assertEqual(1, frequency.detect_integer(self.test_positive_1))
    
    def testLetter(self):
        with self.assertRaises(TypeError):
            frequency.detect_integer(self.test_letter)

class testSplitString(unittest.TestCase):

    def setUp(self):
        self.Empty = ""
        self.Thing = "somethingElse"
        self.add = "+"
        self.sub = "-"
        self.one = "1"
    
    def testopTypeErr(self):
        with self.assertRaises(TypeError):
            frequency.split_string(self.Empty+self.one)
    
    def testintegerTypeErr(self):
        with self.assertRaises(TypeError):
            frequency.split_string(self.add+self.Empty)
    
    def testAddwrongThing(self):
        with self.assertRaises(TypeError):
            frequency.split_string(self.add+self.Thing)
        
    def testAdd1(self):
        thing = frequency.split_string(self.add+self.one)
        self.assertEqual(frequency.Operation.add, thing.op_direction)
        self.assertEqual(1, thing.op_integer)
    
    def testSub1(self):
        thing = frequency.split_string(self.sub+self.one)
        self.assertEqual(frequency.Operation.sub, thing.op_direction)
        self.assertEqual(1, thing.op_integer)


class testOpActionRun(unittest.TestCase):

    def setUp(self):
        self.minus_1 = frequency.split_string("-1")
        self.plus_1 = frequency.split_string("+1")
    
    def testRunEmptyInput(self):
        self.assertEqual(-1, self.minus_1.run())
        self.assertEqual(1, self.plus_1.run())
    
    def testRunMin1(self):
        self.assertEqual(-2, self.minus_1.run(-1))
        self.assertEqual(0, self.plus_1.run(-1))

    def testRunAdd1(self):
        self.assertEqual(0, self.minus_1.run(1))
        self.assertEqual(2, self.plus_1.run(1))
    



if __name__ == '__main__':
    unittest.main()
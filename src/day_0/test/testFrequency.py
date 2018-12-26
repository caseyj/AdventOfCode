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
    
class testMultiOpsRun(unittest.TestCase):
    def setUp(self):
        self.minus_1 = frequency.split_string("-1")
        self.plus_1 = frequency.split_string("+1")
    
    def testNone(self):
        self.assertEqual(0, frequency.multi_ops_run())
    
    def testMin1x3(self):
        min3 = [self.minus_1, self.minus_1, self.minus_1]
        self.assertEqual(-3, frequency.multi_ops_run(min3))

    def testPlus1x3(self):
        plus3 = [self.plus_1, self.plus_1, self.plus_1]
        self.assertEqual(3, frequency.multi_ops_run(plus3))        
    
    def testPlus1Min1(self):
        zero = [self.plus_1, self.minus_1]
        self.assertEqual(0, frequency.multi_ops_run(zero))

class testdetRepeat(unittest.TestCase):

    def setUp(self):
        self.minus_1 = frequency.split_string("-1")
        self.plus_1 = frequency.split_string("+1")
        self.plus_3 = frequency.split_string("+3")
        self.minus_4 = frequency.split_string("-4")
        self.plus_4 = frequency.split_string("+4")
        self.minus_2 = frequency.split_string("-2")
        self.plus_2 = frequency.split_string("+2")
        self.minus_5 = frequency.split_string("-5")
        self.plus_5 = frequency.split_string("+5")
        self.minus_8 = frequency.split_string("-8")
        self.plus_8 = frequency.split_string("+8")
        self.minus_7 = frequency.split_string("-7")
        self.plus_7 = frequency.split_string("+7")
        self.minus_6 = frequency.split_string("-6")
        self.plus_6 = frequency.split_string("+6")

    def test0(self):
        testCase = [self.minus_1, self.plus_1]
        self.assertEqual(0, frequency.det_repeat(testCase))
    
    def test10(self):
        testCase = [self.plus_3, self.plus_3, self.plus_4, self.minus_2, self.minus_4]
        self.assertEqual(10, frequency.det_repeat(testCase))
    
    def test5(self):
        testCase = [self.minus_6, self.plus_3, self.plus_8, self.plus_5, self.minus_6]
        self.assertEqual(5, frequency.det_repeat(testCase))
    
    def test14(self):
        testCase = [self.plus_7, self.plus_7, self.minus_2, self.minus_7, self.minus_4]
        self.assertEqual(14, frequency.det_repeat(testCase))


if __name__ == '__main__':
    unittest.main()
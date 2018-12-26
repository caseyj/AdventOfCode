import fabricSplit
import unittest

class TestGenerateClaims(unittest.TestCase):

    def setUp(self):
        self.fabricTrack = fabricSplit.FabricTracker()
        self.onexone = [0,0,1,1] #1x1 grid with coords [(0,0)]
        self.twoxtwo_off1_1 = [1,1,2,2] #2x2 grid with coords [(1,1),(1,2),(2,1),(2,2)]
        self.five_5_2x2 = [5,5,2,2]

        
        self.onexone_correct = [(0,0)]
        self.twoxtwo_off1_1_correct = [(1,1),(1,2),(2,1),(2,2)]
        self.five_5_2x2_correct = [(5,5),(5,6),(6,5),(6,6)]
    
    def testOneXOne(self):
        self.assertEqual(
            self.onexone_correct, 
            self.fabricTrack.generate_claims(
                self.onexone[0], 
                self.onexone[1], 
                self.onexone[2], 
                self.onexone[3]
            )
        )
    
    def testTwoXTwo(self):
        self.assertEqual(
            self.twoxtwo_off1_1_correct, 
            self.fabricTrack.generate_claims(
                self.twoxtwo_off1_1[0], 
                self.twoxtwo_off1_1[1], 
                self.twoxtwo_off1_1[2], 
                self.twoxtwo_off1_1[3]
            )
        )
    
    def testFiveFive2x2(self):
        self.assertEqual(
            self.five_5_2x2_correct, 
            self.fabricTrack.generate_claims(
                self.five_5_2x2[0], 
                self.five_5_2x2[1], 
                self.five_5_2x2[2], 
                self.five_5_2x2[3]
            )
        )

class TestGenerateClaim(unittest.TestCase):

    def setUp(self):
        self.one_1_4x4 = "#1 @ 1,3: 4x4"
        self.three_1_4x4 = "#2 @ 3,1: 4x4"
        self.five_5_2x2 = "#3 @ 5,5: 2x2"
    
    def testOne_1_4x4(self):
        self.assertEqual([1,3,4,4], fabricSplit.generate_claim(self.one_1_4x4))
    
    def testThree_1_4x4(self):
        self.assertEqual([3,1,4,4], fabricSplit.generate_claim(self.three_1_4x4))
    
    def testFive_5_2x2(self):
        self.assertEqual([5,5,2,2], fabricSplit.generate_claim(self.five_5_2x2))